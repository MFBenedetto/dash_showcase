from tkinter import X
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html, dcc
from navbar import create_navbar
import plotly.graph_objects as go
from utils import get_emptyrow
import pandas as pd
import datetime
import plotly.express as px


d_start = datetime.date(2022, 1, 1)
d_end = datetime.date(2022, 3, 31)

sunburst = pd.read_csv('data/sunburst.csv')

sunburst = px.sunburst(sunburst, path=['size', 'name',], values='value',
                  color='size', hover_data=['name'],
                  color_continuous_scale='RdBu')


sunburst.update_layout(margin=dict(t=0,b=0,l=0,r=0),
        width = 270,  height = 316)

m1 = go.Figure()
m1.add_trace(go.Indicator(
    mode = "number+delta",
    value = 1150,
    delta = {'reference': 800, 'relative': True}))

m1.update_layout(
    font= {'size':16},
    margin=dict(t=0,b=0,l=0,r=0),
    height = 160
    )

m2 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 450,
    mode = "gauge+number+delta",
    delta = {'reference': 400},
    gauge = {'axis': {'range': [None, 600]},
             'steps' : [
                 {'range': [0, 250], 'color': "lightgray"},
                 {'range': [250, 400], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 500}}))

m2.update_layout(
    font= {'size':16},
    margin=dict(t=0,b=0,l=0,r=0),
    width = 280,
    height = 160
    )

m3 = go.Figure()
m3.add_trace(go.Indicator(
    mode = "number+delta",
    value = 12,
    delta = {'reference': 15, 'relative': True}))

m3.update_layout(
    font= {'size':16},
    margin=dict(t=0,b=0,l=0,r=0),
    height = 160
    )
m3.update_xaxes(range=[X[0], X[-1]])

Y = [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413,419, 404, 408, 401, 377, 368, 361, 356, 359, 375,
     397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456,
     436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 480, 492, 418, 423, 423, 426, 447,
     436, 418, 429, 415, 502, 497, 432, 419, 394, 410, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 487]

m4 = go.Figure(go.Indicator(
    mode = "number+delta",
    value = Y[-1],
    delta = {"reference": 500, "valueformat": ".0f"},
    domain = {'y': [0, 1], 'x': [0.25, 0.75]}))

m4.add_trace(go.Scatter(
    x = pd.date_range(start=d_start,end=d_end+datetime.timedelta(days=5)),
    y = Y)
    )



m4.update_layout(
    font= {'size':16},
    margin=dict(t=0,b=20,l=50,r=20),
    height = 220
    )

nav = create_navbar()
header = html.H1("Key Company Metrics ", style={'textAlign': 'center'})

def create_card(header='Header', title= 'Title', body="Body", figure=[], color='info'):
    return dbc.Card([
    dbc.CardHeader(header),
    dbc.CardBody(
        [
            html.H5(title, className="card-title"),
            html.P(
                body,
                className="card-text",
            ),
        ]
    ),
    html.Center(dcc.Graph(figure=figure, className = 'Card image'))
    ], color=color, outline=True
    )

def create_KPI5():
    return    dbc.Card([
                dbc.CardHeader('KPI5'),
                dbc.CardBody(
                [
                html.H5('Recent customers',className="card-title"),
                get_emptyrow(h=20),
                html.Center([
                    html.H6('Reims Collectables'),
                    html.P('Reims,France. Henriot, Paul'),
                    html.Hr(),
                    html.H6('Salzburg Collectables'),
                    html.P('Salzburg, Austria. Pipps, Georg'),
                    html.Hr(),
                    html.H6('Online Diecast Creations Co.'),
                    html.P('Nashua,USA. Young, Valarie.'),
                    html.Hr(),
                    get_emptyrow(h=21),
                    dcc.Graph(figure=sunburst, className = 'Card image'),
                    get_emptyrow(h=21),
                    ])
                ]),],
                color='primary', outline=True)

def create_summary_page():
    layout = html.Div([
                nav,
                get_emptyrow(h=30),
                header,
                get_emptyrow(h=20),
                dbc.Col(dcc.DatePickerRange(
                                id='date-picker-range',
                                start_date=d_start,
                                end_date=d_end, style={'textAlign': 'center'},
                                display_format='DD/MM/Y',
                                start_date_placeholder_text='DD/MM/YY'),
                                width={'size': 4, 'offset':1},
                                lg={'size': 3, 'offset':2},
                                xl={'size': 3, 'offset':2},
                                ),
                get_emptyrow(h=20),
                dbc.Container([
                dbc.Row(
                    [
                    dbc.Col(
                        [
                            dbc.Row([
                                dbc.Col(create_card(header='KPI1', title='Accounts', body='Active', figure=m1, color="info")),
                                dbc.Col(create_card(header='KPI2', title='Subscriptions', body='Baseline: 400, Goal: 500', figure=m2, color="info")),
                                dbc.Col(create_card(header='KPI3', title='Average revenue', body='per user', figure=m3, color="info"))], style={"height": "300px"}
                            ),
                            get_emptyrow(h=20),
                            html.Center(
                                html.H4('Evolution of online users')),
                            get_emptyrow(h=20),
                            dbc.Row(
                                [dbc.Col(create_card(
                                    header='KPI4',title='Daily Online users timeline', body='Baseline: Last period', figure=m4, color="primary"))], 
                                    style={"height": "350px"}
                            ),
                        ],
                    width=7,
                    lg=7, xl=7#, xxl=5
                    ),
                    dbc.Col(create_KPI5(), width={'size': 3, 'offset':0}, xl=3)
                    ],
                    align="start",
                    justify="center",
                    style={
                        'margin-bottom': 0
                    }
                )],
                    fluid=True,
                    className="mt-4",
                    ),
            ],
            style={
            'margin-b': 0
            })
    return layout
    