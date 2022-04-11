from dash import html
from navbar import create_navbar
from utils import get_emptyrow

nav = create_navbar()

def create_reporting_page():

    layout = html.Div( children = [nav,
                    get_emptyrow(h=30),
                    html.H1('Generate reports', style={'textAlign': 'center'}),
                    html.Div('Save and download', style={'textAlign': 'center'})
                        ])


    return layout
