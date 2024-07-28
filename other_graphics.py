    # Gráfico de sol (Sunburst)
    # st.subheader("Jerarquía de Ventas por Región, Marca y Producto")
    # fig4 = px.sunburst(filtered_df, path=['Región', 'marca', 'producto'],
    #                    values='valor_total', title='Jerarquía de Ventas por Región, Marca y Producto',
    #                    color_discrete_sequence=['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00'])
    # fig4.update_layout(title=titles_format, height=800)
    # fig4 = layout.update_figure_layout(fig4)
    # st.plotly_chart(fig4, use_container_width=True)

#    # Sales by condition
#     fig_condition = px.pie(filtered_df.groupby("condicion")["valor_total"].sum().reset_index(), names="condicion", values="valor_total", title="Sales by Condition")
#     st.plotly_chart(fig_condition)

#    # Sales over time
#     st.header("Sales Over Time")
#     filtered_df["fecha_compra"] = pd.to_datetime(filtered_df["fecha_compra"])
#     fig_time = px.line(filtered_df.sort_values(by="fecha_compra"), x="fecha_compra", y="valor_total", title="Sales Over Time")
#     st.plotly_chart(fig_time)

#     # Tabla de datos
#     filtered_df['year'] = filtered_df['fecha_compra'].dt.year.astype(str)
#     st.header("Datos Detallados")
#     st.dataframe(filtered_df[['year', 'marca', 'producto', 'ingresos_netos']])

# def sunburst_chart(df):
#     df = df.groupby(["condicion", "product_genero"])["valor_total"].sum().reset_index()
#     df['valor_total_fmt'] = df['valor_total'].apply(format_value)

#     total_sales = df['valor_total'].sum()
#     df['percent_total'] = df['valor_total'] / total_sales
    
#     fig4 = px.sunburst(df, path=['condicion', 'product_genero'],
#                       custom_data=['valor_total_fmt'],
#                       values='valor_total', title='Ventas vs Condición & Género',
#                       color_discrete_sequence=['#FF00FF', '#00FFFF', '#FFFF00', '#FF1493', '#00FF00']
#                       )

#     fig4.update_traces(
#         texttemplate='<b>%{label}</b><br>Ventas: %{customdata[0]}<br>%{percentRoot:.2%}',
#         hovertemplate='<b>%{label}</b><br>Ventas: %{customdata[0]}<br>Porcentaje: %{percentRoot:.2%}<extra></extra>')
#     fig4.update_traces(rotation=120, selector=dict(type='sunburst'))
#     fig4.update_layout(title=titles_format,
#         uniformtext=dict(minsize=10, mode='hide'),
#         margin=dict(t=0, l=0, r=0, b=0),
#     )
#     fig4 = layout.update_figure_layout(fig4)
#     st.plotly_chart(fig4, use_container_width=True)

# def format_value(value):
#     return f"${value:,.2f}"

# def enhanced_condition_treemap(df):
#     # Group by condition and product_genero, sum the total value
#     df_grouped = df.groupby(["condicion", "product_genero"])["valor_total"].sum().reset_index()
    
#     # Calculate total for each condition
#     df_condition_total = df_grouped.groupby("condicion")["valor_total"].sum().reset_index()
#     df_condition_total['valor_total_fmt'] = df_condition_total['valor_total'].apply(format_value)
    
#     # Merge the grouped data with condition totals
#     df_merged = pd.merge(df_grouped, df_condition_total, on="condicion", suffixes=('', '_condition'))
    
#     # Format values
#     df_merged['valor_total_fmt'] = df_merged['valor_total'].apply(format_value)
#     df_merged['percent_of_condition'] = df_merged['valor_total'] / df_merged['valor_total_condition']
    
#     # Create treemap
#     fig = px.treemap(df_merged,
#                      path=['condicion', 'product_genero'],
#                      values='valor_total',
#                      color='condicion',
#                      custom_data=['valor_total_fmt', 'valor_total_condition', 'percent_of_condition'],
#                      title='Ventas por Condición y Género del Producto')
    
