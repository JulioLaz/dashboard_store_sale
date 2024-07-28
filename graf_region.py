import streamlit as st
import plotly.express as px
import update_figure_layout as layout
import ddbb
height=350
color_map = {
    'Centro-Oeste': 'rgb(275, 204, 204)',  # Pastel red
    'Nordeste': 'rgb(204, 229, 255)',      # Pastel blue
    'Norte': 'rgb(204, 275, 214)',         # Pastel green
    'Sudeste': 'rgb(255, 255, 204)',       # Pastel yellow
    'Sul': 'rgb(235, 204, 229)'            # Pastel pink
}

color_map = {
    'Centro-Oeste': '#FF00FF',
    'Nordeste': '#00FFFF',    
    'Norte': '#FFFF00',        
    'Sudeste': '#FF1493',      
    'Sul': '#00FF00'           
}

titles_format = {'y': 0.95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top', 'font': {'size': 20, 'color': "#00ffff", 'family': "arial"}}

def region_barras(df):
    df_zona_ventas = df.groupby(['Región']).agg(valor_total=('valor_total', 'sum')).reset_index().sort_values(by='valor_total', ascending=False)
    
    fig = px.bar(df_zona_ventas, x='Región', y='valor_total',
                 title='Ventas totales por Región', labels={'Región': 'ID del Vendedor', 'valor_total': 'Ventas totales'},
                 template='plotly_white', color='Región', color_discrete_map=color_map,
                 hover_data={'Región': True, 'valor_total': ':$.2f'})

    fig.update_layout(title=titles_format, xaxis_title='', yaxis_title='', font=dict(family="Arial, sans-serif", size=14, color="white"), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                      height=height, showlegend=False, coloraxis_showscale=False)

    fig.update_traces(texttemplate='$ %{y:.2s}', textposition='inside', textfont=dict(family='Arial Black', size=14),
                      textangle=0, hovertemplate='<b>%{x}<b><br>'+'Ventas Totales: %{y:.2s}<extra></extra>')

    fig.update_xaxes(showline=False, showticklabels=True, tickangle=0, tickfont=dict(family='Arial', color='#ffffdf', size=12))
    fig.update_yaxes(showticklabels=False, showgrid=False)
    fig = layout.update_figure_layout(fig)
    st.plotly_chart(fig, use_container_width=True)

def pop_pie(df):
   df['Color'] = df['Región'].map(color_map)
   
   df_zona_pop = df[['Región', 'Population', 'Color']].drop_duplicates()
   df_zona_pop = df_zona_pop.groupby('Región').agg(Population=('Population', 'sum')).reset_index().sort_values(by='Population', ascending=False)
   
   def format_value(value):
        if value >= 1e6:
            return f'Hab {value/1e6:.1f}M'
        elif value >= 1e3:
            return f'Hab {value/1e3:.1f}K'
        else:
            return f'Hab {value:.0f}'

    # Aplicar el formato a la columna Population
   df_zona_pop['Population_fmt'] = df_zona_pop['Population'].apply(format_value)
   
   fig = px.pie(df_zona_pop, names='Región', values='Population', 
                title='Población por Región', hole=0.3,
                color='Región', color_discrete_map=color_map,
                custom_data=['Population_fmt'])
   
   fig.update_layout(title=titles_format)
   
   fig.update_traces(
        texttemplate='%{label}<br>%{customdata[0]}<br>%{percent:.1%}',
        pull=[0.03, 0, 0, 0, 0],
        textposition='inside',
        textfont_size=14,
        marker=dict(line=dict(color='black', width=2)),
        hovertemplate='<b>%{label}</b><br>Población: %{customdata[0]}<br>Porcentaje: %{percent:.1%}<extra></extra>'
    )
   
   fig.update_layout(title={'x': 0.5, 'xanchor': 'center'}, font=dict(family="Arial Black, sans-serif",
                     size=13), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', showlegend=False)
   fig.update_layout(height=height, uniformtext_minsize=12, uniformtext_mode='hide')
   fig.update_coloraxes(showscale=False)
   fig = layout.update_figure_layout(fig)
   st.plotly_chart(fig, use_container_width=True)


def pbi_pie(df):
   df['Color'] = df['Region'].map(color_map)
   
   df_zona_pbi = df[['Region', 'pbi_R$', 'Color']].drop_duplicates()
   
   def format_value(value):
        if value >= 1e3:
            return f'R$ {value/1e3:.2f}K'
        else:
            return f'R$ {value:.0f}'

    # Aplicar el formato a la columna pbi_R$
   df_zona_pbi['pbi_R$_fmt'] = df_zona_pbi['pbi_R$'].apply(format_value)
   
   fig = px.pie(df_zona_pbi, names='Region', values='pbi_R$', 
                title='PBI por Región', hole=0.3,
                color='Region', color_discrete_map=color_map,
                custom_data=['pbi_R$_fmt'])
   
   fig.update_layout(title=titles_format)
   
   fig.update_traces(
        texttemplate='%{label}<br>%{customdata[0]}<br>%{percent:.1%}',
        pull=[0.03, 0, 0, 0, 0],
        textposition='inside',
        textfont_size=14,
        marker=dict(line=dict(color='black', width=2)),
        hovertemplate='<b>%{label}</b><br>PBI: %{customdata[0]}<br>%{percent:.1%}'
    )
   
   fig.update_layout(title={'x': 0.5, 'xanchor': 'center'}, font=dict(family="Arial Black, sans-serif",
                     size=13), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', showlegend=False)
   fig.update_layout(height=height, uniformtext_minsize=12, uniformtext_mode='hide')
   fig.update_coloraxes(showscale=False)
   fig = layout.update_figure_layout(fig)
   st.plotly_chart(fig, use_container_width=True)


def mapa_br_reg(df):
    geojson_br = ddbb.load_geojson()
    grouped_df = df.groupby(['abbrev_state', 'Estado', 'Región'])['valor_total'].sum().reset_index()
    # print('Regiones: ',grouped_df)
    fig_mapa = px.choropleth(
        grouped_df,
        geojson=geojson_br,
        locations='abbrev_state',
        color='Región',
        color_discrete_map=color_map,
        featureidkey='properties.sigla',
        # title='Ventas Totales por Estado y Región',
        hover_data={'abbrev_state': False, 'Estado': True, 'valor_total': True,'Región':True}
    )
    
    fig_mapa.update_geos(
        visible=False,
        scope="south america",
        center={"lat": -14.2350, "lon": -51.9253},
        projection_scale=1.65,
        showland=False,
        showcountries=False,
        showcoastlines=False,
        showframe=False,
        showsubunits=False
    )

    fig_mapa.update_layout(
        # title=titles_format,
        height=height,
        geo=dict(
            showframe=False,
            showcoastlines=False,
            bgcolor='rgba(0,0,0,0)',
            projection_type='mercator'
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            title=None,
            font=dict(size=12, color="#FFFFFF")
        )
    )    
   
    fig_mapa.update_traces(
        marker_line_width=0,
        hovertemplate='Región: <b>%{customdata[3]}<b><br>Estado: <b>%{customdata[1]}</b><br>Ventas Totales: %{customdata[2]}<extra></extra>'
    )
    
    fig_mapa = layout.update_figure_layout(fig_mapa)
    st.plotly_chart(fig_mapa, use_container_width=True)


def pbi_treemap(df):
    color_map = {
        'Norte': '#FFFF00',
        'Nordeste': '#00FFFF',
        'Centro-Oeste': '#FF00FF',
        'Sudeste': '#FF1493',
        'Sul': '#00FF00'
    }
    
    df['Color'] = df['Region'].map(color_map)
    
    df_zona_pbi = df[['Region', 'pbi_R$', 'Color']].drop_duplicates()
    
    def format_value(value):
        if value >= 1e9:
            return f'R$ {value/1e9:.2f}B'
        elif value >= 1e6:
            return f'R$ {value/1e6:.2f}M'
        elif value >= 1e3:
            return f'R$ {value/1e3:.2f}K'
        else:
            return f'R$ {value:.0f}'
    
    df_zona_pbi['pbi_R$_fmt'] = df_zona_pbi['pbi_R$'].apply(format_value)
    
    fig = px.treemap(df_zona_pbi, 
                     path=['Region'],
                     values='pbi_R$',
                     color='Region',
                     color_discrete_map=color_map,
                     custom_data=['pbi_R$_fmt'],
                     title='PBI por Región')
    
    fig.update_traces(
        texttemplate='<b>%{label}</b><br>%{customdata[0]}<br>%{percentParent:.1%}',
        hovertemplate='<b>%{label}</b><br>PBI: %{customdata[0]}<br>Porcentaje: %{percentParent:.2%}<extra></extra>'
    )
    
    fig.update_layout(
        title=titles_format,
        # title={'text': 'PBI por Región', 'x': 0.5, 'xanchor': 'center', 'y': 0.95, 'yanchor': 'top'},
        font=dict(family="Arial Black, sans-serif", size=13),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=height,
        margin=dict(t=50, l=25, r=25, b=25)
    )
    
    fig = layout.update_figure_layout(fig)
    
    st.plotly_chart(fig, use_container_width=True)