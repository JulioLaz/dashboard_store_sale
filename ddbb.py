import streamlit as st
import requests
import pandas as pd
import clasifica_gen as clge

@st.cache_data(ttl=600)
def generar_dataframe():

    global df_items_pedidos, df_pedidos, df_productos, df_vendedores,df_population, df_final

    df_items_pedidos = pd.read_csv('https://raw.githubusercontent.com/ElProfeAlejo/Bootcamp_Databases/main/itens_pedidos.csv')
    df_items_pedidos.rename(columns={'ciudad': 'ISO_3166_2'},inplace=True)
    df_pedidos = pd.read_csv('https://raw.githubusercontent.com/ElProfeAlejo/Bootcamp_Databases/main/pedidos.csv')
    df_productos = pd.read_csv('https://raw.githubusercontent.com/ElProfeAlejo/Bootcamp_Databases/main/productos.csv')
    df_vendedores = pd.read_csv('https://raw.githubusercontent.com/ElProfeAlejo/Bootcamp_Databases/main/vendedores.csv')

    #POPULATION
    file_id = '1HDZH0m1OMJplUg2JZrJ4slzIpuVGTxM8'
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    df_population = pd.read_csv(url)

    def preprocesamiento():
        global df_items_pedidos, df_pedidos, df_productos, df_vendedores, df_population

        # Eliminar registros con valores nulos en columnas primary o foreign key
        df_items_pedidos.dropna(subset=['pedido_id', 'producto_id'], inplace=True)
        df_pedidos.dropna(subset=['pedido_id', 'producto_id', 'vendedor_id'], inplace=True)
        df_productos.dropna(subset=['producto_id','producto'], inplace=True)### Elimino también los NaN de producto
        df_vendedores.dropna(subset=['vendedor_id'], inplace=True)

        #eliminar la fila con Vendedor='Unknown':
        df_vendedores = df_vendedores[df_vendedores['nombre_vendedor'] != 'Unknown']

        # Eliminar registros duplicados
        df_items_pedidos.drop_duplicates(inplace=True)
        df_pedidos.drop_duplicates(inplace=True)
        df_productos.drop_duplicates(inplace=True)
        df_vendedores.drop_duplicates(inplace=True)

        # Asegurar tipos de datos correctos:
        df_items_pedidos['id_recibo'] = df_items_pedidos['id_recibo'].astype('int32')
        df_items_pedidos['producto_id'] = df_items_pedidos['producto_id'].astype('int32')
        df_items_pedidos['pedido_id'] = df_items_pedidos['pedido_id'].astype('int32')
        df_items_pedidos['ISO_3166_2'] = df_items_pedidos['ISO_3166_2'].astype(str)
        df_items_pedidos['costo_envio'] = df_items_pedidos['costo_envio'].astype('int32')

        df_pedidos['pedido_id'] = df_pedidos['pedido_id'].astype('int32')
        df_pedidos['producto_id'] = df_pedidos['producto_id'].astype('int32')
        df_pedidos['vendedor_id'] = df_pedidos['vendedor_id'].astype('int8')
        df_pedidos['fecha_compra'] = pd.to_datetime(df_pedidos['fecha_compra'])

        df_productos['producto_id'] = df_productos['producto_id'].astype('int32')
        df_productos['precio'] = df_productos['precio'].astype(float)
        df_productos['sku'] = df_productos['sku'].astype(str)

        df_vendedores['vendedor_id'] = df_vendedores['vendedor_id'].astype('int8')
        df_vendedores['nombre_vendedor'] = df_vendedores['nombre_vendedor'].astype(str)

        df_population['Population'] = df_population['Population'].astype(int)
        df_population['Area_km2'] = df_population['Area_km2'].astype('int32')
        df_population['Density_pers_km2'] = df_population['Density_pers_km2'].astype('uint16')

        return df_items_pedidos, df_pedidos, df_productos, df_vendedores, df_population

    df_items_pedidos, df_pedidos, df_productos, df_vendedores, df_population = preprocesamiento()

    #Fusionar dfs:
    df_final = (
        df_items_pedidos.merge(df_pedidos, on='pedido_id')
                .drop(columns=['producto_id_y'])
                .rename(columns={'producto_id_x': 'producto_id'})
                .merge(df_productos, on='producto_id')
                .merge(df_vendedores, on='vendedor_id')
                .merge(df_population, on='ISO_3166_2')
    )
    columns=['total','precio','sku','producto_id','id_recibo', 'Capital','Area_km2', 'Density_pers_km2']
    df_final.drop(columns=columns,inplace=True)
    df_final['ingresos_netos'] = df_final['valor_total'] - df_final['costo_envio']
    df_final['tipo_producto'] = df_final['producto'].str.split().str[0]
    df_final.drop_duplicates(inplace=True)
    df_final.dropna(inplace=True)
    df_final.valor_total.sum()
    return df_final
