import altair as alt
from vega_datasets import data

def make_static_chart():
    '''
    '''
    return alt.Chart(data=data.cars()).mark_circle(size=60).encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
        tooltip='Origin:N',
    ).interactive()

def make_interactive_chart():
    '''
    '''
    pts = alt.selection(type="single", encodings=['x'])

    rect = alt.Chart(data.iris()).mark_rect().encode(
        alt.X('petalLength:Q', bin=True),
        alt.Y('petalWidth:Q', bin=True),
        alt.Color('species',
            scale=alt.Scale(scheme='greenblue'),
            legend=alt.Legend(title='Total Sample')
        )
    )

    circ = rect.mark_point().encode(
        alt.ColorValue('grey'),
        alt.Size('count()',
            legend=alt.Legend(title='Sample in Selection')
        )
    ).transform_filter(
        pts
    )

    line = alt.Chart(data.stocks()).mark_line().encode(
        x='date:T',
        y='price:Q',
        color=alt.condition(pts, alt.ColorValue("steelblue"), alt.ColorValue("grey"))
    ).properties(
        selection=pts,
        width=550,
        height=200
    )

    return alt.vconcat(
        rect + circ,
        line
    ).resolve_legend(
        color="independent",
        size="independent"
    )
