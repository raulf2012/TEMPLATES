# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.7
#   kernelspec:
#     display_name: Python [conda env:research-new]
#     language: python
#     name: conda-env-research-new-py
# ---

# # Import Modules

# +
import os
import sys

import pandas as pd

import plotly.graph_objs as go

# #############################################################################
from methods import get_sliders_init_dict, get_slider_step_i, get_layout
# -

# # Script Inputs

duration_long = 1000 * 3
duration_short = 800 * 3

# # Read Data

# +
df_data = pd.read_csv("data.csv", header=[0, 1])

time_series_indices = list(df_data.columns.levels[0])

df_list = []
for i in time_series_indices:
    df_i = df_data[i]
    df_i = df_i.set_index("name")
    # df_i = df_i.sort_index()
    df_list.append(df_i)


# -

# # methods | get_traces

def get_traces(df):
    trace = go.Scatter(
        x=df["x"],
        y=df["y"],
        mode="markers",
        marker=dict(
            symbol="circle",
            color=df["color"],
            size=18),
        )
    data = [trace]

    return(data)


# +
layout_anim = get_layout(
    duration_long=duration_long,
    duration_short=duration_short)
sliders_dict = get_sliders_init_dict(duration_short)

frames = []; data = []
for i_cnt, df_i in enumerate(df_list):
    traces_i = get_traces(df_i)

    # #################################################################
    if i_cnt == 0: data.extend(traces_i)
    data_i = []; data_i.extend(traces_i)
    frame_i = go.Frame(data=data_i, name=str(i_cnt))
    frames.append(frame_i)
    slider_step_i = get_slider_step_i(i_cnt, duration_short)
    sliders_dict['steps'].append(slider_step_i)

# +
layout_anim["showlegend"] = True

fig = go.Figure(
    data=data,
    layout=layout_anim,
    frames=frames)
fig['layout']['sliders'] = [sliders_dict]

fig.show()
