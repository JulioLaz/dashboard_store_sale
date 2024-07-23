import streamlit as st
import pandas as pd
import plotly.express as px
import ddbb as db
import navbar as nb
import top10_profits_brands_products as prbr
import top10_products_up as prup
import mapa_brasil as mapa
import update_figure_layout as layout
import style_markdown as sm
import years_sales as ys
import vendedor as seller

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

# ocultar label del ratioitens:
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

def main():
    df = db.load_data()

    # Barra lateral
    with st.sidebar:
        st.markdown("<h1></h1>", unsafe_allow_html=True)
        st.markdown("<h1>Filtros</h1>", unsafe_allow_html=True)
        # nb.create_navbar()

    # Contenido principal
    st.title("Dashboard de Ventas")
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
        # else:
            # years_filter = df['fecha_compra'].dt.year.unique()

        # Aplicar el filtro al dataframe
        filtered_df = df[df['fecha_compra'].dt.year.isin(years_filter)]
        
        return filtered_df, years_filter

    filtered_df, selected_years = year_filter(df)
    # years = ["ALL"] + sorted(df['fecha_compra'].dt.year.unique())

    # if 'year_filter_mode' not in st.session_state:
    #    st.session_state.year_filter_mode = True

    # if st.session_state.year_filter_mode:
    #   selected_year = st.sidebar.radio("", options=years[:], index=0, key="year_radio", horizontal=True)
    #   if selected_year == "ALL":
    #      years_filter = df['fecha_compra'].dt.year.unique()
    #   else:
    #      years_filter = [selected_year]
    # else:
    #   years_filter = df['fecha_compra'].dt.year.unique()

    # Filtros de selección múltiple con opción "ALL"
    marca_filter = create_multiselect_filter(df, 'marca', "Marca")
    producto_filter = create_multiselect_filter(df, 'producto', "Producto")
    ciudad_filter = create_multiselect_filter(df, 'Estado', "Estado")
    Región_filter = create_multiselect_filter(df, 'Región', "Región")
    vendedor_filter = create_multiselect_filter(df, 'nombre_vendedor', "Vendedor")
    marca_genero_filter = create_multiselect_filter(df, 'marca_genero', "Género")

