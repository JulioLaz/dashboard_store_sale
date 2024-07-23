import streamlit as st
import requests
import pandas as pd
import clasifica_gen as clge

@st.cache_data(ttl=600)
def generar_dataframe():

    global df_itens_pedidos, df_pedidos, df_productos, df_vendedores,df_population, df_final

    df_itens_pedidos = pd.read_csv('https://raw.githubusercontent.com/ElProfeAlejo/Bootcamp_Databases/main/itens_pedidos.csv')
    df_itens_pedidos.rename(columns={'ciudad': 'ISO_3166_2'},inplace=True)
    df_pedidos = pd.read_csv('https://raw.githubusercontent.com/ElProfeAlejo/Bootcamp_Databases/main/pedidos.csv')
    df_productos = pd.read_csv('https://raw.githubusercontent.com/ElProfeAlejo/Bootcamp_Databases/main/productos.csv')
    df_vendedores = pd.read_csv('https://raw.githubusercontent.com/ElProfeAlejo/Bootcamp_Databases/main/vendedores.csv')

    #POPULATION
    file_id = '1HDZH0m1OMJplUg2JZrJ4slzIpuVGTxM8'
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    df_population = pd.read_csv(url)

    def preprocesamiento():
        global df_itens_pedidos, df_pedidos, df_productos, df_vendedores, df_population

        # Eliminar registros con valores nulos en columnas primary o foreign key
        df_itens_pedidos.dropna(subset=['pedido_id', 'producto_id'], inplace=True)
        df_pedidos.dropna(subset=['pedido_id', 'producto_id', 'vendedor_id'], inplace=True)
        df_productos.dropna(subset=['producto_id','producto'], inplace=True)### Elimino también los NaN de producto
        df_vendedores.dropna(subset=['vendedor_id'], inplace=True)

        #eliminar la fila con Vendedor='Unknown':
        df_vendedores = df_vendedores[df_vendedores['nombre_vendedor'] != 'Unknown']

        # Eliminar registros duplicados
        df_itens_pedidos.drop_duplicates(inplace=True)
        df_pedidos.drop_duplicates(inplace=True)
        df_productos.drop_duplicates(inplace=True)
        df_vendedores.drop_duplicates(inplace=True)

        # Asegurar tipos de datos correctos:
        df_itens_pedidos['id_recibo'] = df_itens_pedidos['id_recibo'].astype('int32')
        df_itens_pedidos['producto_id'] = df_itens_pedidos['producto_id'].astype('int32')
        df_itens_pedidos['pedido_id'] = df_itens_pedidos['pedido_id'].astype('int32')
        df_itens_pedidos['ISO_3166_2'] = df_itens_pedidos['ISO_3166_2'].astype(str)
        df_itens_pedidos['costo_envio'] = df_itens_pedidos['costo_envio'].astype('int32')

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

        return df_itens_pedidos, df_pedidos, df_productos, df_vendedores, df_population

    df_itens_pedidos, df_pedidos, df_productos, df_vendedores, df_population = preprocesamiento()

    #Fusionar dfs:
    df_final = (
        df_itens_pedidos.merge(df_pedidos, on='pedido_id')
                .drop(columns=['producto_id_y'])
                .rename(columns={'producto_id_x': 'producto_id'})
                .merge(df_productos, on='producto_id')
                .merge(df_vendedores, on='vendedor_id')
                .merge(df_population, on='ISO_3166_2')
    )
    columns=['total','precio','sku']
    df_final.drop(columns=columns,inplace=True)
    df_final['ingresos_netos'] = df_final['valor_total'] - df_final['costo_envio']
    df_final['tipo_producto'] = df_final['producto'].str.split().str[0]
    df_final.drop_duplicates(inplace=True)
    df_final.dropna(inplace=True)
    df_final.valor_total.sum()
    return df_final

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
        # print(df_final)
        print(df_all.info())
        return df_all
# @st.cache_data(ttl=600)
# def load_data():
#     file_id = '1bbfb6a71RI7a2F7vv_SzhtKkN8QyugJf'
#     url = f'https://drive.google.com/uc?export=download&id={file_id}'
#     df = pd.read_csv(url)
#     df['fecha_compra'] = pd.to_datetime(df['fecha_compra'])
#     return df
# print(load_data())

@st.cache_data(ttl=600)
def load_geojson():
   file_id = '161Y6BbBVNAnKhSosPetTBSWx-cmP4FYs'
   url = f'https://drive.google.com/uc?export=download&id={file_id}'
   response = requests.get(url)
   brazil_states_geojson = response.json()
   return brazil_states_geojson
