import streamlit as st
import plotly.express as px
import update_figure_layout as layout
height=350
titles_format = {'y':0.91, 'x': 0.5,'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 16, 'color': "#00ffff", 'family': "arial"}}

def sales_line(df):
         df = df.groupby(['Year', 'Month', 'Month_num'])['valor_total'].sum().reset_index()
         df = df.sort_values(by=['Year', 'Month_num'], ascending=[True, True]).reset_index(drop=True)
         fig = px.line(df, x='Month', y='valor_total', markers=True, range_y=(0, df['valor_total'].max()), color='Year', line_dash='Year', title='Ingresos mensuales')
         fig = layout.update_figure_layout(fig)
         fig.update_layout(title=titles_format,height=height,uniformtext_minsize=8, uniformtext_mode='hide',        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=0.85,
            xanchor="center",
            x=0.45,
            title=None,
            font=dict(size=10, color="#FFFFFF"),
                            bgcolor='rgba(0,0,0,0)'  # Quitar el color de fondo

        ))
         fig.update_yaxes(title_text='')
         fig.update_xaxes(showline=False,title_text='',showticklabels=True,
                        #    tickangle=45,
                             tickfont=dict(family='Arial', color='white', size=10))
         st.plotly_chart(fig, use_container_width=True)

def sales_pie(df):
    def format_value(value):
        if value >= 1e6:
            return f'${value/1e6:.1f}M'
        elif value >= 1e3:
            return f'${value/1e3:.1f}K'
        else:
            return f'${value:.0f}'
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
        texttemplate='<b>%{label}</b><br>%{customdata[0]}<br>%{percent:.1%}',
        # textposition='inside',
        textfont_size=10,
        rotation=72,
        marker=dict(line=dict(color='black', width=2)),
        pull=[0.03,0,0],
        hovertemplate='<b>%{label}</b><br>Total Vendido: %{customdata[0]}<br>Porcentaje: %{percent:.1%}<extra></extra>'
    )

    fig.update_layout(
        title=titles_format,
        # font=dict(family="Arial Black, sans-serif", size=14, color="white"),
        font=dict(family="Arial"),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        height=height,
        uniformtext_minsize=10, 
        uniformtext_mode='hide'
    )
    fig.update_coloraxes(showscale=False)
    fig = layout.update_figure_layout(fig)
    st.plotly_chart(fig, use_container_width=True)

def condition_pie(df):
    titles_format = {'y':0.95, 'x': 0.5,'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 16, 'color': "#00ffff", 'family': "arial"}}

    def format_value(value):
        if value >= 1e6:
            return f'${value/1e6:.1f}M'
        elif value >= 1e3:
            return f'${value/1e3:.1f}K'
        else:
            return f'${value:.0f}'
    df = df.groupby(['condicion'])['valor_total'].sum().reset_index()
    df = df.sort_values(by=['condicion'], ascending=[True]).reset_index(drop=True)

    df = df.sort_values(by='valor_total', ascending=False)
    df['valor_total_fmt'] = df['valor_total'].apply(format_value)

    fig = px.pie(df, 
                 names='condicion', 
                 values='valor_total',
                 title='Ventas vs Condición', 
                 hole=0.3,
                 color_discrete_sequence=['#505050','#00ffff','#ff00ff'],
                 custom_data=['valor_total_fmt'])  # Pasamos los valores formateados como custom_data

    fig.update_traces(
        texttemplate='%{label}<br>%{percent:.1%}<br>%{customdata[0]}',
        # textfont_size=12,
        textfont=dict(size=10, color='white'),  # Red color and size 10 for outside labels
        marker=dict(line=dict(color='black', width=2)),
        pull=[0.01,0,0],
        # rotation=10,
        rotation=65,
        hovertemplate='<b>%{label}</b><br>Total Vendido: %{customdata[0]}<br>Porcentaje: %{percent:.1%}<extra></extra>',
        # textposition='outside',
        # insidetextorientation='radial'
    )

    fig.update_layout(
        title=titles_format,
        font=dict(family="Arial, sans-serif"),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        height=height,
        # uniformtext_minsize=12, 
        # uniformtext_mode='hide'
    )
    fig.update_coloraxes(showscale=False)
    fig = layout.update_figure_layout(fig)
    st.plotly_chart(fig, use_container_width=True)    

def genre_pie(df):
    titles_format = {'y':0.95, 'x': 0.5,'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 16, 'color': "#00ffff", 'family': "arial"}}

    def format_value(value):
        if value >= 1e6:
            return f'${value/1e6:.1f}M'
        elif value >= 1e3:
            return f'${value/1e3:.1f}K'
        else:
            return f'${value:.0f}'
    df = df.groupby(['product_genero'])['valor_total'].sum().reset_index()
    df = df.sort_values(by=['product_genero'], ascending=[True]).reset_index(drop=True)

    df = df.sort_values(by='valor_total', ascending=False)
    df['valor_total_fmt'] = df['valor_total'].apply(format_value)

    fig = px.pie(df, 
                 names='product_genero', 
                 values='valor_total',
                 title='Sales vs Genre', 
                 hole=0.3,
                 color_discrete_sequence=['#505050','#00ffff','#ff00ff'],
                 custom_data=['valor_total_fmt'])  # Pasamos los valores formateados como custom_data

    fig.update_traces(
        texttemplate='%{label}<br>%{percent:.1%}<br>%{customdata[0]}',
        # textfont_size=12,
        textfont=dict(size=10, color='white'),  # Red color and size 10 for outside labels
        marker=dict(line=dict(color='black', width=2)),
        pull=[0.01,0,0],
        # rotation=10,
        rotation=65,
        hovertemplate='<b>%{label}</b><br>Total Vendido: %{customdata[0]}<br>Porcentaje: %{percent:.1%}<extra></extra>',
        # textposition='outside',
        # insidetextorientation='radial'
    )

    fig.update_layout(
        title=titles_format,
        font=dict(family="Arial, sans-serif"),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        height=height,
        # uniformtext_minsize=12, 
        # uniformtext_mode='hide'
    )
    fig.update_coloraxes(showscale=False)
    fig = layout.update_figure_layout(fig)
    st.plotly_chart(fig, use_container_width=True)    