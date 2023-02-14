from dash import html, callback, dash_table, dcc
from navbar import create_navbar
from utils import get_emptyrow
import dash_bootstrap_components as dbc
import datetime
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA
import numpy as np

d_start = datetime.date(2022, 1, 1)
d_end = datetime.date(2022, 3, 31)

X = [str(d.year)+'-'+str(d.month)+'-'+str(d.day) for d in pd.date_range(start=d_start,end=d_end)]

P = [X[-1]]+[str(d.year)+'-'+str(d.month)+'-'+str(d.day) for d in pd.date_range(start=d_end+datetime.timedelta(days=1),end=d_end+datetime.timedelta(days=14))]

Y = [156,
    109, 139, 165, 206, 191, 148, 197, 175, 145, 159, 200, 216, 242,
    268, 254, 304, 265, 301, 313, 347, 383, 362, 316, 344, 328, 298,
    324, 361, 379, 394, 359, 365, 394, 421, 466, 427, 447, 418, 458,
    415, 433, 409, 401, 379, 366, 388, 349, 357, 328, 348, 350, 335,
    324, 303, 323, 277, 287, 240, 240, 207, 250, 204, 198, 169, 128,
    149, 116, 136, 96, 72, 99, 132, 170, 195, 196, 203, 200, 187, 235,
    244, 233, 276, 228, 270, 231, 276, 282, 236, 272, 263]


df = pd.DataFrame({'Date': X, 'Sale': Y[1:]})

data = [{'Date': x, 'Sales': y} for x,y in zip(X,Y)]

columns=[{"name": i, "id": i, "type": "numeric"} for i in ['Date', 'Sales']]

@callback(
    Output('graph', 'figure'),
    [Input('submit', 'n_clicks')],
    [State('table', 'data')]
)
def update(n_clicks, data):
    if data is None:
        raise PreventUpdate
    
    X = [d.get('Date') for d in data]
    Y = [d.get('Sales') for d in data]

    fig = go.Figure()
    # Create and style traces
    fig.add_trace(
        go.Scatter(
                x=X,
                y=Y,
                name='Historical sales',
                line=dict(color='firebrick', width=4)
            )
        )

    # fit model
    model = ARIMA(np.array(Y), order=(16, 2, 6))
    fitted = model.fit()
    # make prediction
    preds = np.insert(fitted.forecast(14),0,Y[-1],axis=0)

    fig.add_trace(go.Scatter
                    (x=P, y=preds, name='Predictions',
                         line=dict(color='royalblue', width=4, dash='dot')))

    # Edit the layout
    fig.update_layout(
                    xaxis_title='Month',
                    yaxis_title='Sales')

    return fig

nav = create_navbar()
header = html.H1('Machine Learning and AI', style={'textAlign': 'center'})
subheader = html.H3('Sales prediction', style={'textAlign': 'center'})
subsubheader = html.H3('Edit the data and obtain real-time forecasting', style={'textAlign': 'center'})
def create_ML_page():
    layout = html.Div([
                nav,
                get_emptyrow(h=30),
                header,
                get_emptyrow(h=20),
                subheader,
                get_emptyrow(h=20),
                subsubheader,
                dbc.Row([
                    dbc.Col(
                        [
                            dash_table.DataTable(
                                id='table',
                                columns=columns,
                                data=data,
                                editable=True,
                                page_action="native",       # all data is passed to the table up-front or not ('none')
                                page_current=0,             # page number that user is on
                                page_size=5,               # number of rows visible per page
                                fill_width=False
                            ),
                            html.Button(id='submit', children=['Submit'])
                        ], width=2, align='center'),
                        dbc.Col(
                            dcc.Graph(id='graph'),
                        width=8, align='center')
                ], justify='center'),
            ]
        )

    return layout