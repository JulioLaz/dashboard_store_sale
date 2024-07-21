import streamlit as st
import plotly.express as px
import plotly.colors
import dashboard as main
import plotly.express as px
# print(px.colors.named_colorscales())
# "Top 10 Marcas según Ganancia Neta"
tiltes_format = {'x': 0.2, 'font': {'size': 28, 'color': "#00ffff", 'family': "arial"}}
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

peach=['rgb(253, 224, 197)','rgb(251, 211, 184)','rgb(249, 198, 171)','rgb(247, 185, 158)','rgb(246, 172, 145)','rgb(245, 165, 135)','rgb(244, 162, 128)','rgb(244, 160, 121)','rgb(244, 159, 117)','rgb(245, 158, 114)']
pera=['rgb(211, 242, 163)','rgb(196, 232, 159)','rgb(181, 222, 155)','rgb(166, 212, 151)','rgb(151, 202, 148)','rgb(136, 192, 144)','rgb(121, 182, 140)','rgb(106, 172, 136)','rgb(91, 162, 133)','rgb(76, 155, 130)']

print('Emrld_palette: ', Emrld_palette)


colors_1 = []
for i in range(10):
    r = int(253 - i * 15)
    g = int(224 - i * 9.67)
    b = int(197 - i * 3.67)
    colors_1.append(f'rgb({r}, {g}, {b})')
colors_1

colors_2 = []
for i in range(10):
    r = int(211 - i * 15)
    g = int(242 - i * 9.67)
    b = int(163 - i * 3.67)
    colors_2.append(f'rgb({r}, {g}, {b})')
colors_2
