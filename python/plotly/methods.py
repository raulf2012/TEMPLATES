import plotly.graph_objs as go


def get_layout(
    duration_long=1000 * 2,
    duration_short=800 * 2,
    ):
    """
    """
    #| - get_layout

    #| - updatemenus
    updatemenus = [
        {
            'buttons': [
                {
                    'args': [
                        None,
                        {
                            'frame': {
                                'duration': duration_long,  # TEMP_DURATION
                                'redraw': False,
                                },
                            'fromcurrent': True,
                            'transition': {
                                'duration': duration_short,  # TEMP_DURATION
                                'easing': 'quadratic-in-out',
                                }
                            }
                        ],
                    'label': 'Play',
                    'method': 'animate'
                    },
                {
                    'args': [
                        [None],
                        {
                            'frame': {
                                'duration': 0,
                                'redraw': False,
                                },
                            'mode': 'immediate',
                            'transition': {'duration': 0},
                            }
                        ],
                    'label': 'Pause',
                    'method': 'animate'
                    }
                ],
            'direction': 'left',
            'pad': {'r': 10, 't': 87},
            'showactive': False,
            'type': 'buttons',
            'x': 0.1,
            'xanchor': 'right',
            'y': 0,
            'yanchor': 'top'
            }
        ]

    #__|

    layout = go.Layout(
        # title='Material Discovery Training',
        showlegend=False,
        font=dict(
            # family='Courier New, monospace',

            family='Arial',
            size=20,
            color='black'
            ),

        xaxis={
            'title': 'Candidate Structures',

            # 'range': [0 - 5, len(models_list[0]) + 5],
            # 'autorange': False,
            'autorange': True,

            'showgrid': False,
            'zeroline': False,
            'showline': True,
            'ticks': '',
            'showticklabels': True,
            'mirror': True,
            'linecolor': 'black',

            },

        yaxis={
            'title': 'Formation Energy (eV)',

            # 'range': [global_y_min, global_y_max],
            # 'range': [-1.5, 2.4],
            # 'autorange': False,
            'autorange': True,
            'fixedrange': False,

            'showgrid': False,
            'zeroline': True,
            'showline': True,
            'ticks': '',
            'showticklabels': True,
            'mirror': True,
            'linecolor': 'black',

            },

        updatemenus=updatemenus,
        )

    return(layout)
    #__|

    
def get_sliders_init_dict(duration_short):
    """
    """
    # | - get_sliders_init_dict
    sliders_dict = {
        # 'active': 0,
        'active': 0,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 20},
            'prefix': 'Loop #:',
            'visible': True,
            'xanchor': 'right'
            },
        'transition': {
            'duration': duration_short,  # TEMP_DURATION
            'easing': 'cubic-in-out'},
        'pad': {'b': 10, 't': 50},
        'len': 0.8,
        'x': 0.1,
        'y': 0,
        'steps': [],
        }

    return(sliders_dict)
    #__|

def get_slider_step_i(i_cnt, duration_short):
    """
    """
    #| - get_slider_step_i
    slider_step_i = {
        'args': [
            [str(i_cnt)],
            {
                'frame': {
                    'duration': duration_short,  # TEMP_DURATION
                    'redraw': False},
                'mode': 'immediate',
                'transition': {
                    'duration': duration_short,  # TEMP_DURATION
                    },
                },
            ],
        'label': str(i_cnt),
        'method': 'animate',
        }

    return(slider_step_i)
    #__|

# TEMP