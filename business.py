from dash import html
from navbar import create_navbar

nav = create_navbar()

header = html.H3('BUSSINESS')

def create_business_page():
    layout = html.Div([
        nav,
        header,
    ])
    return layout
