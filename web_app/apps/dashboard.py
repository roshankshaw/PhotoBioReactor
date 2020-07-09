import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

from web_app.app import app

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# colors = {
#     'background': '#111111',
#     'text': '#7FDBFF'
# }

COLORS = ["#fad3cf", "#7971ea", "#a7d129", "#b643cd", "#f95959", "#f5f5c6", "#f6f4f4"]

# df = pd.DataFrame({"x": [1, 2, 3], "SF": [4, 1, 2], "Montreal": [2, 4, 5]})

# fig = px.bar(df, x="x", y=["SF", "Montreal"], barmode="group")
#
# fig.update_layout(plot_bgcolor=colors['background'],
#                   paper_bgcolor=colors['background'], font_color=colors['text'])

layout = html.Div([
    html.Div([
        html.Div([
            html.H1(
                children='DASHBOARD',
                id="dashboard_title",
                className="col"
            ),
        ], className="row"),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Input(
                        id="inpA",
                        placeholder="First Value",
                        className="row col inpUser",
                        value=0
                    ),
                    dcc.Input(
                        id="inpB",
                        placeholder="Second Value",
                        className="row col inpUser",
                        value=0
                    ),
                    dcc.Input(
                        id="inpC",
                        placeholder="Third Value",
                        className="row col inpUser",
                        value=0
                    ),
                    dcc.Input(
                        id="inpD",
                        placeholder="Fourth Value",
                        className="row col inpUser",
                        value=0
                    ),
                    dcc.Input(
                        id="inpE",
                        placeholder="Fifth Value",
                        className="row col inpUser",
                        value=0
                    ),
                    html.Button(
                        children="SUBMIT",
                        id="btnSubmit",
                        className="row align-self-end"
                    )
                ],
                className="container divInputs"),
            ],
                id="divUserInput",
                className="col-md divDisplay"
            ),
            html.Div([
                html.Div(
                    id="divColor",
                    className="align-self-center",
                    style={
                        "background-color": COLORS[0]
                    }
                )
            ],
                id="divBuildingColor",
                className="container d-flex align-items-center justify-content-center col-md divDisplay"
            ),
        ], className="row"),
        html.Div([
            html.Div(
                children='DIV 3',
                id="divGraph1",
                className="col-md divDisplay"
            ),
            html.Div(
                children='DIV 4',
                id="divGraph2",
                className="col-md divDisplay"
            ),
        ], className="row"),
        html.Div([
            html.Button([
                dcc.Link('BUILDING', href='/apps/building')
            ],
                id='btnPageChange',
            ),
        ], className='row justify-content-end')
    ], className="container")
])

@app.callback(
    Output('divBuildingColor', 'children'),
    [
        Input('btnSubmit', 'n_clicks')
    ],
    [
        State('inpA', 'value'),
        State('inpB', 'value'),
        State('inpC', 'value'),
        State('inpD', 'value'),
        State('inpE', 'value'),
    ]
)
def update_color(n_clicks, a, b, c, d, e):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    print(a+b+c+d+e)
    return html.Div(
                    id="divColor",
                    className="align-self-center",
                    style={
                        "background-color":COLORS[(a+b+c+d+e)%7]
                    }
                )