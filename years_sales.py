import streamlit as st
import plotly.express as px
import update_figure_layout as layout

def format_value(value):
        if value >= 1e6:
            return f'${value/1e6:.1f}M'
        elif value >= 1e3:
            return f'${value/1e3:.1f}K'
        else:
            return f'${value:.0f}'

titles_format = {'y':0.95, 'x': 0.5,'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 20, 'color': "#00ffff", 'family': "arial"}}

def sales_line(df):
         df = df.groupby(['Year', 'Month', 'Month_num'])['valor_total'].sum().reset_index()
         df = df.sort_values(by=['Year', 'Month_num'], ascending=[True, True]).reset_index(drop=True)
         fig = px.line(df, x='Month', y='valor_total', markers=True, range_y=(0, df['valor_total'].max()), color='Year', line_dash='Year', title='Ingresos mensuales')
         fig = layout.update_figure_layout(fig)
         fig.update_layout(title=titles_format,height=450,uniformtext_minsize=8, uniformtext_mode='hide')
         fig.update_yaxes(title_text='')
         fig.update_xaxes(showline=False,title_text='',showticklabels=True, tickangle=45, tickfont=dict(family='Arial', color='white', size=12))
         st.plotly_chart(fig, use_container_width=True)

def sales_pie(df):
    df = df.groupby(['Year'])['valor_total'].sum().reset_index()
    df = df.sort_values(by=['Year'], ascending=[True]).reset_index(drop=True)

    df = df.sort_values(by='valor_total', ascending=False)
    df['valor_total_fmt'] = df['valor_total'].apply(format_value)

    fig = px.pie(df, 
                 names='Year', 
                 values='valor_total',
                 title='Ventas por Año', 
                 hole=0.3,
                 color_discrete_sequence=['#272cc2','#aeeafc','#e6a3a3'],
                 custom_data=['valor_total_fmt'])  # Pasamos los valores formateados como custom_data

    fig.update_traces(
        texttemplate='%{label}<br>%{percent:.1%}<br>%{customdata[0]}',
        textposition='inside',
        textfont_size=14,
        marker=dict(line=dict(color='black', width=2)),
        pull=[0.03,0,0],
        hovertemplate='<b>%{label}</b><br>Total Vendido: %{customdata[0]}<br>Porcentaje: %{percent:.1%}<extra></extra>'
    )

    fig.update_layout(
        title=titles_format,
        font=dict(family="Arial Black, sans-serif", size=14, color="white"),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        height=450,
        uniformtext_minsize=12, 
        uniformtext_mode='hide'
    )

    fig.update_coloraxes(showscale=False)
    
    fig = layout.update_figure_layout(fig)
    
    st.plotly_chart(fig, use_container_width=True)


   # Sales by condition
def condition_treemap(df):
    df= df.groupby(["condicion", "product_genero"])["valor_total"].sum().reset_index()
    df['valor_total_fmt'] = df['valor_total'].apply(format_value)
    
    fig = px.treemap(df, 
                     path=['condicion','product_genero'],
                     values='valor_total',
                     color='condicion',
                     custom_data=['valor_total_fmt','valor_total'],
                     title='Ventas vs Condicion')
    
    fig.update_traces(
        texttemplate='<b>%{label}:</b><br>%{customdata[0]}<br>%{percentParent:.1%}',
        hovertemplate='<b>%{label}</b><br>Venta: %{customdata[0]}<br>Porcentaje: %{percentParent:.2%}<extra></extra>'
    )
    
    fig.update_layout(
        title=titles_format,
        font=dict(family="Arial Black, sans-serif", size=13),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=450,
        margin=dict(t=50, l=25, r=25, b=25)
    )
    fig = layout.update_figure_layout(fig)
    st.plotly_chart(fig, use_container_width=True)


def sunburst_chart(df):
    df = df.groupby(["condicion", "product_genero"])["valor_total"].sum().reset_index()
    df['valor_total_fmt'] = df['valor_total'].apply(format_value)

    total_sales = df['valor_total'].sum()
    df['percent_total'] = df['valor_total'] / total_sales
    
    fig4 = px.sunburst(df, path=['condicion', 'product_genero'],
                      custom_data=['valor_total_fmt'],
                      values='valor_total', title='Ventas vs Condición & Género',
                      color_discrete_sequence=['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00']
                      )

    fig4.update_traces(
        texttemplate='<b>%{label}</b><br>Ventas: %{customdata[0]}<br>%{percentRoot:.2%}',
        hovertemplate='<b>%{label}</b><br>Ventas: %{customdata[0]}<br>Porcentaje: %{percentRoot:.2%}<extra></extra>')
    fig4.update_traces(rotation=120, selector=dict(type='sunburst'))
    fig4.update_layout(title=titles_format,
        uniformtext=dict(minsize=10, mode='hide'),
        margin=dict(t=0, l=0, r=0, b=0),
    )
    fig4 = layout.update_figure_layout(fig4)
    st.plotly_chart(fig4, use_container_width=True)