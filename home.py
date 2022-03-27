from dash import html
from navbar import create_navbar

nav = create_navbar()

header = html.H3('Welcome to the home page!')

def create_page_home():
    layout = html.Div([
        nav,
        header,
    ])
    return layout
