from dash import html
from navbar import create_navbar

nav = create_navbar()

header = html.H3('PRODUCT')

def create_product_page():
    layout = html.Div([
        nav,
        header,
    ])
    return layout
