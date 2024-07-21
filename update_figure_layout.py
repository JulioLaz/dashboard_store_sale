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