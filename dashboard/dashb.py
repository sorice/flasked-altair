from flask import Flask, render_template, url_for, redirect, jsonify,\
                Blueprint, make_response
import json
from dashboard.plot import Div
from dashboard.plot import make_static_chart, make_interactive_chart

main = Blueprint('main', __name__)

# ----- Generate Altair Charts -----
chart_1 = make_static_chart()
chart_2 = make_interactive_chart()

# ----- Charts Payload -----
charts_ = [{'id': 'scatter_1',
            'chart_as_json': json.loads(chart_1.to_json())
            },
           {'id': 'interactive_1',
            'chart_as_json': json.loads(chart_2.to_json())
            }
    ]

# ----- Build Payload -----

page_title = Div(id='page_title',
                 class_='tc f2 code pa4 bg-washed-green',
                 children='Flask + Altair')

row_1 = Div(class_='pa4 w-60 center bb helvetica fw2',
            children="""Paragraph example, a lot of text for explanations
            accompanying the graphs to help to understand the context.""")

row_2 = Div(class_='w-60 center bb helvetica fw2',
            children=[
                Div(class_='fl w-50 pa4',
                    id='scatter_1',
                    children=None),
                Div(class_='fl w-50 pa4 tl',
                    children="""Text accompanying graph 1, just to.
                                show composed DIV""")
                ])

row_3 = Div(class_='w-60 center bb helvetica fw2',
            children=[
                Div(id='tchart1',
                    class_='tc w-100 pa4',
                    children='Select some points, and drag the selection.'),
                Div(id='column',
                    class_= 'tc w-100 pa4',
                    children = [
                        Div(id='interactive_1',
                            class_='tr',
                            children=None),
                        Div(id='button1',
                            class_='btn btn-lg btn-success',
                            children='Zoom')])])

payloads_ = [page_title, row_1, row_2, row_3]

@main.route('/')
def index():
    return render_template('index.html', payloads=payloads_, charts=charts_)

#https://vega.github.io/vega-lite/tutorials/getting_started.html
@main.route('/vlspec', methods = ['GET'])
def serve_vlspec():
    value = {
        "data": {
            "values": [
            {"a": "C", "b": 2}, {"a": "C", "b": 7}, {"a": "C", "b": 4},
            {"a": "D", "b": 1}, {"a": "D", "b": 2}, {"a": "D", "b": 6},
            {"a": "E", "b": 8}, {"a": "E", "b": 4}, {"a": "E", "b": 7}
            ]
        },
        "mark": "bar",
        "encoding": {
            "y": {"field": "a", "type": "nominal"},
            "x": {
            "aggregate": "average", "field": "b", "type": "quantitative",
            "axis": {"title": "Mean of b"}
            }
        }
    }
    return make_response(jsonify(value),200)

if __name__ == '__main__':
    app.run(debug=True)
