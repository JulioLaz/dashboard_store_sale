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

# Style en navbar:
sm.style_navbar()
st.markdown("""<style>[data-testid="stSidebar"] {background-color: rgba(0,0,0,0);}</style>""",unsafe_allow_html=True)

# ocultar label del ratioitems:
hide_element_style = '''<style>#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(9) > div > label {display: none}'''
st.markdown(hide_element_style, unsafe_allow_html=True)

def create_multiselect_filter(df, column, label):
    options = ["ALL"] + list(df[column].unique())
    selected = st.sidebar.multiselect(
        label,
        options=options,
        default=["ALL"],
        key=f"{column}_filter"
    )
    if "ALL" in selected:
        return df[column].unique()
    return selected

# years=list(db.load_data().Year.unique())
df_regiones= db.load_pop_pbi_region()
def main():
    df = db.load_data()


# Obtener las marcas top_n y asignar los colores
    fluorescent_colors = ['#39FF14', '#FF1493', '#00FFFF', '#FFFF00', '#FF00FF',                 '#FF4500', '#7FFF00', '#00FF7F', '#00CED1', '#FFD700']
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
        all_years = st.sidebar.checkbox('Todo el periodo', value=True)
        
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
    marca_filter = create_multiselect_filter(df, 'marca', "Marca")
    producto_filter = create_multiselect_filter(df, 'producto', "Producto")
    ciudad_filter = create_multiselect_filter(df, 'Estado', "Estado")
    Región_filter = create_multiselect_filter(df, 'Región', "Región")
    vendedor_filter = create_multiselect_filter(df, 'nombre_vendedor', "Vendedor")
    marca_genero_filter = create_multiselect_filter(df, 'marca_genero', "Género")

    top_n = int(st.sidebar.radio("TOP", options=['3', '5', '10'], index=0, key="top", horizontal=True))

    sm.style_gen() # CSS personalizado

    mask = (
        (df['nombre_vendedor'].isin(vendedor_filter)) &
        (df['Estado'].isin(ciudad_filter)) &
        (df['marca'].isin(marca_filter)) &
        (df['producto'].isin(producto_filter)) &
        (df['Región'].isin(Región_filter)) &
        (df['marca_genero'].isin(marca_genero_filter)) &
        (df['fecha_compra'].dt.year.isin(selected_years))
        # (df['fecha_compra'].dt.year.isin(years_filter))
    )
    filtered_df = df[mask]

    sm.style_title()

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
        col1.markdown("<div class='metric-title'>Total de Ventas</div>", unsafe_allow_html=True)
        col1.metric("", formata_numero(filtered_df['valor_total'].sum(),'$'), delta=sales_change,label_visibility="hidden")
        
        # Ganancia Neta
        current_profit = current_data['ingresos_netos'].sum()
        previous_profit = previous_data['ingresos_netos'].sum()
        profit_change = calculate_change(current_profit, previous_profit)
        if previous_profit!=0:
            profit_change=f"{profit_change:.2%}"
        else: profit_change="sin perído previo"        
        col2.markdown("<div class='metric-title'>Ganancia Neta</div>", unsafe_allow_html=True)
        col2.metric("", formata_numero(filtered_df['ingresos_netos'].sum(),'$'), delta=profit_change)
        
        # Número de Pedidos
        current_orders = current_data['pedido_id'].nunique()
        previous_orders = previous_data['pedido_id'].nunique()
        orders_change = calculate_change(current_orders, previous_orders)
        if previous_orders!=0:
            orders_change=f"{orders_change:.2%}"
        else: orders_change="sin perído previo"          
        col3.markdown("<div class='metric-title'>Número de Pedidos</div>", unsafe_allow_html=True)
        col3.metric("", formata_numero(current_orders,''), delta=orders_change)
        # col3.metric("", f"{current_orders:,}", delta=orders_change)
        
        # Marcas
        current_brands = current_data['marca'].nunique()
        previous_brands = previous_data['marca'].nunique()
        brands_change = calculate_change(current_brands, previous_brands)
        if previous_brands!=0:
            brands_change=f"{brands_change:.2%}"
        else: brands_change="sin perído previo"         
        col4.markdown("<div class='metric-title'>Marcas</div>", unsafe_allow_html=True)
        col4.metric("", f"{current_brands:,}", delta=brands_change)
        
        # Productos
        current_products = current_data['producto'].nunique()
        previous_products = previous_data['producto'].nunique()
        products_change = calculate_change(current_products, previous_products)
        if previous_products!=0:
            products_change=f"{products_change:.2%}"
        else: products_change="sin perído previo"          
        col5.markdown("<div class='metric-title'>Productos</div>", unsafe_allow_html=True)
        col5.metric("", f"{current_products:,}", delta=products_change)
    dashboard_metrics(filtered_df)

    col1, col2,col3 = st.columns(3)
    with col1: #ventas por años line:
        ys.sales_line(filtered_df)
    with col2: #ventas por años pie:
        ys.sales_pie(filtered_df)
    with col3: #ventas por años pie:
        # ys.enhanced_condition_treemap(filtered_df)
        # ys.sunburst_chart(filtered_df)
        ys.condition_pie(filtered_df)
        # ys.condition_treemap(filtered_df)

    col1, col2 = st.columns(2)
    with col1: #Vendedores por años
        seller.seller(filtered_df)
    with col2: # Vendedores total ventas distribucion:
        seller.seller_pie(filtered_df)

    ### regiones:
    col4, col1, col2, col3 = st.columns(4)
    with col1:
        region.region_barras(filtered_df)
    with col2:
        region.pop_pie(filtered_df)
    with col3:
        region.pbi_treemap(df_regiones)
    with col4:
        region.mapa_br_reg(filtered_df)

    ### MAPA 
    col5, col6 = st.columns(2)
    with col5: #Mapa de brasil ventas totales por Estado:
        mapa.mapa_br(filtered_df)
    with col6: # Top 10 de Venta totales neta por estado
        mapa.barras(filtered_df)


    # Crear dos columnas principales
    col_left, col_right = st.columns(2)
    color_map=assign_colors(df)

    with col_left:
        col1, col2 = st.columns(2)
        with col1: #"Top Marcas según Ganancia Neta"
            prbr.graf_011(filtered_df, top_n, color_map)
        with col2: #"Jerarquía de Ventas por Marca y Producto"
            prbr.treemap_brands_products(filtered_df, top_n, color_map)

    with col_right:
        prbr.sales_line_top(filtered_df, top_n, color_map) #"Ingresos Mensuales por Marca"

    ### PRODUCTOS
    col3, col4 ,col5 ,col6 = st.columns(4)
    with col3: # Top 10 productos más costosos
        prup.graf_01(filtered_df,top_n)
    with col4: # Top 10 productos agrupados por tipo con mayores ventas
        prup.graf_02(filtered_df,top_n)
    with col5:
        prup.graf_03(filtered_df,top_n)
    with col6: # Top 10 marcas según ganancia neta
        prup.graf_022(filtered_df,top_n)

    pe.profit_evol(filtered_df)
if __name__ == '__main__':
    main()