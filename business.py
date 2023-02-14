from dash import html, callback
from navbar import create_navbar
from dash import callback, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from utils import get_emptyrow
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

nav = create_navbar()

header = html.H1("Business Intelligence", style={'textAlign': 'center'})

dfGDP = pd.read_csv('data/GDPdata.csv')
dfGDP = dfGDP.rename(columns={'gdpPercap': 'Sales', 'lifeExp': 'Revenue'})

heatmap = go.Figure(data=go.Heatmap(
                    z=dfGDP['Sales'],
                    y=dfGDP['year'],
                    x=dfGDP['country'],
                    colorscale='Turbo'))
heatmap.update_layout(margin=dict(l=0, r=0, t=0, b=0))

df = px.data.tips()
df['customer'] = df['sex'].replace({'Female': 'Normal', 'Male': 'Premium'})
df['Bill'] = df['total_bill']

@callback(
    Output("graph1", "figure"), 
    Input("distribution", "value"))
def display_graph(distribution):
    fig1 = px.histogram(df, x="Bill", y="Bill", color="customer", marginal=distribution.lower().strip(),
                    hover_data=df.columns)

    fig1.update_layout(margin=dict(l=0, r=0, t=0, b=0))

    return fig1

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

tab_layout = html.Div([
            dbc.Row([
            dbc.Col(html.Div([
                    dcc.Tabs(id="tabs", value='tab-1', children=[
                            dcc.Tab(label='Revenue History', value='tab-1', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='Revenue Heatmap', value='tab-2', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='Distribution', value='tab-3', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='Timeline', value='tab-4', style=tab_style, selected_style=tab_selected_style),
                        ], style=tabs_styles),
                        get_emptyrow(h=10),
                        html.Div(id='tabs-content')
                ]), width=10)
            ], justify="center", align='start') #end row
        ])#end div


# Add histogram data
x1 = np.random.randn(260) + 8
x2 = np.random.randn(180) + 10
x3 = np.random.randn(150) + 9
x4 = np.random.randn(250) + 14
x5 = np.random.randn(40) + 20

# Group data together
hist_data = [x1, x2, x3, x4, x5]

group_labels = ['Americas', 'Africa','Europe', 'Asia', 'Oceania', ]

# Create distplot with custom bin_size
fig2 = ff.create_distplot(hist_data, group_labels, bin_size=.2)

fig2.update_layout(height=350,
                margin=dict(l=0, r=0, t=0, b=0))

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
                    y=0.5
                ),
                margin=dict(l=0, r=0, t=0, b=30),
            )
        )

def get_heatmap_plot():
    return html.Center([
                html.H3('Revenue (in Millions of USD) from sales'),
                        dcc.Graph(figure=heatmap,
                                style = {'textAlign': 'center'}),
                ])


def get_GDP_plot():
    return html.Center([
                html.H3('Revenue (in Millions of USD) from sales'),
                dbc.Col( 
                [
                        dcc.Graph(id='graph-with-slider', 
                                style = {'textAlign': 'center'}),
                        dcc.Slider(
                            dfGDP['year'].min(),
                            dfGDP['year'].max(),
                            step=None,
                            value=dfGDP['year'].max(),
                            marks={str(year): str(year) for year in dfGDP['year'].unique()},
                            id='year-slider')
                    ],
                    style = {'text-align':'center'})
                ])

def get_timeline_plot():
        return [dbc.Row([dbc.Col(html.H3("Market share timeline"),
                        width={'size': 'auto', 'offset': 0}
                        )],justify="center", align="center"
                ),
                dbc.Row([dbc.Col(dcc.Graph(id='graph3', figure=fig3),
                    style={'height': 10},
                    id='fig1')
                ],justify="evenly", align="start")]

@callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = dfGDP[dfGDP.year == selected_year]

    fig = px.scatter(filtered_df, x="Sales", y="Revenue",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)
    fig.update_layout(transition_duration=50)
    return fig


def get_dist_plots():
    return [dbc.Row([dbc.Col(html.H3("Client expenditure"),
                    width={'size': 6, 'offset':0},
                    style = {'text-align':'center'}),
                dbc.Col(html.H3("Client tenure distribution"),
                    width={'size': 6, 'offset':0},
                    style = {'text-align':'center'})],
                justify="evenly", align="center"),
                dbc.Row([dbc.Col([
                    dcc.RadioItems(
                        id='distribution',
                        options=[' Box ', 'Violin ', ' Rug '],
                        value='box', inline=True
                    ),
                    dcc.Graph(id='graph1')],
                        width={'size': 6,  "offset": 0, 'order': 'first'}),
                dbc.Col(dcc.Graph(id='graph2', figure=fig2),
                            width={'size': 6,  "offset": 0, 'order': 'last'})
        ], justify="evenly", align='center')]

@callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return get_GDP_plot()
    if tab == 'tab-2':
        return get_heatmap_plot()
    elif tab == 'tab-3':
       return get_dist_plots()
    elif tab == 'tab-4':
       return get_timeline_plot()


def create_business_page():
    layout = [
        nav,
        get_emptyrow(h=30),
        header,
        get_emptyrow(h=10),
        tab_layout,
    ]
    
    return layout

