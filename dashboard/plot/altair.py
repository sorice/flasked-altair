import altair as alt
from vega_datasets import data

def make_static_chart1():
    '''
    '''
    return alt.Chart(data=data.cars()).mark_circle(size=60).encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='Origin:N',
        tooltip='Origin:N',
    ).interactive()

def make_static_chart():
    '''
    '''
    return alt.Chart(data=data.iris()).mark_circle(size=60).encode(
        x='petalLength:Q',
        y='petalWidth:Q',
        color='species:N',
        tooltip='sepalWidth:Q',
    ).interactive()

def make_interactive_chart():
    '''
    '''
    pts = alt.selection_interval(encodings=['x','y'])

    rect = alt.Chart(data.cars()).mark_point().encode(
        x='Miles_per_Gallon:Q',
        y='Horsepower:Q',
        color=alt.condition(pts, 'Origin', alt.value('lightgray'))
    ).properties(
        selection = pts
    )

    # scale=alt.Scale(scheme='greenblue'),
    #         legend=alt.Legend(title='Total Sample')
    #     )
    # circ = rect.mark_point().encode(
    #     alt.ColorValue('grey'),
    #     alt.Size('count()',
    #         legend=alt.Legend(title='Sample in Selection')
    #     )
    # ).transform_filter(
    #     pts
    # )

    return alt.vconcat(
        rect | rect.encode(x='Acceleration')
    ).resolve_legend(
        color="independent",
        size="independent"
    )
