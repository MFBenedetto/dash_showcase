from dash import dcc, html, Dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from home import create_home_page
from data import create_data_page
from summary import create_summary_page
from ML import create_ML_page
from business import create_business_page
from reporting import create_reporting_page
#from config.USERS import USERNAME_PASSWORD_PAIRS


app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX], update_title='Loading...')
server = app.server
 
# import dash_auth
# auth = dash_auth.BasicAuth(
#     app,
#     USERNAME_PASSWORD_PAIRS
# )

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.Div(id='blank-output')
])

app.title = 'Data and analytics dashboard - HOME'
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/data':
        return create_data_page()
    if pathname == '/summary':
        return create_summary_page()
    if pathname == '/ML':
        return create_ML_page()
    if pathname == '/business':
        return create_business_page()
    if pathname == '/reporting':
        return create_reporting_page()
    else:
        return create_home_page()
    return create_home_page()

if __name__ == '__main__':
    app.run_server(debug=True)
