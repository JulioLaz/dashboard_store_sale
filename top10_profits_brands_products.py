import streamlit as st
import plotly.express as px
import plotly.colors
import update_figure_layout as layout
import pandas as pd
import colorsys
from pandas.tseries.offsets import DateOffset

height=350
titles_format = {'y':0.91, 'x': 0.5,'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 14, 'color': "#00ffff", 'family': "arial"}}

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

def graf_011(df, top_n, color_map):
    df = df.groupby('marca')['ingresos_netos'].sum().nlargest(top_n).reset_index().sort_values(by='ingresos_netos', ascending=False).reset_index(drop=True)
    fig_marcas = px.bar(df, x='marca', y='ingresos_netos', title=f'Marcas vs Ganancia Neta - Top {top_n}', color='marca', color_discrete_map=color_map)
    fig_marcas = layout.update_figure_layout(fig_marcas)
    fig_marcas.update_traces(texttemplate='$ %{y:.2s}', textposition='inside',
                             textfont=dict(family='Arial black', color='black', size=10), textangle=0)
    fig_marcas.update_layout(title=titles_format, height=height, uniformtext_minsize=8, uniformtext_mode='hide', showlegend=False)
    fig_marcas.update_yaxes(title_text='', showticklabels=False, showgrid=False)
    fig_marcas.update_xaxes(title_text='', showline=False, showticklabels=True, 
                            # tickangle=45, 
                            tickfont=dict(family='Arial', color='#ffffdf', size=10))
    st.plotly_chart(fig_marcas, use_container_width=True)

def treemap_brands_products(df, top_n, color_map):
    top_brands = df.groupby('marca')['valor_total'].sum().nlargest(top_n).index
    df_filtered = df[df['marca'].isin(top_brands)].copy()
    df_filtered['marca'] = pd.Categorical(df_filtered['marca'], categories=top_brands, ordered=True)
    df_filtered = df_filtered.sort_values('marca').reset_index(drop=True)
    
    fig5 = px.treemap(df_filtered, path=['marca', 'producto'], values='valor_total',
                      title=f'Ventas por Marca/Producto - Top {top_n}',
                      color='marca', color_discrete_map=color_map)
    
    fig5.update_layout(title=titles_format, height=height)
    fig5 = layout.update_figure_layout(fig5)
    st.plotly_chart(fig5, use_container_width=True)

def generate_soft_colors(n):
    HSV_tuples = [(x * 1.0 / n, 0.5, 0.9) for x in range(n)]
    return ['#%02x%02x%02x' % tuple(int(x*200) for x in colorsys.hsv_to_rgb(*hsv)) for hsv in HSV_tuples]

def sales_line_top(df, top_n, color_map):
    df_date = df.copy()
    top_brands = df.groupby('marca')['valor_total'].sum().nlargest(top_n).index
    df = df[df['marca'].isin(top_brands)]
    df['YearMonth'] = df['Year'].astype(str) + '-' + df['Month_num'].astype(str).str.zfill(2)
    df = df.groupby(['marca', 'YearMonth'])['valor_total'].sum().reset_index()
    df['YearMonth'] = pd.to_datetime(df['YearMonth'], format='%Y-%m')
    df = df.sort_values(by='YearMonth').reset_index(drop=True)

    min_date = df['YearMonth'].min()
    max_date = df['YearMonth'].max()

    fig = px.line(df, x='YearMonth', y='valor_total', markers=True, range_y=(0, df['valor_total'].max()),
                  color='marca', title=f'Ingresos mensuales por Marca - Top {top_n}', color_discrete_map=color_map)

    fig.update_traces(line=dict(width=.6), marker=dict(size=3))

    years = df['YearMonth'].dt.year.unique()
    year_colors = generate_soft_colors(len(years))
    year_color_map = dict(zip(years, year_colors))

    df_date['fecha_compra'] = pd.to_datetime(df_date['fecha_compra'])

    max_year = max_date.year
    for year in years:
        start_date = f"{year}-01-01"
        if year == max_year:
            end_date = max_date.strftime("%Y-%m-%d")
        else:
            end_date = f"{year}-12-31"

        fig.add_vrect(
            x0=start_date, x1=end_date,
            annotation_text=f"Year {year}",
            annotation_position="top left",
            fillcolor=year_color_map[year],
            opacity=0.3,
            line_width=0,
            annotation_font=dict(size=10, family="Arial", color="white")
        )

    fig = layout.update_figure_layout(fig)
    fig.update_layout(title=titles_format, height=height,
                      uniformtext_minsize=8, uniformtext_mode='hide',
                      xaxis=dict(
                          tickformat='%b',  # Mostrar nombre del mes
                          tickvals=pd.date_range(start=df['YearMonth'].min(), end=df['YearMonth'].max(), freq='MS'),  # Definir los ticks en cada inicio de mes
                          range=[min_date, max_date]  # Set the range for the x-axis
                      ),
                      legend=dict(
                          orientation="h",
                          yanchor="bottom",
                          y=.96,
                          xanchor="center",
                          x=0.47,
                          title=None,
                          font=dict(size=9, color='white'),
                          bgcolor='rgba(0,0,0,0)'  # Quitar el color de fondo
                      )
                      )
    fig.update_yaxes(title_text='')
    fig.update_xaxes(showline=False, title_text='', showticklabels=True,
                     tickfont=dict(family='Arial', color='white', size=8))  # Show tick every 3 months
    st.plotly_chart(fig, use_container_width=True)

def create_top_n_pie_chart(df, top_n):
    df_brands=df.groupby('marca')[['valor_total','ingresos_netos']].sum().reset_index()
    df_brands.sort_values(by='valor_total', ascending=False, inplace=True)
    df_brands.reset_index(drop=True, inplace=True)
    top_df_brands=df_brands.head(top_n)
    resto_df_brands=df_brands[top_n:]
    top_df_brands.loc[top_n] = ['resto', resto_df_brands.valor_total.sum(), resto_df_brands.ingresos_netos.sum()]
    max_index = top_df_brands['valor_total'].idxmax()

    pull_values = [0] * len(top_df_brands)
    pull_values[max_index] = 0.1  # Explode el valor más alto
    fig = px.pie(
        top_df_brands,
        names='marca',
        values='valor_total',
        title='Venta Total por Marca',
        hole=0.3,
        labels={'marca': 'Marca', 'valor_total': 'Total'},
        # color_discrete_sequence=color_map
        color_discrete_sequence=px.colors.sequential.RdBu
    )

    fig.update_traces(
        textinfo='percent+label',
        textfont_size=14,
        marker=dict(line=dict(color='gray', width=2)),
        pull=pull_values,
        # textposition='inside'
    )

    fig.update_layout(
        title=titles_format, height=height,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False  
    )
    fig.update_coloraxes(showscale=False)
    fig = layout.update_figure_layout(fig)
    st.plotly_chart(fig, use_container_width=True)          