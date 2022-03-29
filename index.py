import base64
import io

from dash import dcc, html, Dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from home import create_home_page
from data import create_data_page
from summary import create_summary_page
from product import create_product_page
from business import create_business_page

import pandas as pd

# The full list of available themes is:
# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX])
server = app.server

 
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/data':
        return create_data_page()
    if pathname == '/summary':
        return create_summary_page()
    if pathname == '/product':
        return create_product_page()
    if pathname == '/business':
        return create_business_page()
    else:
        return create_home_page()


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    if 'csv' in filename:
        # Assume that the user uploaded a CSV file
        return pd.read_csv(
            io.StringIO(decoded.decode('utf-8')))
    elif 'xls' in filename:
        # Assume that the user uploaded an excel file
        return pd.read_excel(io.BytesIO(decoded))


@app.callback(Output('datatable-upload-container', 'data'),
              Output('datatable-upload-container', 'columns'),
              Input('datatable-upload', 'contents'),
              State('datatable-upload', 'filename'))
def update_output(contents, filename):
    if contents is None:
        return [{}], []
    df = parse_contents(contents, filename)
    return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]


@app.callback(Output('datatable-upload-graph', 'figure'),
              Input('datatable-upload-container', 'data'))
def display_graph(df):
    if (df.empty or len(df.columns) < 1):
        return {
            'data': [{
                'x': [],
                'y': [],
                'type': 'bar'
            }]
        }
    return {
        'data': [{
            'x': df[df.columns[0]],
            'y': df[df.columns[1]],
            'type': 'bar'
        }]
    }


if __name__ == '__main__':
    app.run_server(debug=True)
