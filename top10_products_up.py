import streamlit as st
import plotly.express as px
import update_figure_layout as layout
import plotly.express as px

titles_format = {'y':0.95, 'x': 0.5,'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 20, 'color': "#00ffff", 'family': "arial"}}

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

def graf_01(df):
         fig = px.bar(df, x='producto', y='valor_unitario', title='Top 10 Productos más Costosos')
         fig.update_traces(marker_color=colors_3)
         fig = layout.update_figure_layout(fig)
         fig.update_layout(title=titles_format)
         fig.update_layout(showlegend=False)
         fig.update_traces(texttemplate='%{y:.2s}', textposition='inside',
                              textfont=dict(family='Arial black', color='black', size=14), textangle=0)
         fig.update_layout(height=500,uniformtext_minsize=8, uniformtext_mode='hide')
         fig.update_xaxes(title_text='')  # Remove x and y axis labels
         fig.update_yaxes(title_text='')  # Remove x and y axis labels
         fig.update_yaxes(showticklabels=False, showgrid=False)
         fig.update_xaxes(showline=False)  # Remove x-axis line
         fig.update_xaxes(showticklabels=True, tickangle=45, tickfont=dict(family='Arial', color='#ffffdf', size=12))
         st.plotly_chart(fig, use_container_width=True)

def graf_02(df):
         fig = px.bar(df, x='producto_filtrado', y='valor_total', title='Top 10 Tipo de poductos con mayores ventas')
         fig.update_traces(marker_color=colors_2)
         fig = layout.update_figure_layout(fig)
         fig.update_layout(title=titles_format)
         fig.update_layout(showlegend=False)
         fig.update_traces(texttemplate='%{y:.2s}', textposition='inside',
                              textfont=dict(family='Arial black', color='black', size=14), textangle=0)
         fig.update_layout(height=500,uniformtext_minsize=8, uniformtext_mode='hide')
         fig.update_xaxes(title_text='')  # Remove x and y axis labels
         fig.update_yaxes(title_text='')  # Remove x and y axis labels
         fig.update_yaxes(showticklabels=False, showgrid=False)
         fig.update_xaxes(showline=False)  # Remove x-axis line
         fig.update_xaxes(showticklabels=True, tickangle=45, tickfont=dict(family='Arial', color='#ffffdf', size=12))         
         st.plotly_chart(fig, use_container_width=True)