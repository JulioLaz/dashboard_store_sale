import streamlit as st
import plotly.express as px
import ddbb as db
import update_figure_layout as layout

geojson_br = db.load_geojson()
titles_format = {'x': 0.2, 'font': {'size': 28, 'color': "#00ffff", 'family': "arial"}}

def update_figure_layout(fig):
    fig.update_layout(
        plot_bgcolor='#1E1E1E',
        paper_bgcolor='#1E1E1E',
        font=dict(size=12, color='#00FF00'),  # Verde fluorescente
        margin=dict(l=40, r=40, t=60, b=40)
    )
    fig.update_xaxes(gridcolor='#333333', zerolinecolor='#333333')
    fig.update_yaxes(gridcolor='#333333', zerolinecolor='#333333')
    return fig

def mapa_br(df):
    # Mapa de Brasil (Choropleth)
    grouped_df = df.groupby(['abbrev_state', 'Estado'])['valor_total'].sum().reset_index()
    fig_mapa = px.choropleth(
        grouped_df,
        geojson=geojson_br,
        locations='abbrev_state',
        color='valor_total',
        color_continuous_scale='viridis',
        featureidkey='properties.sigla',
        title='Ventas Totales por Estado',
        range_color=[grouped_df['valor_total'].min(), grouped_df['valor_total'].max()],
        hover_data={'abbrev_state': False, 'Estado': True}
    )
    fig_mapa.update_geos(
        visible=False,
        scope="south america",
        center={"lat": -14.2350, "lon": -51.9253},
        projection_scale=1.7,
        showland=False,
        showcountries=False,
        showcoastlines=False,
        showframe=False,
        showsubunits=False
    )
    fig_mapa.update_layout(
        title=titles_format,
        height=700,
        coloraxis_showscale=False,
        geo=dict(
            showframe=False,
            showcoastlines=False,
            bgcolor='rgba(0,0,0,0)',
            projection_type='mercator'
        )
    )
    fig_mapa.update_traces(
        marker_line_width=0,
        hovertemplate='<b>%{customdata[1]}</b><br>Ventas Totales: %{z}<extra></extra>'
    )
    fig_mapa = layout.update_figure_layout(fig_mapa)
    st.plotly_chart(fig_mapa, use_container_width=True)