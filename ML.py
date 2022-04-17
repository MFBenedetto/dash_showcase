from dash import html
from navbar import create_navbar
from utils import get_emptyrow

nav = create_navbar()
header = html.H1('Machine Learning and AI', style={'textAlign': 'center'})
subheader = html.H3('Sales prediction', style={'textAlign': 'center'})

def create_ML_page():
    layout = html.Div([
                nav,
                get_emptyrow(h=30),
                header,
                get_emptyrow(h=20),
                subheader
            ]
        )
    return layout