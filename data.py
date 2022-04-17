import os
import pandas as pd
import base64
import plotly.express as px
from dash import dash_table, dcc, html, callback
import dash_bootstrap_components as dbc
from navbar import create_navbar
from utils import get_emptyrow
from dash.dependencies import Input, Output

import base64
import io

import pandas as pd
from dash.dependencies import Input, Output
from utils import get_emptyrow

PATH = 'data' 
DATA = pd.read_csv(os.path.join(PATH, 'empty.csv'))

nav = create_navbar()

@callback([Output('datatable', 'data'), Output('datatable', 'columns')],
            Input('dropdown', 'value'))
def display_table(value=''):
    if value is None:
        return DATA
    file = os.path.join(PATH, value)

    try:
        if 'csv' in file:
            # Assume that the user uploaded a CSV or TXT file
            df = pd.read_csv(file)
        elif 'xls' in file:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(file)
        else:
            df = DATA
    except Exception as e:
        print(e)
        df = DATA

    return [df.to_dict('records'), [{"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True} for i in df.columns]]
    

@callback(
    [Output(component_id='fig1', component_property='children'),
    Output(component_id='var_name', component_property='children')],
    [Input(component_id='datatable', component_property="derived_virtual_data"),
    Input(component_id='datatable', component_property="selected_columns")]
)
def update_bar(all_rows_data,selected_columns):
    if len(selected_columns)>0:
        try:
            dff = pd.to_numeric(pd.DataFrame(all_rows_data), errors='raise')
            fig=px.histogram(dff, x=selected_columns)
            fig.update_layout(showlegend=False)
            return [
                dcc.Graph(
                        figure=fig
                )
            ], f'Plotting variable {selected_columns}'
        except:
            dff = pd.DataFrame(all_rows_data).astype('category')
            fig=px.histogram(dff, x=selected_columns)
            fig.update_layout(showlegend=False)
            return [
                dcc.Graph(
                        figure=fig,
                        style={"height": "100%", "width": "80%"}
                )
            ], f'Plotting variable {selected_columns}'
    else:
        return html.H3('Select a column to plot'), ' '

# Highlight selected column
@callback(
    Output('datatable', 'style_data_conditional'),
    [Input('datatable', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': {'column_id': i},
        'background_color': '#D2F3FF'
    } for i in selected_columns]

def create_data_page():
    files = [f for f in os.listdir(PATH) if f.endswith(".csv") or f.endswith(".xlsx") and f not in ('empty.csv')]
    layout = html.Div([
                    nav,
                    get_emptyrow(h=30),
                    html.H1(children="Explore and edit your data",style={'text-align':'center'}),
                    get_emptyrow(h=20),
                    dbc.Row(
                        dbc.Col([
                            html.Div(                                    
                                    dcc.Dropdown(options=files, style={'width': '100%'}, value=files[0], id='dropdown')
                                )
                            ],
                            width={'size': 2, 'offset': 0},
                            align='center'),
                            justify="evenly",
                            align="start"
                    ),
                    get_emptyrow(h=10),
                    html.Hr(),
                    get_emptyrow(h=10),
                    html.A(id='filename',style={'color':'#00361c','text-align':'center'}),
                    dash_table.DataTable(
                        id='datatable',
                        data=DATA.to_dict('records'),
                        columns= [{"name": i, "id": i} for i in DATA.columns],
                        editable=True,              # allow editing of data inside all cells
                        filter_action="native",     # allow filtering of data by user ('native') or not ('none')
                        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
                        sort_mode="single",         # sort across 'multi' or 'single' columns
                        column_selectable="single",  # allow users to select 'multi' or 'single' columns
                        row_selectable="multi",     # allow users to select 'multi' or 'single' rows
                        row_deletable=True,         # choose if user can delete a row (True) or not (False)
                        selected_columns=[],        # ids of columns that user selects
                        selected_rows=[],           # indices pof rows that user selects
                        page_action="native",       # all data is passed to the table up-front or not ('none')
                        page_current=0,             # page number that user is on
                        page_size=10,               # number of rows visible per page
                        style_cell={                # ensure adequate header width when text is shorter than cell's text
                            'height': 'auto', 'minWidth': 95, 'maxWidth': 95, 'width': 95
                        },
                        style_cell_conditional=    # align text columns to left. By default they are aligned to right
                            [{
                                'textAlign': 'center'
                            }],
                        style_data = {                # overflow cells' content into multiple lines
                            'whiteSpace': 'normal',
                            'height': 'auto'
                        },
                        style_table = {
                            'overflowX': 'auto',
                            'width':'85%',
                            'margin':'auto'},
                    ),
                    html.Hr(),
                    get_emptyrow(h=50),
                    html.Center([
                        html.H2(id='var_name', children=" ",style={'text-align':'center'}),
                        html.Div(id='fig1')]
                    ),
                    get_emptyrow(h=50),
            ])

    return layout
