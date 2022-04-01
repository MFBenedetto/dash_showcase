from tkinter import X
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import callback, html, dcc
from navbar import create_navbar
from datetime import date
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
import plotly.graph_objects as go


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
    y = [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 356, 359, 375, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456, 436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 480, 492]))

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

df = px.data.tips()
df['customer'] = df['sex'].replace({'Female': 'Normal', 'Male': 'Premium'})
df['Bill'] = df['total_bill']
fig1 = px.histogram(df, x="Bill", y="Bill", color="customer", marginal="rug",
                   hover_data=df.columns)

# Add histogram data
x1 = np.random.randn(200) + 8
x2 = np.random.randn(200) + 10
x3 = np.random.randn(200) + 9
x4 = np.random.randn(200) + 14

# Group data together
hist_data = [x1, x2, x3, x4]

group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

fig1.update_layout(height=450)

# Create distplot with custom bin_size
fig2 = ff.create_distplot(hist_data, group_labels, bin_size=.2)

fig2.update_layout(height=450)

dates = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
fig3 = dict(
            data=[
                dict(
                    x=dates,
                    y=[0.03, 0.02, 0.08, 0.16, 0.01, 0.14, 0.11, 0.19, 0.21, 0.1, 0.06, 0.23, 0.17, 0.24, 0.07, 0.15, 0.04, 0.05],
                    name='Rest of world',
                ),
                dict(
                    x=dates,
                    y=[0.82, 0.81, 0.86, 0.9, 0.89, 0.88, 0.87, 0.99, 0.92, 0.94, 0.98, 0.85, 0.96, 0.93, 0.95, 0.8, 0.97, 0.83],
                    name='China',
                ),
                dict(
                    x=dates,
                    y=[0.68, 0.5, 0.34, 0.74, 0.19, 0.04, 0.77, 0.33, 0.84, 0.37, 0.97, 0.73, 0.11, 0.94, 0.61, 0.13, 0.1, 0.44],
                    name='Europe',
                ),
                dict(
                    x=dates,
                    y=[0.8, 0.44, 0.45, 0.82, 0.56, 0.83, 0.9, 0.49, 0.92, 0.97, 0.58, 0.61, 0.76, 0.51, 0.71, 0.84, 0.41, 0.5],
                    name='USA')
            ],
            layout=dict(
                showlegend=True,
                legend=dict(
                    x=0,
                    y=1.0
                ),
                margin=dict(l=40, r=0, t=40, b=30),
            )
        )

nav = create_navbar()

def create_summary_page():
    layout = html.Div([
            nav,
            dbc.Col(dcc.DatePickerRange(
                                id='date-picker-range',
                                start_date=date(2022, 1, 1),
                                end_date= date(2022, 3, 31), style={'textAlign': 'center'}),
                                width={'size': 4, 'offset':1}),
            html.H1("SUMMARY", style={'textAlign': 'center'}),
            dbc.Row([dbc.Col(dcc.Graph(id='m1', figure=m1),
                        id='fig1',
                        width={'size': 3,  "offset": 0, 'order': 1}),
                    dbc.Col(dcc.Graph(id='m2', figure=m2),
                            width={'size': 5,  "offset": 0, 'order': 2}),
                    dbc.Col(dcc.Graph(id='m3', figure=m3),
                            width={'size': 3,  "offset": 0, 'order': 3})],
                justify="center", align='end'),
            html.Hr(),
            dbc.Row([dbc.Col(html.H2("Client expenditure"),
                        width={'size': 4, 'offset':0},
                        style = {'text-align':'center'}),
                    dbc.Col(html.H2("Revenue timeline"),
                        width={'size': 4, 'offset':0},
                        style = {'text-align':'center'})],
                    justify="evenly", align="end"),
            dbc.Row([dbc.Col(dcc.Graph(id='fig1', figure=fig1),
                        id='fig1',
                        width={'size': 4,  "offset": 0, 'order': 'first'}),
                    dbc.Col(dcc.Graph(id='fig2', figure=fig2),
                            width={'size': 4,  "offset": 0, 'order': 'last'})
            ], justify="evenly"),
            html.Hr(),
            dbc.Row([dbc.Col(html.H2("Market share timeline"),
                            width={'size': 'auto', 'offset': 0}
                            )],justify="center", align="end"
                    ),
            dbc.Row([dbc.Col(dcc.Graph(id='fig3', figure=fig3),
                        style={'height': 120},
                        id='fig1',
                        width={'size': 10,  "offset": 0, 'order': 'first'})
            ],justify="evenly", align="end")
    ])
    return layout