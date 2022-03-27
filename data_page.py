from dash import html
from navbar import create_navbar
nav = create_navbar()

header = html.H3('Raw data')

def create_data_page(df):
    layout = html.Div([
        nav,
        header,
    ])
    
    layout = ddk.App(show_editor=True, children=[
    ddk.DataTable(
       id='table',
       columns=[{"name": i, "id": i} for i in df.columns],
       data=df.to_dict('records'),
       editable=True
    )
    ])
    return layout