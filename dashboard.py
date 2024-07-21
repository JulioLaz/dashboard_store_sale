import streamlit as st
import pandas as pd
import plotly.express as px
import ddbb as db
import navbar as nb
import top10_profits_brands_products as prbr
import top10_products_up as prup
import mapa_brasil as mapa
import update_figure_layout as layout

def formata_numero(valor, prefijo=''):
    for unidad in ['', 'k']:
        if valor < 1000:
            return f'{prefijo} {valor:.2f} {unidad}'
        valor /= 1000
    return f'{prefijo} {valor:.2f} M'

st.set_page_config(page_title="Ventas ecommerce Brazil", page_icon=":shopping_bags:", layout="wide")

titles_format = dict(font=dict(size=18, color='#1f77b4'), xref='paper', x=0.5, y=0.95, xanchor='center', yanchor='top')


st.markdown(
    """
   <link href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" rel="stylesheet">
   <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">

    <style>
    .stApp {
        background-color: #1E1E1E;
        color: #00FF00;
    }
    header{
    background-color: rgba(0,0,0,0) !important;
    }
        .navbar-custom {
            top: 0rem !important; 
            position: fixed !important;
            width: calc(100% - 0px) !important;
            right: 0px !important; 
            z-index: 1000 !important;
            background-color: black !important; 
        }
        #navbarNav{
        margin: 2.3rem 2rem 0 0 !important;
            display: flex;
            justify-content: flex-end;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def create_navbar():
    st.markdown("""
<nav class="navbar navbar-expand-lg navbar-dark bg-dark navbar-custom">
  <a class="navbar-brand" href="#" style="font-size: 40px; font-family: Arial; color: #00ffff; margin-left: 2.5rem">🛍️ Análisis de Ventas</a>
  <div class="collapse navbar-collapse" id="navbarNav" >
    <ul class="navbar-nav margenes">
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/JulioLaz" target="_blank">
          <i class="fab fa-github me-2 fa-lg"></i></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.linkedin.com/in/julio-lazarte-developer/" target="_blank">
          <i class="fab fa-linkedin me-2 fa-lg"></i></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://cv-lazarte-julio.web.app/" target="_blank">
          <i class="fas fa-globe me-2 fa-lg"></i></a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)  

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: rgba(0,0,0,0);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ocultar label del ratioitens:
hide_element_style = '''
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(9) > div > label {
        display: none
        }
'''

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
    st.sidebar.header("Filtros")
    nb.create_navbar()
    nb.create_navbar()

    years = ["ALL"] + sorted(df['fecha_compra'].dt.year.unique())

    if 'year_filter_mode' not in st.session_state:
       st.session_state.year_filter_mode = True

    if st.session_state.year_filter_mode:
      selected_year = st.sidebar.radio("", options=years[:], index=0, key="year_radio", horizontal=True)
      if selected_year == "ALL":
         years_filter = df['fecha_compra'].dt.year.unique()
      else:
         years_filter = [selected_year]
    else:
      years_filter = df['fecha_compra'].dt.year.unique()

    # Filtros de selección múltiple con opción "ALL"
    marca_filter = create_multiselect_filter(df, 'marca', "Marca")
    producto_filter = create_multiselect_filter(df, 'producto', "Producto")
    ciudad_filter = create_multiselect_filter(df, 'Estado', "Estado")
    Región_filter = create_multiselect_filter(df, 'Región', "Región")
    vendedor_filter = create_multiselect_filter(df, 'nombre_vendedor', "Vendedor")
    marca_genero_filter = create_multiselect_filter(df, 'marca_genero', "Género")

