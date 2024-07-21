import streamlit as st
import requests
import pandas as pd

@st.cache_data(ttl=600)
def load_data():
    file_id = '1bbfb6a71RI7a2F7vv_SzhtKkN8QyugJf'
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    df = pd.read_csv(url)
    df['fecha_compra'] = pd.to_datetime(df['fecha_compra'])
    return df
# print(load_data())

@st.cache_data(ttl=600)
def load_geojson():
   file_id = '161Y6BbBVNAnKhSosPetTBSWx-cmP4FYs'
   url = f'https://drive.google.com/uc?export=download&id={file_id}'
   response = requests.get(url)
   brazil_states_geojson = response.json()
   return brazil_states_geojson

# def load_geojson():
#    with open('brazil-states.geojson', 'r', encoding='utf-8') as f:
#         return json.load(f)
# print(load_geojson())