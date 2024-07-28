import streamlit as st
import plotly.express as px
import update_figure_layout as layout
import pandas as pd
import colorsys
import statsmodels.api as sm
height=350
titles_format = {'y': 0.95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 20, 'color': "#00ffff", 'family': "arial"}}

def generate_soft_colors(n):
    HSV_tuples = [(x * 1.0 / n, 0.5, 0.9) for x in range(n)]
    return ['#%02x%02x%02x' % tuple(int(x*255) for x in colorsys.hsv_to_rgb(*hsv)) for hsv in HSV_tuples]


def profit_evol(df):       
    evolucion_ganancia = df.groupby('fecha_compra')['ingresos_netos'].sum().reset_index()
    fig = px.line(evolucion_ganancia, x='fecha_compra', y='ingresos_netos', title='Evolución Histórica de la Ganancia Neta')

    years = df['fecha_compra'].dt.year.unique()
    year_colors = generate_soft_colors(len(years))
    year_color_map = dict(zip(years, year_colors))

    df['fecha_compra'] = pd.to_datetime(df['fecha_compra'])
    max_date = df['fecha_compra'].max() + pd.Timedelta(weeks=1)
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
            opacity=0.2,
            line_width=0,
            annotation_font=dict(size=12, family="Arial Black", color="white")
        )

        # Agregar línea de tendencia
        year_df = evolucion_ganancia[evolucion_ganancia['fecha_compra'].dt.year == year]
        if len(year_df) > 1:  # Para evitar problemas con años con muy pocos datos
            X = sm.add_constant(year_df.index)
            y = year_df['ingresos_netos']
            model = sm.OLS(y, X).fit()
            trend = model.predict(X)

            fig.add_traces(
                px.scatter(year_df, x='fecha_compra', y=trend, trendline="ols", trendline_color_override='red').data[1]
            #     px.scatter(year_df, x='fecha_compra', y=trend, trendline="ols", trendline_color_override=year_color_map[year]).data[1]
            )
            
    fig = layout.update_figure_layout(fig)
    fig.update_traces(line=dict(width=.9), marker=dict(size=3))
#     fig.update_traces(line=dict(width=.8, color='red'), marker=dict(size=3))
    fig.update_layout(
        title=titles_format,
        height=height,
        uniformtext_minsize=8, 
        uniformtext_mode='hide',
        xaxis=dict(
            tickformat='%b',  # Mostrar nombre del mes
            tickvals=pd.date_range(start=df['fecha_compra'].min(), end=df['fecha_compra'].max(), freq='MS'),  # Definir los ticks en cada inicio de mes
            # showgrid=True,
            # gridcolor='gray',
            # gridwidth=0.1,
            # griddash='dash'
        )
    )
    fig.update_yaxes(title_text='')
    fig.update_xaxes(showline=True, title_text='', showticklabels=True, tickangle=0, tickfont=dict(family='Arial', color='white', size=12))
    st.plotly_chart(fig, use_container_width=True)
