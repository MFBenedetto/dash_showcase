from dash import html
from navbar import create_navbar

nav = create_navbar()

header = html.H3('SUMMARY')


def create_summary():
    layout = html.Div([
        nav,
        header,
    ])
    return layout
