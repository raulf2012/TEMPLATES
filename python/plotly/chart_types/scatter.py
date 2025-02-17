
#| - Fuller scatter plot instantiation
import chart_studio.plotly as py
import plotly.graph_objs as go

#  import os

x_array = [0, 1, 2, 3]
y_array = [0, 1, 2, 3]


trace = go.Scatter(
    x=x_array,
    y=y_array,
    mode="markers",
    opacity=0.8,
    marker=dict(

        symbol="circle",
        color='LightSkyBlue',

        opacity=0.8,

        # color=z,
        colorscale='Viridis',
        colorbar=dict(thickness=20),

        size=20,
        line=dict(
            color='MediumPurple',
            width=2
            )
        ),

    line=dict(
        color="firebrick",
        width=2,
        dash="dot",
        ),

    error_y={
        "type": 'data',
        "array": [0.4, 0.9, 0.3, 1.1],
        "visible": True,
        },

    )

data = [trace]

fig = go.Figure(data=data)
fig.show()
#__|

#| - Simple Plotly Plot

import plotly.graph_objs as go

x_array = [0, 1, 2, 3]
y_array = [0, 1, 2, 3]

trace = go.Scatter(
    mode="markers",
    x=x_array,
    y=y_array,
    )
data = [trace]

fig = go.Figure(data=data)
fig.show()

#__|


# <--------------------------------------------------------
# <--------------------------------------------------------
# <--------------------------------------------------------
# <--------------------------------------------------------
# <--------------------------------------------------------
# <--------------------------------------------------------




#| - 2022-11-09 | Better one, incorporates base property objects (applies my default stylings)
# Input your  figure objects here
# layout = fig_0.layout  # <-----------------


import plotly.graph_objs as go
import copy

from plotting.my_plotly import base_plotly_layout, base_plotly_scatter_props, shared_axis_dict, shared_axis_dict__bigger
shared_axis_dict = shared_axis_dict__bigger

from plotting.my_plotly import my_plotly_plot





my_ploty_plot_input = dict(
    place_in_out_plot=True,
    write_html=True,
    verbose=False,
    )

base_plotly_layout['showlegend'] = True

shared_xaxis_dict = copy.deepcopy(shared_axis_dict)
shared_yaxis_dict = copy.deepcopy(shared_axis_dict)


data = []

trace = go.Scatter(base_plotly_scatter_props).update(
    mode='markers',
    x=df_2.PC_z_ave__BEC,
    y=df_2.dipole__0__BEC,
    )
data.append(trace)

# ---------------------------------------------------------

layout = go.Layout(base_plotly_layout)

layout.update(
    showlegend=False,
    )

layout.xaxis.update(shared_xaxis_dict)
layout.xaxis.update(
    title_text='TEMP X',
    # range=[0, 10]
    )

layout.yaxis.update(shared_yaxis_dict)
layout.yaxis.update(
    title_text='TEMP Y',
    )

fig = go.Figure(data=data, layout=layout)
fig.show()


# Writting to the plot to file
if False:
    from plotting.my_plotly import my_plotly_plot
    my_plotly_plot(
        figure=fig,
        plot_name='TEMP_PLOT_NAME',
        **my_ploty_plot_input,
        )

#__|
