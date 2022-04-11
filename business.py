from dash import html, callback
from navbar import create_navbar
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from utils import get_emptyrow

nav = create_navbar()

header = html.H1("Business Intelligence", style={'textAlign': 'center'})

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

@callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55, title = 'Life expectancy by GDP')

    fig.update_layout(transition_duration=100)
    return fig

def create_business_page():
    layout = [
        nav,
        get_emptyrow(h=30),
        header,
        html.Center(
        html.Div([dcc.Graph(id='graph-with-slider', 
                            style = {'textAlign': 'center'}),
                    dcc.Slider(
                        df['year'].min(),
                        df['year'].max(),
                        step=None,
                        value=df['year'].min(),
                        marks={str(year): str(year) for year in df['year'].unique()},
                        id='year-slider'
                    )
                ],style={'textAlign': 'center', 'width': "40%"}))
    ]
    return layout