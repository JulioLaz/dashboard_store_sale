import numpy as np
import streamlit as st
import ddbb as db
import navbar as nb
import top10_profits_brands_products as prbr
import top10_products_up as prup
import mapa_brasil as mapa
import style_markdown as sm
import years_sales as ys
import vendedor as seller
import graf_region as region
import profit_evolution as pe

def formata_numero(valor, prefijo=''):
    for unidad in ['', 'k']:
        if valor < 1000:
            return f'{prefijo} {valor:.2f} {unidad}'
        valor /= 1000
    return f'{prefijo} {valor:.2f} M'

st.set_page_config(page_title="Ventas ecommerce Brazil", page_icon=":shopping_bags:", layout="wide")

titles_format = dict(font=dict(size=18, color='#1f77b4'), xref='paper', x=0.5, y=0.95, xanchor='center', yanchor='top')

sm.style_navbar() # Style en navbar:


# # ocultar label del ratioitems:
hide_element_style = '''<style>#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(9) > div > label {display: none}'''
st.markdown(hide_element_style, unsafe_allow_html=True)

def create_multiselect_filter(df, column, label):
    all_values = list(df[column].unique())
    
    # Checkbox para seleccionar todos los valores
    all_selected = st.sidebar.checkbox(f'All {label}', value=True, key=f"all_{column}_checkbox")
    
    if all_selected:
        return all_values
    else:
        # Si no se seleccionan todos, mostrar el multiselect
        selected = st.sidebar.multiselect(
            label,
            options=all_values,
            default=[],
            key=f"{column}_multiselect"
        )
        if not selected:
            # st.sidebar.warning(f"No hay selección para {label}. Se usarán todos los valores.")
            return df[column].unique()
        return selected
# def create_multiselect_filter(df, column, label):
#     options = ["ALL"] + list(df[column].unique())
#     selected = st.sidebar.multiselect(
#         label,
#         options=options,
#         default=["ALL"],
#         key=f"{column}_filter")
#     if "ALL" in selected:
#         return df[column].unique()
#     if not selected:
#         st.sidebar.warning(f"No hay selección para {label}. Por favor, seleccione al menos un valor.")
#         return df[column].unique()
#     return selected

years=list(db.load_data().Year.unique())
df_regiones= db.load_pop_pbi_region()

def main():
    df = db.load_data()
    fluorescent_colors = ['#39FF14', '#FF1493', '#00FFFF', '#FFFF00', '#FF00FF', '#FF4500', '#7FFF00', '#00FF7F', '#00CED1', '#FFD700']
    def assign_colors(df):
        top_brands = df.groupby('marca')['valor_total'].sum().nlargest(10).index
        color_map = {brand: fluorescent_colors[i] for i, brand in enumerate(top_brands)}
        return color_map

    # Barra lateral
    with st.sidebar:
        st.markdown("<h1></h1>", unsafe_allow_html=True)

    nb.create_navbar()

    def year_filter(df):
        years = sorted(df['fecha_compra'].dt.year.unique())
        
        # Checkbox para seleccionar todo el periodo
        all_years = st.sidebar.checkbox('All Periods', value=True)
        
        if all_years:
            years_filter = years
        else:
            selected_year = st.sidebar.radio("", options=years[:], index=0, key="year_radio", horizontal=True)
            if selected_year == "ALL":
                years_filter = df['fecha_compra'].dt.year.unique()
            else:
                years_filter = [selected_year]

        # Aplicar el filtro al dataframe
        filtered_df = df[df['fecha_compra'].dt.year.isin(years_filter)]
        
        return filtered_df, years_filter
    
    filtered_df, selected_years = year_filter(df)

    # Filtros de selección múltiple con opción "ALL"
    marca_filter = create_multiselect_filter(df, 'marca', "Brand")
    producto_filter = create_multiselect_filter(df, 'producto', "Product")
    Región_filter = create_multiselect_filter(df, 'Región', "Region")
    ciudad_filter = create_multiselect_filter(df, 'Estado', "State")
    vendedor_filter = create_multiselect_filter(df, 'nombre_vendedor', "Seller")
    # marca_genero_filter = create_multiselect_filter(df, 'marca_genero', "Género")
    marca_genero_filter = create_multiselect_filter(df, 'condicion', "Condition")
    st.sidebar.subheader("Top", divider="gray")

    top_n = int(st.sidebar.radio("", options=['3', '5', '10'], index=0, key="top", horizontal=True))

    sm.style_gen() # CSS personalizado

    mask = (
        (df['nombre_vendedor'].isin(vendedor_filter)) &
        (df['Estado'].isin(ciudad_filter)) &
        (df['marca'].isin(marca_filter)) &
        (df['producto'].isin(producto_filter)) &
        (df['Región'].isin(Región_filter)) &
        (df['condicion'].isin(marca_genero_filter)) &
        # (df['marca_genero'].isin(marca_genero_filter)) &
        (df['fecha_compra'].dt.year.isin(selected_years))
        # (df['fecha_compra'].dt.year.isin(years_filter))
    )
    filtered_df = df[mask]

    # Verificar si el DataFrame filtrado está vacío
    # if filtered_df.empty:
    #     st.warning("No hay datos disponibles para los filtros seleccionados. Por favor, ajusta los filtros.")
    #     return