#     # Update traces for better information display
#     fig.update_traces(
#         texttemplate='<b>%{label}</b><br>%{customdata[0]}<br>%{customdata[2]:.1%} de la condición',
#         hovertemplate='<b>%{label}</b><br>'
#                       'Venta: %{customdata[0]}<br>'
#                       'Total de la condición: ${customdata[1]:,.2f}<br>'
#                       'Porcentaje de la condición: %{customdata[2]:.2%}<extra></extra>'
#     )
    
#     # Update layout for a more professional look
#     fig.update_layout(
#         title={
#             'text': 'Ventas por Condición y Género del Producto',
#             'y':0.95,
#             'x':0.5,
#             'xanchor': 'center',
#             'yanchor': 'top',
#             'font': dict(size=24, family="Arial Black, sans-serif")
#         },
#         font=dict(family="Arial, sans-serif", size=14),
#         margin=dict(t=80, l=25, r=25, b=25),
#         height=600,
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)'
#     )
    
#     # Display the chart in Streamlit
#     st.plotly_chart(fig, use_container_width=True)

# def condition_pie(df):
#     df = df.groupby(['condicion'])['valor_total'].sum().reset_index()
#     df = df.sort_values(by='valor_total', ascending=False)
#     df['valor_total_fmt'] = df['valor_total'].apply(format_value)
#     df['percent'] = df['valor_total'] / df['valor_total'].sum() * 100

#     # Define a threshold for when to show labels outside
#     threshold = 20  # 5% threshold for outside labels

#     # Create lists for inside and outside text
#     inside_text = []
#     outside_text = []

#     for percent in df['percent']:
#         if percent < threshold:
#             inside_text.append('')
#             outside_text.append('%{label}<br>%{percent:.1%}<br>%{customdata[0]}')
#         else:
#             inside_text.append('%{label}<br>%{percent:.1%}<br>%{customdata[0]}')
#             outside_text.append('')

#     fig = go.Figure(data=[go.Pie(
#         labels=df['condicion'],
#         values=df['valor_total'],
#         hole=0.3,
#         marker_colors=['#ffff00', '#00ffff', '#ff00ff'],
#         customdata=df[['valor_total_fmt']],
#         hovertemplate='<b>%{label}</b><br>Total Vendido: %{customdata[0]}<br>Porcentaje: %{percent:.1%}<extra></extra>',
#         textfont_size=14,
#         textposition='inside',
#         texttemplate=inside_text,
#         insidetextorientation='radial'
#     )])

#     # Add outside labels
#     fig.update_traces(
#         textposition='outside',
#         texttemplate=outside_text,
#         textfont_size=12,
#     )

#     fig.update_layout(
#         title=titles_format,
#         font=dict(family="Arial Black, sans-serif", size=10),
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)',
#         showlegend=False,
#         height=450,
#         uniformtext_minsize=10,
#         uniformtext_mode='hide'
#     )

    # # Adjust margins to accommodate outside labels
    # fig.update_layout(margin=dict(l=80, r=80, t=100, b=80))

    # st.plotly_chart(fig, use_container_width=True)

 # Sales by condition
# def condition_treemap(df):
#     df= df.groupby(["condicion", "product_genero"])["valor_total"].sum().reset_index()
#     df['valor_total_fmt'] = df['valor_total'].apply(format_value)
    
#     fig = px.treemap(df, 
#                      path=['condicion','product_genero'],
#                      values='valor_total',
#                      color='condicion',
#                      custom_data=['valor_total_fmt','valor_total'],
#                      title='Ventas vs Condicion')
    
#     fig.update_traces(
#         texttemplate='<b>%{label}:</b><br>%{customdata[0]}<br>%{percentParent:.1%}',
#         hovertemplate='<b>%{label}</b><br>Venta: %{customdata[0]}<br>Porcentaje: %{percentParent:.2%}<extra></extra>'
#     )
    
#     fig.update_layout(
#         title=titles_format,
#         font=dict(family="Arial Black, sans-serif", size=13),
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)',
#         height=450,
#         margin=dict(t=50, l=25, r=25, b=25)
#     )
#     fig = layout.update_figure_layout(fig)
#     st.plotly_chart(fig, use_container_width=True)