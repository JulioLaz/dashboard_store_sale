import streamlit as st
import plotly.express as px
import plotly.colors
import update_figure_layout as layout


titles_format = {'y':0.95, 'x': 0.5,'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 20, 'color': "#00ffff", 'family': "arial"}}

viridis_palette = plotly.colors.sequential.Plotly3_r
inferno_palette = px.colors.sequential.Inferno
blue_palette = px.colors.sequential.Blues
green_palette = px.colors.sequential.Greens
magma_palette = px.colors.sequential.Magma
Peach_palette = px.colors.sequential.Peach
Mint_palette = px.colors.sequential.Mint
Tealgrn_palette = px.colors.sequential.Tealgrn
Purpor_palette = px.colors.sequential.Purpor
Sunset_palette = px.colors.sequential.Sunset
Emrld_palette = px.colors.sequential.Emrld

peach=['rgb(253, 224, 197)','rgb(251, 211, 184)','rgb(249, 198, 171)','rgb(247, 185, 158)','rgb(246, 172, 145)','rgb(245, 165, 135)','rgb(244, 162, 128)','rgb(244, 160, 121)','rgb(244, 159, 117)','rgb(245, 158, 114)']
pera=['rgb(211, 242, 163)','rgb(196, 232, 159)','rgb(181, 222, 155)','rgb(166, 212, 151)','rgb(151, 202, 148)','rgb(136, 192, 144)','rgb(121, 182, 140)','rgb(106, 172, 136)','rgb(91, 162, 133)','rgb(76, 155, 130)']

colors_1 = []
for i in range(10):
    r = int(253 - i * 10)
    g = int(224 - i * 9.67)
    b = int(197 - i * 3.67)
    colors_1.append(f'rgb({r}, {g}, {b})')

colors_2 = []
for i in range(10):
    r = int(211 - i * 15)
    g = int(242 - i * 9.67)
    b = int(163 - i * 3.67)
    colors_2.append(f'rgb({r}, {g}, {b})')

def graf_011(df):
         # colors = [viridis_palette[i] for i in range(len(df))]
         fig_marcas = px.bar(df, x='marca', y='ingresos_netos', title='Top 10 Marcas según Ganancia Neta')
         fig_marcas.update_traces(marker_color=peach)
         fig_marcas = layout.update_figure_layout(fig_marcas)
         fig_marcas.update_layout(title=titles_format)
         fig_marcas.update_layout(showlegend=False)
         fig_marcas.update_traces(texttemplate='$ %{y:.2s}', textposition='inside',
                              textfont=dict(family='Arial black', color='black', size=12), textangle=0)
         fig_marcas.update_layout(height=500,uniformtext_minsize=8, uniformtext_mode='hide')
         fig_marcas.update_xaxes(title_text='')  # Remove x and y axis labels
         fig_marcas.update_yaxes(title_text='')  # Remove x and y axis labels
         fig_marcas.update_yaxes(showticklabels=False, showgrid=False)
         fig_marcas.update_xaxes(showline=False)  # Remove x-axis line
         fig_marcas.update_xaxes(showticklabels=True, tickangle=45, tickfont=dict(family='Arial', color='#ffffdf', size=14))
         st.plotly_chart(fig_marcas, use_container_width=True)
         pass

def graf_022(df,top_n):
         df = df.groupby('producto')['ingresos_netos'].sum().nlargest(top_n).reset_index()
         fig_productos = px.bar(df, x='producto', y='ingresos_netos', title=f'Top {top_n} Productos según Ganancia Neta')
         fig_productos.update_traces(marker_color=pera)
         fig_productos = layout.update_figure_layout(fig_productos)
         fig_productos.update_layout(title=titles_format)
         fig_productos.update_layout(showlegend=False)
         fig_productos.update_traces(texttemplate='$ %{y:.2s}', textposition='inside',
                              textfont=dict(family='Arial black', color='black', size=12), textangle=0)
         fig_productos.update_layout(height=500,uniformtext_minsize=8, uniformtext_mode='hide')
         fig_productos.update_xaxes(title_text='')  # Remove x and y axis labels
         fig_productos.update_yaxes(title_text='')  # Remove x and y axis labels
         fig_productos.update_yaxes(showticklabels=False, showgrid=False)
         fig_productos.update_xaxes(showline=False)  # Remove x-axis line
         fig_productos.update_xaxes(showticklabels=True, tickangle=45, tickfont=dict(family='Arial', color='#ffffdf', size=14))         
         st.plotly_chart(fig_productos, use_container_width=True)
         pass