# CSS personalizado
    sm.style_gen()

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

    #### Métricas principales
    col1, col2, col3, col4,col5 = st.columns(5)

    col1.markdown(f" <div class='metric-title'>Total de Ventas</div>", unsafe_allow_html=True)
    col1.metric("Total de Ventas", formata_numero(filtered_df['valor_total'].sum(),'$'),label_visibility="hidden")

    col2.markdown(f" <div class='metric-title'>Ganancia Neta</div>", unsafe_allow_html=True)
    col2.metric("", formata_numero(filtered_df['ingresos_netos'].sum(),'$'))

    col3.markdown(f" <div class='metric-title'>Número de Pedidos</div>", unsafe_allow_html=True)
    col3.metric("", f"{filtered_df['pedido_id'].nunique():,}")

    col4.markdown(f" <div class='metric-title'>Marcas</div>", unsafe_allow_html=True)
    col4.metric("", f"{filtered_df['marca'].nunique():,}")

    col5.markdown(f" <div class='metric-title'>Productos</div>", unsafe_allow_html=True)
    col5.metric("", f"{filtered_df['producto'].nunique():,}")

    col1, col2 = st.columns(2)
    
    with col1: #ventas por años line:
        ys.sales_line(filtered_df)

    with col2: #ventas por años pie:
        ys.sales_pie(filtered_df)

    col1, col2 = st.columns(2)

    with col1: #Vendedores por años
        seller.seller(filtered_df)
    with col2: # Vendedores total ventas distribucion:
        seller.seller_pie(filtered_df)

    col5, col6 = st.columns(2)

    with col5: #Mapa de brasil ventas totales por Estado:
    # Mapa 
        grouped_df = filtered_df.groupby(['abbrev_state', 'Estado'])['valor_total'].sum().reset_index()
        mapa.mapa_br(grouped_df)

    with col6: # Top 10 de Venta totales neta por estado

        grouped_df = filtered_df.groupby(['abbrev_state', 'Estado'])['valor_total'].sum().reset_index()
        top_10_estados = filtered_df.groupby('Estado')['valor_total'].sum().nlargest(10).reset_index()
        mapa.barras(top_10_estados)

    col1, col2 = st.columns(2)

    with col1: #"Top 10 Marcas según Ganancia Neta"
        top_10_marcas = filtered_df.groupby('marca')['ingresos_netos'].sum().nlargest(10).reset_index().sort_values(by='ingresos_netos', ascending=False).reset_index(drop=True)
        prbr.graf_011(top_10_marcas)

    with col2: # Top 10 marcas según ganancia neta
        top_10_productos = filtered_df.groupby('producto')['ingresos_netos'].sum().nlargest(10).reset_index()
        prbr.graf_022(top_10_productos)

    col3, col4 = st.columns(2)

    with col3: # Top 10 productos más costosos
        top_10_costosos = filtered_df.groupby('producto')['valor_unitario'].mean().nlargest(10).reset_index()
        prup.graf_01(top_10_costosos)

    with col4: # Top 10 productos agrupados por tipo con mayores ventas

        filtered_df['producto_filtrado'] = filtered_df['producto'].str.split().str[0]
        df_productos_mas_ventas = (filtered_df.groupby('producto_filtrado')[['valor_total', 'cantidad']].sum().reset_index().sort_values(by='valor_total', ascending=False).reset_index(drop=True))
        df_top_10 = df_productos_mas_ventas.nlargest(10, 'valor_total')
        prup.graf_02(df_top_10)

    # col5, col6 = st.columns(2)

    # with col5: #Mapa de brasil ventas totales por Estado:
    # # Mapa 
    #     grouped_df = filtered_df.groupby(['abbrev_state', 'Estado'])['valor_total'].sum().reset_index()
    #     mapa.mapa_br(grouped_df)

    # with col6: # Top 10 de Venta totales neta por estado

    #     grouped_df = filtered_df.groupby(['abbrev_state', 'Estado'])['valor_total'].sum().reset_index()
    #     top_10_estados = filtered_df.groupby('Estado')['valor_total'].sum().nlargest(10).reset_index()
    #     mapa.barras(top_10_estados)
   
    # Top 10 productos más vendidos históricamente
    st.subheader("Top 10 Productos más Vendidos")
    top_10_vendidos = filtered_df.groupby('producto')['cantidad'].sum().nlargest(10).reset_index()
    fig_vendidos = px.bar(top_10_vendidos, x='producto', y='cantidad', color='cantidad',color_continuous_scale='viridis')
    fig_vendidos = layout.update_figure_layout(fig_vendidos)
    st.plotly_chart(fig_vendidos, use_container_width=True)

    # Evolución histórica de la ganancia neta
    st.subheader("Evolución Histórica de la Ganancia Neta")
    evolucion_ganancia = filtered_df.groupby('fecha_compra')['ingresos_netos'].sum().reset_index()
    fig_evolucion = px.line(evolucion_ganancia, x='fecha_compra', y='ingresos_netos', title='Evolución Histórica de la Ganancia Neta')
    fig_evolucion = layout.update_figure_layout(fig_evolucion)
    st.plotly_chart(fig_evolucion, use_container_width=True)

    # Gráfico de sol (Sunburst)
    st.subheader("Jerarquía de Ventas por Región, Marca y Producto")
    fig4 = px.sunburst(filtered_df, path=['Región', 'marca', 'producto'],
                       values='valor_total', title='Jerarquía de Ventas por Región, Marca y Producto',
                       color_discrete_sequence=['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00'])
    fig4.update_layout(title=titles_format, height=800)
    fig4 = layout.update_figure_layout(fig4)
    st.plotly_chart(fig4, use_container_width=True)

    # Mapa de árbol (Treemap)
    st.subheader("Jerarquía de Ventas por Marca y Producto")
    fig5 = px.treemap(filtered_df, path=['marca', 'producto'], values='valor_total',
                      title='Jerarquía de Ventas por Marca y Producto',color_discrete_sequence=['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00'])
    fig5.update_layout(title=titles_format, height=600)
    fig5 = layout.update_figure_layout(fig5)
    st.plotly_chart(fig5, use_container_width=True)

   # Total sales by region
    st.header("Total Sales by Region")
    fig_region = px.bar(filtered_df.groupby("Región")["valor_total"].sum().reset_index(), x="Región", y="valor_total", title="Total Sales by Region")
    st.plotly_chart(fig_region)

   # Sales by state
    st.header("Total Sales by State")
    fig_state = px.bar(filtered_df.groupby("Estado")["valor_total"].sum().reset_index(), x="Estado", y="valor_total", title="Total Sales by State")
    st.plotly_chart(fig_state)

   # Sales by condition
    st.header("Sales by Condition")
    fig_condition = px.pie(filtered_df.groupby("condicion")["valor_total"].sum().reset_index(), names="condicion", values="valor_total", title="Sales by Condition")
    st.plotly_chart(fig_condition)

   # Sales over time
    st.header("Sales Over Time")
    filtered_df["fecha_compra"] = pd.to_datetime(filtered_df["fecha_compra"])
    fig_time = px.line(filtered_df.sort_values(by="fecha_compra"), x="fecha_compra", y="valor_total", title="Sales Over Time")
    st.plotly_chart(fig_time)

    # Tabla de datos
    filtered_df['year'] = filtered_df['fecha_compra'].dt.year.astype(str)
    st.header("Datos Detallados")
    st.dataframe(filtered_df[['year', 'marca', 'producto', 'ingresos_netos']])

if __name__ == '__main__':
    main()