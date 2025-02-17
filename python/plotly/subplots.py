import plotly.graph_objs as go
from plotly.subplots import make_subplots




# #########################################################
l_tmp = 0.
spec_d0 = dict(l=l_tmp, b=0.)
spec_d1 = dict()
spec_d2 = dict()
spec_d3 = dict()
spec_d4 = dict()

# #########################################################
l_tmp = 0.
t_tmp = -0.001
spec_00 = dict(l=l_tmp, t=t_tmp)
spec_01 = dict(t=t_tmp)
spec_02 = dict(t=t_tmp)
spec_03 = dict(t=t_tmp)
spec_04 = dict(t=t_tmp)

# #########################################################
# l_tmp = 0.033
l_tmp = 0.025
t_tmp = 0.0025
# spec_10 = dict(l=0.025, r=0., t=t_tmp, b=0.)
spec_10 = dict(l=0.03, r=0., t=t_tmp, b=0.)
spec_11 = dict(l=l_tmp, r=0., t=t_tmp, b=0.)
spec_12 = dict(l=l_tmp, r=0., t=t_tmp, b=0.)

# spec_13 = dict(l=0.044, r=0., t=t_tmp, b=0.)
spec_13 = dict(l=0.03, r=0., t=t_tmp, b=0.)
spec_14 = dict(l=0.03, r=0., t=t_tmp, b=0.)

# #########################################################
spec_20 = dict()
spec_21 = dict()
spec_22 = dict()
# spec_23 = dict(rowspan=1, colspan=2, l=0.2, t=0.1)
# spec_23 = dict(rowspan=1, colspan=2, l=0.2, t=0.15)
spec_23 = dict(rowspan=1, colspan=2, l=0.2, t=0.13)
spec_24 = None

# #########################################################
spec_dtmp = dict(rowspan=1)
# spec_0tmp = dict(rowspan=3)
spec_0tmp = None
spec_1tmp = None
spec_2tmp = None
dx_tmp = 0.11
dx_d6 = dx_tmp / 6
fig = make_subplots(
    rows=4, cols=6,
    specs=[
        [spec_dtmp, spec_d0, spec_d1, spec_d2, spec_d3, spec_d4],
        [spec_0tmp, spec_00, spec_01, spec_02, spec_03, spec_04],
        [spec_1tmp, spec_10, spec_11, spec_12, spec_13, spec_14],
        [spec_2tmp, spec_20, spec_21, spec_22, spec_23, spec_24],
        ],
    print_grid=False,
    shared_yaxes=False,
    horizontal_spacing=0.015,
    vertical_spacing=0.,
    row_heights=[
        0.03,
        0.33 + 0.06 - 0.05 + 0.07,
        0.14 - 0.06 + 0.03,
        0.45,
        ],
    column_widths=[1 / 6 - dx_tmp, 1 / 6 + dx_d6, 1 / 6 + dx_d6, 1 / 6 + dx_d6, 1 / 6 + dx_d6, 1 / 6 + dx_d6],
    )






# #########################################################
# #########################################################
# #########################################################


import plotly.graph_objs as go
from plotly.subplots import make_subplots

spec_00 = dict()
spec_01 = dict()

fig = make_subplots(
    rows=1, cols=2,
    specs=[
        [spec_00, spec_01],
        ],
    # print_grid=False,
    # shared_yaxes=False,
    # horizontal_spacing=0.015,
    # vertical_spacing=0.,
    # row_heights=[
    #     0.03,
    #     0.33 + 0.06 - 0.05 + 0.07,
    #     0.14 - 0.06 + 0.03,
    #     0.45,
    #     ],
    # column_widths=[1 / 6 - dx_tmp, 1 / 6 + dx_d6, 1 / 6 + dx_d6, 1 / 6 + dx_d6, 1 / 6 + dx_d6, 1 / 6 + dx_d6],
    )

