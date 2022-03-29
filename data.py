from os.path import exists
import pandas as pd

from dash import dash_table, dcc, html
import dash_bootstrap_components as dbc

from navbar import create_navbar


def create_data_page():
    
    filename = 'data.csv' # @todo make this variable depend on a selection in index
    path_to_file = f'data/{filename}' 

    if exists(path_to_file):
        df = pd.read_csv('data/data.csv')

        layout = html.Div([ create_navbar(),
                            html.H3('Upload and inspect data'),
                            dbc.Table.from_dataframe(
                                df, striped=True, bordered=True, hover=True, index=True
                            )],
        )
    else:
        header = html.H1(f'File {filename} not found, please go to Load page')
        layout = html.Div([
        ])
    return layout