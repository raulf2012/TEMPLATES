
series_i = go.Contour(

    z=X,
    x=x_range,
    y=y_range,

    zmin=0.2,
    zmax=1.2,

    ncontours=20,

    #| - Color Scale
    colorscale='Jet',
    reversescale=True,
    autocontour=True,
    # showscale=False,
    #__|

    #| - Colorbar
    colorbar=go.contour.ColorBar(

        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        dtick=None,
        exponentformat=None,
        len=None,
        lenmode=None,
        nticks=None,
        outlinecolor=None,
        outlinewidth=None,
        separatethousands=None,
        showexponent=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        thickness=None,
        thicknessmode=None,
        tick0=None,
        tickangle=None,
        tickcolor=None,
        tickfont=None,
        tickformat=None,
        tickformatstops=None,
        tickformatstopdefaults=None,
        ticklen=None,
        tickmode=None,
        tickprefix=None,
        ticks=None,
        ticksuffix=None,
        ticktext=None,
        ticktextsrc=None,
        tickvals=None,
        tickvalssrc=None,
        tickwidth=None,

        title=go.contour.colorbar.Title(
            font=None,
            side=None,  # ['right', 'top', 'bottom']
            text=None,
            ),

        titlefont=None,
        titleside=None,
        x=None,
        xanchor=None,
        xpad=None,
        y=None,
        yanchor=None,
        ypad=None,

        ),
    #__|

    #| - Line
    line=go.contour.Line(
        color="white",
        # dash="dot",
        smoothing=1.,
        # width=0.5,
        width=0.,
        )
    #__|

    )