# CSS personalizado
    st.markdown("""
    <style>
    [data-testid="stWidgetLabel"]{
         color: #ff00ff !important;
         font-size: 10px !important;
         font-weight: 400 !important;
         display: flex;
         justify-content: right !important;
        }        
    [role="radiogroup"] {
           display: flex !important;
           justify-content: center !important;
      }
    .st-cc {
         font-size: 12px !important;
         font-weight: 500 !important;
      }
    [data-testid="stRadio"] label:has(input:checked) {
      color: white !important;
      background-color: rgba(200,200,200,.3) !important;
      padding: .4rem .8rem !important;
      border: 1px solid white !important;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(2) > div > div > label:nth-child(1) > div.st-ba.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by > div > p{
    color: white !important;
                    }                
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(2) > div > div > label:nth-child(2) > div.st-ba.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by > div > p{
    color: white !important;
                    }                
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(2) > div > div > label:nth-child(3) > div.st-ba.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by > div > p{
    color: white !important;
                    }                
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(2) > div > div > label:nth-child(4) > div.st-ba.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by > div > p{
    color: white !important;
                }                


 
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(2) > div > label > div > p{
                font-size: 20px;
                font-weight: bold;
                color: yellow;
                    }
                
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > label > div > p{
                font-size: 20px;
                font-weight: bold;
                color: yellow;
                    }

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > label > div > p{
                font-size: 20px;
                font-weight: bold;
                color: yellow;
                    }

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > label > div > p{
            font-size: 20px;
            font-weight: bold;
            color: yellow;
                }
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > label > div > p{
            font-size: 20px;
            font-weight: bold;
            color: yellow;
                }

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > label > div > p{
            font-size: 20px;
            font-weight: bold;
            color: yellow;
                }

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > label > div > p{
            font-size: 20px;
            font-weight: bold;
            color: yellow;
                }

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > label > div > p{
            font-size: 20px;
            font-weight: bold;
            color: yellow;
                }


#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(1) > div > div > h2{
   font-size: 2rem;
   font-weight: 600;
   color: aqua !important;
   margin: 1rem !important;                
                }

               
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > div > div{
            background-color: rgba(0,0,0,0) !important;                }

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
            color: white !important}               

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
            color: #00ffff !important;                }                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
            color: white !important;                }                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(3) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
            background-color: rgba(200,200,200,0.3) !important;                }                
               

                
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > div > div > div{
            background-color: rgba(0,0,0,0) !important;                }

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
            color: white !important}               }                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
            color: #00ffff !important;                }                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
            color: white !important;                }                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(4) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
            background-color: rgba(200,200,200,0.3) !important;                }                
               
                
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > div > div > div{
            background-color: rgba(0,0,0,0) !important;                }

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
            color: white !important}                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
            color: #00ffff !important;                }                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
            color: white !important;                }                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(5) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
            background-color: rgba(200,200,200,0.3) !important;                }                
               
                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > div > div > div{
            background-color: rgba(0,0,0,0) !important;}

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
            color: white !important}                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
            color: #00ffff !important;
                    }                

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
            color: white !important;
                    }                

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(6) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
         background-color: rgba(200,200,200,0.3) !important;
                }                
               
                
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > div > div > div{
         background-color: rgba(0,0,0,0) !important;
                }

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
         color: white !important}                

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
         color: #00ffff !important;
                }                

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
         color: white !important;
                }                

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(7) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
         background-color: rgba(200,200,200,0.3) !important;
                }                
                
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > div > div > div{
         background-color: rgba(0,0,0,0) !important;}

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > div.st-eg.st-dm.st-c9.st-db.st-da.st-eh{
         color: white !important}

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > div > div > div > div.st-ak.st-al.st-as.st-da.st-bg.st-db.st-dc > svg{
         color: #00ffff !important;}                

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > div > div > div > div.st-ak.st-al.st-bd.st-be.st-bf.st-as.st-bg.st-bh.st-ar.st-bi.st-bj.st-bk.st-bl > div.st-eg.st-cn.st-ar.st-ca.st-c9.st-eh{
         color: white !important;}                

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1gv3huu.eczjsme18 > div.st-emotion-cache-6qob1r.eczjsme11 > div.st-emotion-cache-1gwvy71.eczjsme12 > div > div > div > div > div:nth-child(8) > div > div > div > div > div.st-c3.st-bx.st-cq.st-cr.st-cs.st-ae.st-ah.st-af.st-c9.st-bk.st-bm.st-ct.st-bl > span{
         background-color: rgba(200,200,200,0.3) !important;}                
               
#root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(1),
#root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(2),
#root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(3),
#root > div:nth-child(1) .st-emotion-cache-ocqkz7 > div:nth-child(4) {
    border: 1px solid #00ff00;
    border-radius: 5px;
    padding: 10px;
}
                       
                
/* Hide specific label */
#root > div:nth-child(1) .st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(n+1):nth-child(-n+4) > div > div > div > div:nth-child(2) > div > label {
    display: none;
}

/* Hide  */
#root > div:nth-child(1) .st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(n+1):nth-child(-n+5),
#root > div:nth-child(1) .st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(8) {
    display: none;
}



                #root > div:nth-child(2) > div > div > div > div > div > div > ul > div{
                background-color: darkgray;
                }

      </style>
   """, unsafe_allow_html=True)

    mask = (
        (df['nombre_vendedor'].isin(vendedor_filter)) &
        (df['Estado'].isin(ciudad_filter)) &
        (df['marca'].isin(marca_filter)) &
        (df['producto'].isin(producto_filter)) &
        (df['Región'].isin(Región_filter)) &
        (df['marca_genero'].isin(marca_genero_filter)) &
        (df['fecha_compra'].dt.year.isin(years_filter))
    )
    filtered_df = df[mask]

    st.markdown("""
        <style>
        .metric-title {
            font-size: 14px; /* Cambia el tamaño del título */
            color: #00FF00; /* Cambia el color del título */
            # border: 1px solid white;
        }
        </style>
        """, unsafe_allow_html=True)

    #### Métricas principales
    col1, col2, col3, col4 = st.columns(4)

    col1.markdown(f"<div class='metric-title'>Total de Ventas</div>", unsafe_allow_html=True)
    col1.metric("Total de Ventas", formata_numero(filtered_df['valor_total'].sum(),'$'),label_visibility="hidden")

    col2.markdown(f"<div class='metric-title'>Número de Pedidos</div>", unsafe_allow_html=True)
    col2.metric("", f"{filtered_df['pedido_id'].nunique():,}")

    col3.markdown(f"<div class='metric-title'>Ganancia Neta</div>", unsafe_allow_html=True)
    col3.metric("", formata_numero(filtered_df['ingresos_netos'].sum(),'$'))

    col4.markdown(f"<div class='metric-title'>Productos Únicos</div>", unsafe_allow_html=True)
    col4.metric("", f"{filtered_df['producto'].nunique():,}")

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

    # Mapa 
    grouped_df = filtered_df.groupby(['abbrev_state', 'Estado'])['valor_total'].sum().reset_index()
    mapa.mapa_br(grouped_df)

    # Top 10 de ganancia neta por estado
    st.subheader("Top 10 Estados según Ganancia Neta")
    top_10_estados = filtered_df.groupby('Estado')['ingresos_netos'].sum().nlargest(10).reset_index()
    fig_estados = px.bar(top_10_estados, x='Estado', y='ingresos_netos', title='Top 10 Estados según Ganancia Neta')
    fig_estados = layout.update_figure_layout(fig_estados)
    st.plotly_chart(fig_estados, use_container_width=True)

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


# fig4 = px.sunburst(filtered_df, path=['Región', 'marca', 'producto'],
                  #  values='valor_total', title='Jerarquía de Ventas por Región, Marca y Producto',
                  #  color_discrete_sequence=['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00'])

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