# print('#'*70)
# print('columnas :', generar_dataframe().columns)
# print('#'*70)
### Clasifica genero: ###
@st.cache_data(ttl=600)
def load_data():
        df_marca_genero=clge.marca_gen()
        clasificando_productos_unisex=clge.dict_prod_gen()
        df_final = generar_dataframe().copy()
        df_all = pd.merge(df_final, df_marca_genero, on='marca', how='inner')
        df_all['product_genero']=df_all['marca_genero']
        df_all['product_genero'] = df_all.apply(lambda row: clasificando_productos_unisex.get(row['producto'], row['product_genero']),axis=1)
        df_all['fecha_compra'] = pd.to_datetime(df_all['fecha_compra'])
        df_all['Year'] = df_all['fecha_compra'].dt.year
        df_all['Month'] = df_all['fecha_compra'].dt.month_name()
        df_all['Month_num'] = df_all['fecha_compra'].dt.month
        return df_all

### PBI & Pop for State
@st.cache_data(ttl=600)
def load_pop_pbi_state():
    url = "https://es.wikipedia.org/wiki/Anexo:Estados_de_Brasil_por_PIB_per_c%C3%A1pita_(nominal)"
    tablas = pd.read_html(url)
    tabla = tablas[0]
    df_data_brasil=pd.DataFrame(tabla)

    PBI=df_data_brasil['PIB per cápita']
    poblacion=df_data_brasil['Referencia (2023)']
    region=df_data_brasil['Región']

    df_data_brasil_pbi_pop_state = pd.concat([region,PBI,poblacion],axis=1)
    columns=['Región', 'BRL', 'Población']
    df_data_brasil_pbi_pop_state= df_data_brasil_pbi_pop_state[columns].copy()
    df_data_brasil_pbi_pop_state.rename(columns={'BRL': 'pbi_R$','Región': 'Estado','Población':'Poblacion'}, inplace=True)
    df_data_brasil_pbi_pop_state=df_data_brasil_pbi_pop_state.sort_values(by='Estado', ascending=True).reset_index(drop=True)
    df_data_brasil_pbi_pop_state=df_data_brasil_pbi_pop_state[df_data_brasil_pbi_pop_state['Estado']!='Brasil']
    df_data_brasil_pbi_pop_state['Poblacion'] = (df_data_brasil_pbi_pop_state['Poblacion'].str.replace('.', '')).astype('uint32')
    df_data_brasil_pbi_pop_state['pbi_R$'] = (df_data_brasil_pbi_pop_state['pbi_R$']*1000).astype('uint32')
    return df_data_brasil_pbi_pop_state

@st.cache_data(ttl=600)
def load_pop_pbi_region():
    url = "https://es.wikipedia.org/wiki/Anexo:Estados_de_Brasil_por_PIB_per_c%C3%A1pita_(nominal)"
    tablas = pd.read_html(url)
    tabla_region = tablas[1]
    df_data_brasil_region=pd.DataFrame(tabla_region)
    PBI_reg=df_data_brasil_region['PIB per cápita']
    poblacion_reg=df_data_brasil_region['Referencia (2023)']
    region_reg=df_data_brasil_region['Región']
    df_data_brasil_pbi_pop_region = pd.concat([region_reg,PBI_reg,poblacion_reg],axis=1)
    df_data_brasil_pbi_pop_region=df_data_brasil_pbi_pop_region[df_data_brasil_pbi_pop_region['Región']!='Brasil']
    columns=['Región', 'BRL', 'Población']
    df_data_brasil_pbi_pop_region= df_data_brasil_pbi_pop_region[columns].copy()
    df_data_brasil_pbi_pop_region.rename(columns={'BRL': 'pbi_R$','Región': 'Region','Población':'Poblacion'}, inplace=True)
    df_data_brasil_pbi_pop_region['Poblacion'] = (df_data_brasil_pbi_pop_region['Poblacion'].str.replace('.', '')).astype('uint32')
    df_data_brasil_pbi_pop_region['pbi_R$'] = (df_data_brasil_pbi_pop_region['pbi_R$']*1000).astype('uint32')
    return df_data_brasil_pbi_pop_region

@st.cache_data(ttl=600)
def load_geojson():
   file_id = '161Y6BbBVNAnKhSosPetTBSWx-cmP4FYs'
   url = f'https://drive.google.com/uc?export=download&id={file_id}'
   response = requests.get(url)
   brazil_states_geojson = response.json()
   return brazil_states_geojson
