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

        layout = html.Div([create_navbar(),
                            dbc.Row(),
                            html.H1(children="Upload and inspect data",style={'color':'#00361c','text-align':'center'}),
                            dbc.Row([dbc.Col(html.Div(), width=3),
                                     dbc.Col(html.Div(dash_table.DataTable(
                                                        id='datatable-interactivity',
                                                        columns=[
                                                            {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
                                                            if i == "iso_alpha3" or i == "year" or i == "id"
                                                            else {"name": i, "id": i, "deletable": True, "selectable": True}
                                                            for i in df.columns
                                                        ],
                                                        data=df.to_dict('records'),  # the contents of the table
                                                        editable=True,              # allow editing of data inside all cells
                                                        filter_action="native",     # allow filtering of data by user ('native') or not ('none')
                                                        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
                                                        sort_mode="single",         # sort across 'multi' or 'single' columns
                                                        column_selectable="multi",  # allow users to select 'multi' or 'single' columns
                                                        row_selectable="multi",     # allow users to select 'multi' or 'single' rows
                                                        row_deletable=True,         # choose if user can delete a row (True) or not (False)
                                                        selected_columns=[],        # ids of columns that user selects
                                                        selected_rows=[],           # indices of rows that user selects
                                                        page_action="native",       # all data is passed to the table up-front or not ('none')
                                                        page_current=0,             # page number that user is on
                                                        page_size=20,               # number of rows visible per page
                                                        style_cell={                # ensure adequate header width when text is shorter than cell's text
                                                            'minWidth': 95, 'maxWidth': 95, 'width': 95
                                                        },
                                                        style_cell_conditional=[    # align text columns to left. By default they are aligned to right
                                                            {
                                                                'if': {'column_id': c},
                                                                'textAlign': 'left'
                                                            } for c in ['country', 'iso_alpha3']
                                                        ],
                                                        style_data={                # overflow cells' content into multiple lines
                                                            'whiteSpace': 'normal',
                                                            'height': 'auto'
                                                        }))),
                                                        dbc.Col(html.Div(), width=3)]),
                            html.Br(),
                            html.Br(),
                            html.Div(id='fig1'),
                            html.Div(id='fig2')
                        ])

    else:
        header = html.H1(f'File {filename} not found, please go to Load page')
        layout = html.Div([
        ])
    return layout