import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import callback, html, dcc
from navbar import create_navbar
from datetime import date
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

df = px.data.tips()
fig1 = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug",
                   hover_data=df.columns)


# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
x4 = np.random.randn(200) + 4

# Group data together
hist_data = [x1, x2, x3, x4]

group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

# Create distplot with custom bin_size
fig2 = ff.create_distplot(hist_data, group_labels, bin_size=.2)

nav = create_navbar()

fig3 =dict(
            data=[
                dict(
                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                    y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                    350, 430, 474, 526, 488, 537, 500, 439],
                    name='Rest of world',
                    marker=dict(
                        color='rgb(55, 83, 109)'
                    )
                ),
                dict(
                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                    y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                    299, 340, 403, 549, 499],
                    name='China',
                    marker=dict(
                        color='rgb(26, 118, 255)'
                    )
                )
            ],
            layout=dict(
                showlegend=True,
                legend=dict(
                    x=0,
                    y=1.0
                ),
                margin=dict(l=40, r=0, t=40, b=30)
            )
        )


def create_summary_page():
    layout = html.Div([
            nav,
            dbc.Row([dbc.Col(html.H1("SUMMARY"),
                        width={'size': 2, 'offset': 5}),
                    dbc.Col(dcc.DatePickerRange(
                                id='date-picker-range',
                                start_date=date(1997, 5, 3),
                                end_date= date(2022, 3, 31),
                            ),
                        width={'size': 2, 'offset': 2})
                    ], justify="center",  align="end"),
            dbc.Row([dbc.Col(html.H2("Metric 1"),
                            width={'size':2, 'offset':2}
                            ),
                    dbc.Col(html.H2("Metric 2"),
                            width={'size':2, 'offset':1}),
                    dbc.Col(html.H2("Metric 3"),
                            width={'size':2, 'offset':1}),
            ]),
            dbc.Row(
                [
                    dbc.Col(dcc.Dropdown(id='metric_1', placeholder='last dropdown',
                                        options=[{'label': 'Option A', 'value': 'optA'},
                                                {'label': 'Option B', 'value': 'optB'}]),
                            width={'size': 3, "offset": 2, 'order': 3}
                            ),
                    dbc.Col(dcc.Dropdown(id='metric_2', placeholder='first dropdown',
                                        options=[{'label': 'Option A', 'value': 'optA'},
                                                {'label': 'Option B', 'value': 'optB'}]),
                            width={'size': 4, "offset": 1, 'order': 1}
                            ),
                    dbc.Col(dcc.Dropdown(id='metric_3', placeholder='middle dropdown',
                                        options=[{'label': 'Option A', 'value': 'optA'},
                                                {'label': 'Option B', 'value': 'optB'}]),
                            width={'size': 2,  "offset": 0, 'order': 2}
                            ),
                ]
            ),
            html.Hr(),
            dbc.Row([dbc.Col(html.H2("Sales timeline"),
                        width={'size': 3, 'offset':1}),
                    dbc.Col(html.H2("Revenue timeline"),
                        width={'size': 3, 'offset':1})],
                    justify="center", align="end"),
            dbc.Row([dbc.Col(dcc.Graph(id='fig1', figure=fig1),
                        id='fig1',
                        width={'size': 4,  "offset": 2, 'order': 'first'}),
                    dbc.Col(dcc.Graph(id='fig2', figure=fig1),
                            width={'size': 4,  "offset": 1, 'order': 'last'})
            ]),
            html.Hr(),
            dbc.Row([dbc.Col(html.H2("Historic timeline"),
                            width={'size': 'auto', 'offset': 0}
                            )],justify="center", align="end"
                    ),
            dbc.Row([dbc.Col(dcc.Graph(id='fig3', figure=fig3),
                        style={'height': 120},
                        id='fig1',
                        width={'size': 8,  "offset": 2, 'order': 'first'})
            ])
    ])
    return layout

@callback(
    [Output('pie_chart1', 'figure'),
    Output('pie_chart2', 'figure')],
    [Input('a_dropdown', 'value'),
    Input('b_dropdown', 'value'),
    Input('c_dropdown', 'value')]
)
def update_graph(dpdn_a, dpdn_b, dpdn_c):
    dff = df[:200]
    if dpdn_a is None or dpdn_b is None or dpdn_c is None:
        pie_fig = px.pie(dff, names=dff.index, values='Street_robbery', title='Street Robbery Berlin')\
            .update_layout(showlegend=False, title_x=0.5).update_traces(textposition='inside',  textinfo='label+percent')
        pie_fig2 = px.pie(dff, names=dff.index, values='Drugs', title='Drugs Berlin')\
            .update_layout(showlegend=False, title_x=0.5).update_traces(textposition='inside', textinfo='label+percent')
        return pie_fig, pie_fig2
    else:
        raise dash.exceptions.PreventUpdate

