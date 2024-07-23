def update_figure_layout(fig):
    fig.update_layout(
        plot_bgcolor='black',
        # plot_bgcolor='#1E1E1E',
        paper_bgcolor='black',
        font=dict(size=12, color='#00FF00'),  # Verde fluorescente
        margin=dict(l=20, r=20, t=60, b=20)
        
    )
    # fig.update_xaxes(gridcolor='white', zerolinecolor='white')
    # fig.update_yaxes(gridcolor='white', zerolinecolor='white')
    fig.update_xaxes(gridcolor='#333333', zerolinecolor='#333333')
    fig.update_yaxes(gridcolor='#333333', zerolinecolor='#333333')
    return fig