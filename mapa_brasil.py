import plotly
import streamlit as st
import plotly.express as px
import ddbb as db
import update_figure_layout as layout

# geojson_br = db.load_geojson()
titles_format = {'x': 0.2, 'font': {'size': 28, 'color': "#00ffff", 'family': "arial"}}
viridis_palette = plotly.colors.sequential.Viridis

def generate_color_map(df, palette):
    # Normalize the `valor_total` to the range [0, 1]
    norm = (df['valor_total'] - df['valor_total'].min()) / (df['valor_total'].max() - df['valor_total'].min())
    # Map the normalized values to the color palette
    colors = [palette[int(x * (len(palette) - 1))] for x in norm]
    return colors

    # Mapa de Brasil (Choropleth)
def mapa_br(df):
    geojson_br = db.load_geojson()
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
    # return fig_mapa

def get_color_map(fig_mapa, df):
    color_map = {}
    for trace in fig_mapa['data']:
        if 'marker' in trace and 'colorscale' in trace['marker']:
            colors = trace['marker']['colorscale']
            for i, state in enumerate(df['abbrev_state']):
                color_map[state] = colors[i % len(colors)]
    return color_map

def barras(df):
    colors = generate_color_map(df, viridis_palette)
    df = df.sort_values(by='valor_total', ascending=False).head(10)
    fig = px.bar(df, x='Estado', y='valor_total', title='Top 10 Estados vs Ventas')
    fig.update_traces(marker_color=colors)
    fig = layout.update_figure_layout(fig)
    fig.update_layout(title=titles_format)
    fig.update_layout(showlegend=False)
    fig.update_traces(texttemplate='%{y:.2s}', textposition='inside',
                      textfont=dict(family='Arial black', color='black', size=14), textangle=0)
    fig.update_layout(height=500, uniformtext_minsize=8, uniformtext_mode='hide')
    fig.update_xaxes(title_text='')  # Remove x and y axis labels
    fig.update_yaxes(title_text='')  # Remove x and y axis labels
    fig.update_yaxes(showticklabels=False, showgrid=False)
    fig.update_xaxes(showline=False)  # Remove x-axis line
    fig.update_xaxes(showticklabels=True, tickangle=45, tickfont=dict(family='Arial', color='#ffffdf', size=14))
    st.plotly_chart(fig, use_container_width=True)         