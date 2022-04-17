from dash import html
from navbar import create_navbar
from utils import get_emptyrow

nav = create_navbar()

def create_home_page():

    layout = html.Div( children = [nav,
                    get_emptyrow(h=30),
                    html.H1('Data and analytics dashboard', style={'textAlign': 'center'}),
                    html.Div('A web application framework for your data', style={'textAlign': 'center'})
                        ])


    return layout