#### metric with indicator
    def calculate_change(current, previous):
        if previous == 0:
            return 0
        return (current - previous) / previous

    def get_previous_period_data(df, date_column='Year'):
        current_period = df[date_column].max()
        previous_period = df[df[date_column] < current_period][date_column].max()
        if previous_period==np.nan:
            previous_period=previous_period
        else: 
            previous_period=current_period-1
        current_data = df[df[date_column] == current_period]
        previous_data = db.load_data()[db.load_data()[date_column] == previous_period]
        return current_data, previous_data

    def dashboard_metrics(filtered_df):
        current_data, previous_data = get_previous_period_data(filtered_df)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        # Total de Ventas
        current_sales = current_data['valor_total'].sum()
        previous_sales = previous_data['valor_total'].sum()
        sales_change = calculate_change(current_sales, previous_sales)
        if previous_sales!=0:
            sales_change=f"{sales_change:.2%}"
        else: sales_change="sin perído previo"
        col1.markdown("<span style='color: #00ff00;font-size:1.5rem'>Total de Ventas</span>", unsafe_allow_html=True)
        col1.metric("", formata_numero(filtered_df['valor_total'].sum(),'$'), delta=sales_change, label_visibility="hidden")
        
        # Ganancia Neta
        current_profit = current_data['ingresos_netos'].sum()
        previous_profit = previous_data['ingresos_netos'].sum()
        profit_change = calculate_change(current_profit, previous_profit)
        if previous_profit!=0:
            profit_change=f"{profit_change:.2%}"
        else: profit_change="sin perído previo"        
        col2.markdown("<span style='color: #00ff00;font-size:1.5rem'>Ganancia Neta</span>", unsafe_allow_html=True)
        col2.metric("", formata_numero(filtered_df['ingresos_netos'].sum(),'$'), delta=profit_change)
        
        # Número de Pedidos
        current_orders = current_data['pedido_id'].nunique()
        previous_orders = previous_data['pedido_id'].nunique()
        orders_change = calculate_change(current_orders, previous_orders)
        if previous_orders!=0:
            orders_change=f"{orders_change:.2%}"
        else: orders_change="sin perído previo"          
        col3.markdown("<span style='color: #00ff00;font-size:1.5rem'>Número de Pedidos</span>", unsafe_allow_html=True)
        col3.metric("", formata_numero(current_orders,''), delta=orders_change)
        # col3.metric("", f"{current_orders:,}", delta=orders_change)
        
        # Marcas
        current_brands = current_data['marca'].nunique()
        previous_brands = previous_data['marca'].nunique()
        brands_change = calculate_change(current_brands, previous_brands)
        if previous_brands!=0:
            brands_change=f"{brands_change:.2%}"
        else: brands_change="sin perído previo"         
        col4.markdown("<span style='color: #00ff00;font-size:1.5rem'>Marcas</span>", unsafe_allow_html=True)
        col4.metric("", f"{current_brands:,}", delta=brands_change)
        
        # Productos
        current_products = current_data['producto'].nunique()
        previous_products = previous_data['producto'].nunique()
        products_change = calculate_change(current_products, previous_products)
        if previous_products!=0:
            products_change=f"{products_change:.2%}"
        else: products_change="sin perído previo"          
        col5.markdown("<span style='color: #00ff00;font-size:1.5rem'>Productos</span>", unsafe_allow_html=True)
        col5.metric("", f"{current_products:,}", delta=products_change)
    
    dashboard_metrics(filtered_df)

    # def show_sales_and_sellers():
    st.subheader("Sales & Sellers")
    tab1, tab2, tab3 = st.tabs(["Profits & Sales", "Sales vs Condition & Genre",'Seller'])

    with tab1: 
        col1, col2 = st.columns(2)
        with col1:
            ys.sales_line(filtered_df) #ventas por años line:
        with col2:
            ys.sales_pie(filtered_df)  #ventas por años pie
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            ys.condition_pie(filtered_df) #ventas por condición pie
        with col2:
            ys.genre_pie(filtered_df) #ventas por genre pie
    with tab3: 
        col1, col2 = st.columns(2)         ### Sellers
        with col1:
            seller.seller(filtered_df)  #Vendedores por años
        with col2: 
            seller.seller_pie(filtered_df) # Vendedores total ventas distribucion:

        # st.markdown('''<div><img style='margin-bottom: 5px' src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=00ff00&size=30&center=true&vCenter=true&width=1000&height=36&duration=4000&lines=Análisis+por+Estados+y+Regiones:+Ventas,+población+y+PBI"></div>''', unsafe_allow_html=True)

    st.subheader("Regions & States")        ### regiones:
    tab1, tab2, tab3 = st.tabs(["Regions & Sales", "Population & PBI",'Sales for States'])
    
    with tab1: 

        col1, col2 = st.columns(2)
        with col1:
            region.mapa_br_reg(filtered_df)
        with col2:
            region.region_barras(filtered_df)

    with tab2:
        col3, col4 = st.columns(2)
        with col3:
            region.pop_pie(filtered_df)
        with col4:
            region.pbi_treemap(df_regiones)

    with tab3:
        col5, col6 = st.columns(2)
        with col5: 
            mapa.mapa_br(filtered_df)#Mapa de brasil ventas totales por Estado:
        with col6: 
            mapa.barras(filtered_df,top_n) # Top n de Venta totales neta por estado

       # st.markdown('''<div><img style='margin-bottom: 5px' src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=00ff00&size=30&center=true&vCenter=true&width=800&height=36&duration=2800&lines=Análisis+de+Productos+y+Marcas"></div>''', unsafe_allow_html=True)


    st.subheader("Brands & Products")        ### regiones:    
    color_map=assign_colors(df)
    tab1, tab2 = st.tabs(["Brands & Profits", "Monthly Profits per Brand"])
        
    with tab1:
            col1, col2 = st.columns(2)
            with col1: 
                prbr.graf_011(filtered_df, top_n, color_map) #"Top Marcas según Ganancia Neta"
            with col2: 
                prbr.treemap_brands_products(filtered_df, top_n, color_map) #"Jerarquía de Ventas por Marca y Producto"

    with tab2:
            prbr.sales_line_top(filtered_df, top_n, color_map) #"Ingresos Mensuales por Marca"

        ### PRODUCTOS
    tab1, tab2 = st.tabs(["Most Selled Products", "Products & Profits"])
    with tab1:
        col1, col2 = st.columns(2)
        with col1: # Top 10 productos más costosos
            prup.graf_01(filtered_df,top_n,fluorescent_colors)
        with col2: # Top 10 productos agrupados por tipo con mayores ventas
            prup.graf_02(filtered_df,top_n,fluorescent_colors)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            prup.graf_03(filtered_df,top_n,fluorescent_colors)
        with col2: # Top 10 marcas según ganancia neta
            prup.graf_022(filtered_df,top_n,fluorescent_colors)

        # st.markdown('''<div><img style='margin-bottom: 5px' src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=00ff00&size=30&center=true&vCenter=true&width=800&height=36&duration=2500&lines=Evolución+hitórica+de+Ganancias"></div>''', unsafe_allow_html=True)

    ### Evolunción de ventas
    st.subheader("Sales Evolution")       
    pe.profit_evol(filtered_df)


    nb.create_links()

if __name__ == '__main__':
    main()