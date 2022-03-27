from dash import dcc, html, Dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from home import create_home_page
#from upload import create_upload_page
from data import create_data_page
from summary import create_summary_page
from page_3 import create_page_3

# The full list of available themes is:
# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX])
server = app.server

import pandas as pd
 
server = app.server
app.config.suppress_callback_exceptions = True

df = pd.read_csv('data/data.csv')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
#    if pathname == '/upload':
#        return create_upload_page()
    if pathname == '/summary':
        return create_summary_page()
    if pathname == '/page-3':
        return create_page_3()
    if pathname == '/data':
        return create_data_page(df)
    else:
        return create_home_page()


if __name__ == '__main__':
    app.run_server(debug=True)
