import streamlit as st
import plotly.express as px
import update_figure_layout as layout
height=350
titles_format = {'y':0.95, 'x': 0.5,'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 16, 'color': "#00ffff", 'family': "arial"}}

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

colors_3 = [] #rgb(253, 211, 203)
for i in range(10):
    r = int(253 - i * 15)
    g = int(211 - i * 9.67)
    b = int(203 - i * 3.67)
    colors_3.append(f'rgb({r}, {g}, {b})')

# Top 10 Productos más Costosos
def graf_01(df,top_n):
         df = df.groupby('producto')['valor_unitario'].mean().nlargest(top_n).reset_index()
         fig = px.bar(df, x='producto', y='valor_unitario', title=f'Productos más Costosos - Top {top_n}')
         fig.update_traces(marker_color=colors_3)
         fig = layout.update_figure_layout(fig)
         fig.update_layout(title=titles_format)
         fig.update_layout(showlegend=False)
         fig.update_traces(texttemplate='$ %{y:.2s}', textposition='inside',
                              textfont=dict(family='Arial black', color='black', size=12), textangle=0)
         fig.update_layout(height=height,uniformtext_minsize=8, uniformtext_mode='hide')
         fig.update_xaxes(title_text='')  # Remove x and y axis labels
         fig.update_yaxes(title_text='')  # Remove x and y axis labels
         fig.update_yaxes(showticklabels=False, showgrid=False)
         fig.update_xaxes(showline=False)  # Remove x-axis line
         fig.update_xaxes(showticklabels=True, tickangle=45, tickfont=dict(family='Arial', color='#ffffdf', size=12))
         st.plotly_chart(fig, use_container_width=True)

# Top 10 Tipo de poductos con mayores ventas
def graf_02(df,top_n):
         df['producto_filtrado'] = df['producto'].str.split().str[0]
         df = (df.groupby('producto_filtrado')[['valor_total', 'cantidad']].sum().reset_index().sort_values(by='valor_total', ascending=False).reset_index(drop=True))
         df = df.nlargest(top_n, 'valor_total')
         fig = px.bar(df, x='producto_filtrado', y='valor_total', title=f'Tipo de poductos con mayores ventas - Top {top_n}')
         fig = layout.update_figure_layout(fig)
         fig.update_traces(showlegend=False,marker_color=colors_2,texttemplate='$ %{y:.2s}', textposition='inside',
                              textfont=dict(family='Arial black', color='black', size=12), textangle=0)
         fig.update_layout(title=titles_format,height=height,uniformtext_minsize=8, uniformtext_mode='hide')
         fig.update_yaxes(title_text='',showticklabels=False, showgrid=False)
         fig.update_xaxes(title_text='',showline=False,showticklabels=True, tickangle=45, tickfont=dict(family='Arial', color='#ffffdf', size=12))         
         st.plotly_chart(fig, use_container_width=True) 

    # Top 10 productos más vendidos históricamente
def graf_03(df,top_n):
        df = df.groupby('producto')['cantidad'].sum().nlargest(top_n).reset_index()
        fig = px.bar(df, x='producto', y='cantidad',title=f'Productos más vendidos - Top {top_n}')
        fig = layout.update_figure_layout(fig)
        fig.update_layout(title=titles_format,showlegend=False,height=height,uniformtext_minsize=8, uniformtext_mode='hide')
        fig.update_traces(marker_color=colors_3,texttemplate='%{y} u', textposition='inside',
                              textfont=dict(family='Arial black', color='black', size=12), textangle=0)
        fig.update_yaxes(title_text='',showticklabels=False, showgrid=False)
        fig.update_xaxes(title_text='',showline=False,showticklabels=True, tickangle=45, tickfont=dict(family='Arial', color='#ffffdf', size=12))         
        st.plotly_chart(fig, use_container_width=True)

def graf_022(df,top_n):
         df = df.groupby('producto')['ingresos_netos'].sum().nlargest(top_n).reset_index()
         fig_productos = px.bar(df, x='producto', y='ingresos_netos', title=f'Productos según Ganancia Neta - Top {top_n}')
         fig_productos = layout.update_figure_layout(fig_productos)

         fig_productos.update_traces(marker_color=pera,texttemplate='$ %{y:.2s}', textposition='inside',
                              textfont=dict(family='Arial black', color='black', size=12), textangle=0)
         fig_productos.update_layout(title=titles_format,height=height,uniformtext_minsize=8, uniformtext_mode='hide',showlegend=False)
         fig_productos.update_yaxes(title_text='',showticklabels=False, showgrid=False)
         fig_productos.update_xaxes(title_text='',showline=False,showticklabels=True, tickangle=45, tickfont=dict(family='Arial', color='#ffffdf', size=14))
         st.plotly_chart(fig_productos, use_container_width=True)
         pass              