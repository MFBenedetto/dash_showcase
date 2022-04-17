from email.quoprimime import header_check
from tkinter import X
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html, dcc
from navbar import create_navbar
from datetime import date
import numpy as np
import plotly.graph_objects as go
from utils import get_emptyrow

m1 = go.Figure()
m1.add_trace(go.Indicator(
    mode = "number+delta",
    value = 1150,
    delta = {'reference': 800, 'relative': True},
    domain = {'x': [0, 1], 'y': [0, 1]}))

m1.update_layout(
    title={
        'text': "<span style='color:black'>ACCOUNTS</span><br><span style='color:gray'>ACTIVE</span>",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
            'yanchor': 'top'},
    font= {'size':24}
    )

m2 = go.Figure(go.Indicator(
    mode = "number+delta",
    value = 492,
    delta = {"reference": 500, "valueformat": ".0f"},
    domain = {'y': [0, 1], 'x': [0.25, 0.75]}))

m2.add_trace(go.Scatter(
    y = [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413,419, 404, 408, 401, 377, 368, 361, 356, 359, 375, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456, 436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 480, 492]))

m2.update_layout(
    xaxis = {'range': [0, 62]},
    title={
        'text': "<span style='color:black'>USERS ONLINE</span>",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font= {'size':24}
    )

m3 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 450,
    domain = {'x': [0, 1], 'y': [0, 1]}
))


m3.update_layout(
    title={
        'text': "<span style='color:black'>SUBSCRIPTIONS</span>",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font= {'size':24}
    )

nav = create_navbar()
header = html.H1("Summary", style={'textAlign': 'center'})


def create_summary_page():
    card = dbc.Card(
    [dbc.CardHeader("Header"), dbc.CardBody("Body")], className="h-100"
)

    graph_card = dbc.Card(
        [dbc.CardHeader("Here's a graph"), dbc.CardBody("An amazing graph")],
        className="h-100",
    )

    layout1 = html.Div([
                nav,
                get_emptyrow(h=30),
                dbc.Col(dcc.DatePickerRange(
                                id='date-picker-range',
                                start_date=date(2022, 1, 1),
                                end_date= date(2022, 3, 31), style={'textAlign': 'center'}),
                                width={'size': 4, 'offset':1}),
                header,
                get_emptyrow(h=20),
                dbc.Row(
                    [
                    dbc.Col(
                        [
                            dbc.Row([dbc.Col(card)] * 4, style={"height": "300px"}),
                            get_emptyrow(h=40),
                            html.H2("Based on forecase done an approximate amount..."),
                            dbc.Row(
                                [dbc.Col(graph_card)] * 2, style={"height": "500px"}
                            ),
                        ],
                    width=8,
                    ),
                    dbc.Col(card, width=2),
                    ],
                justify="center",
            )],
            style={
                    'margin': 0 #Or whatever number suits your needs
                },
            )

    layout = html.Div([

            dbc.Row([dbc.Col(dcc.Graph(id='m1', figure=m1),
                        id='fig1',
                        width={'size': 3,  "offset": 0, 'order': 1}),
                    dbc.Col(dcc.Graph(id='m2', figure=m2),
                            width={'size': 5,  "offset": 0, 'order': 2}),
                    dbc.Col(dcc.Graph(id='m3', figure=m3),
                            width={'size': 3,  "offset": 0, 'order': 3})],
                justify="center", align='end'),
    ])
    return layout1