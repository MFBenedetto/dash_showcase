from dash import html
import dash_bootstrap_components as dbc
from navbar import create_navbar
from utils import get_emptyrow

nav = create_navbar()

def create_home_page():

    layout = html.Div( 
                    [nav,
                    get_emptyrow(h=30),
                    html.H1('Data and analytics dashboard', style={'textAlign': 'center'}),
                    html.H2('A web application framework for your data', style={'textAlign': 'center'}),
                    dbc.Col([
                        get_emptyrow(h=30),
                        html.H3('Contents', style={'textAlign': 'left'}),
                        get_emptyrow(h=30),
                        dbc.Col([
                            html.H4('Summary', style={'textAlign': 'left'}),
                            html.H5('A presentation of the key metrics for a quick overview', style={'textAlign': 'left'}),
                            get_emptyrow(h=30),
                            html.H4('Data:', style={'textAlign': 'left'}),
                            html.H5('Load and inspect your data with quick visualization tools', style={'textAlign': 'left'}),
                            get_emptyrow(h=30),
                            html.H4('Business Analytics', style={'textAlign': 'left'}),
                            html.H5('Explore your business data', style={'textAlign': 'left'}),
                            get_emptyrow(h=30),
                            html.H4('Machine learning - AI', style={'textAlign': 'left'}),
                            html.H5('Run ML models', style={'textAlign': 'left'}),
                            get_emptyrow(h=30),
                            html.H4('Reporting', style={'textAlign': 'left'}),
                            html.H5('Create and download a report of the current dashboard', style={'textAlign': 'left'}),
                        ], width={"offset": 1})
                    ], width={"offset": 3})
            ])
    return layout
