import streamlit as st
import plotly.express as px
import update_figure_layout as layout
height=350
peach = ['rgb(253, 224, 197)', 'rgb(251, 211, 184)', 'rgb(249, 198, 171)', 'rgb(247, 185, 158)', 'rgb(246, 172, 145)',
         'rgb(245, 165, 135)', 'rgb(244, 162, 128)', 'rgb(244, 160, 121)', 'rgb(244, 159, 117)', 'rgb(245, 158, 114)']
titles_format = {'y': 0.95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top', 'font': {
    'size': 20, 'color': "#00ffff", 'family': "arial"}}

color_map = {
    'Centro-Oeste': 'rgb(275, 204, 204)',  # Pastel red
    'Nordeste': 'rgb(204, 229, 255)',      # Pastel blue
    'Norte': 'rgb(204, 275, 214)',         # Pastel green
    'Sudeste': 'rgb(255, 255, 204)',       # Pastel yellow
    'Sul': 'rgb(235, 204, 229)'          # Pastel pink
}

def seller(df):
    colors = ['#272cc2', '#aeeafc', '#e6a3a3'] * df.nombre_vendedor.nunique()
    df_ingresos_vendedor = df.groupby(['nombre_vendedor', 'Year']).agg(valor_total=('valor_total', 'sum')).reset_index()
   #  print(df_ingresos_vendedor)
    fig = px.bar(df_ingresos_vendedor,x='nombre_vendedor',y='valor_total',color='Year',
                 title='Ventas totales por Vendedor por Año',labels={'nombre_vendedor': 'ID del Vendedor','valor_total': 'Ventas totales', 'Year': 'Año'},
                 template='plotly_white', color_discrete_sequence=colors[:df.Year.nunique()],
                 hover_data={'Year': True, 'valor_total': ':$.2f'})

    fig.update_layout(title=titles_format,xaxis_title='',yaxis_title='',font=dict(family="Arial, sans-serif", size=14, color="white"),plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)',
                      height=height,showlegend=False,coloraxis_showscale=False)

    fig.update_traces(texttemplate='$ %{y:.2s}',textposition='inside',textfont=dict(family='Arial Black', size=14),
        textangle=0,hovertemplate='<b>%{x}</b><br>'+'Año: %{customdata[0]}<br>'+'Ventas Totales: %{y:.2s}<extra></extra>',
                      marker_color=colors )

    fig.update_xaxes(showline=False,
        showticklabels=True,tickangle=0,tickfont=dict(family='Arial', color='#ffffdf', size=12)
    )

    fig.update_yaxes(showticklabels=False, showgrid=False)
    fig = layout.update_figure_layout(fig)
    st.plotly_chart(fig, use_container_width=True)

color_seller=['#A2FEFD','#F2A2FE','#A2FEFD','#F2A2FE','#F2A2FE']

def seller_pie(df):
    df_vendedores = df.groupby('nombre_vendedor').sum('valor_total').reset_index()[['nombre_vendedor', 'valor_total']].sort_values(by='valor_total', ascending=False)
    # colors = px.colors.sequential.Blues
    colors = color_seller

    def format_value(value):
        if value >= 1e6:
            return f'${value/1e6:.1f}M'
        elif value >= 1e3:
            return f'${value/1e3:.1f}K'
        else:
            return f'${value:.0f}'

    # Aplicar el formato a la columna total_vendido
    df_vendedores['total_vendido_fmt'] = df_vendedores['valor_total'].apply(format_value)

    fig = px.pie(df_vendedores,
                 values='valor_total',
                 names='nombre_vendedor',
                 title='Distribución de Total ventas por Vendedor',
                 color_discrete_sequence=colors,
                 hole=.3,
                 hover_data={'valor_total': ':$.2f'})

    fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center'},
        font=dict(family="Arial Black, sans-serif", size=14),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=height,
        legend_title_text='ID del Vendedor',
        showlegend=False

    )
    fig.update_layout(title=titles_format)

    fig.update_traces(
        pull=[0.03,0,0,0,0,0],
        textposition='inside',
        texttemplate='%{label}<br>%{percent:.2%}<br>%{customdata[0]}',
        textfont_size=14,
        marker=dict(line=dict(color='black', width=2)),
        customdata=df_vendedores[['total_vendido_fmt']],
        hovertemplate='<b>%{label}</b><br>Total Vendido: %{customdata[0]}<br>Porcentaje: %{percent:.1%}<extra></extra>'
    )

    fig = layout.update_figure_layout(fig)
    st.plotly_chart(fig, use_container_width=True)

# def seller_pie00(df):
#     df_vendedores = df.groupby('nombre_vendedor').agg(total_vendido=('valor_total', lambda x: (x * df.loc[x.index, 'cantidad']).sum()),cantidad_vendida=('cantidad', 'sum')).sort_values(by='total_vendido', ascending=False).reset_index()  
#     colors = px.colors.sequential.Blues
#    #  colors = px.colors.sequential.Inferno

#     fig = px.pie(df_vendedores, 
#                  values='total_vendido', 
#                  names='nombre_vendedor',
#                  title='Distribución de Ingresos Netos por Vendedor',
#                  color_discrete_sequence=colors,hole=.3,
#                  hover_data={'total_vendido': ':$.2f'})

#     fig.update_layout(
#       #   textinfo='percent+label',
#         title=titles_format,
#         font=dict(family="Arial Black, sans-serif", size=14),
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)',
#         height=450,
#         legend_title_text='ID del Vendedor',
#         showlegend=False
#     )

#     fig.update_traces(pull=[0.03,0,0,0,0,0],
#         textposition='inside',
#         textinfo='percent+label+value',
#         textfont_size=14,
#         textfont_color='black',
#         hovertemplate='<b>%{label}</b><br>Ingresos Netos: %{customdata[0]}<br>Porcentaje: %{percent:.1f}%<extra></extra>'
#     )
#     fig = layout.update_figure_layout(fig)
#     st.plotly_chart(fig, use_container_width=True)

# def sales_pie(df):
#    df=df.sort_values(by='valor_total', ascending=False)
#    fig = px.pie(df, names='Year', values='valor_total', title='Distribución de Total Vendido por Año', hole=0.3,
#       labels={'Años': 'Year', 'Total': 'valor_total'}, color_discrete_sequence=['#272cc2','#aeeafc','#e6a3a3'])
#    fig.update_layout(title=titles_format)
#    fig.update_traces( textinfo='percent+label', textfont_size=14, marker=dict(line=dict(color='black', width=1)), pull=[0.03,0,0],)
#    fig.update_layout(title={'x': 0.5, 'xanchor': 'center'},font=dict(family="Arial, sans-serif", size=14, color="white"),plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)',showlegend=False)
#    fig.update_layout(height=450,uniformtext_minsize=12, uniformtext_mode='hide')
#    fig.update_coloraxes(showscale=False)
#    fig = layout.update_figure_layout(fig)
#    st.plotly_chart(fig, use_container_width=True)