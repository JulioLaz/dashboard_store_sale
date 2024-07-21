import requests
import streamlit as st

@st.cache_data(ttl=600)
def load_data_geo():
   file_id = '161Y6BbBVNAnKhSosPetTBSWx-cmP4FYs'
   url = f'https://drive.google.com/uc?export=download&id={file_id}'
   response = requests.get(url)
   brazil_states_geojson = response.json()
   return brazil_states_geojson