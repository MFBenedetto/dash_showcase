from ctypes import alignment
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container
from utils import get_emptyrow

LOGO = "static/logo.png"

def create_navbar():
    navbar =    dbc.Navbar(
                    dbc.Container(
                        [
                            html.A(
                                # Use row and col to control vertical alignment of logo / brand
                                dbc.Row(
                                    [
                                        dbc.Col(["made by",html.Br(), html.Img(src=LOGO, height="30px"), html.Br(), "Polynoes"],
                                        style = {'color': 'white', 'font-size': '12px'}),
                                    ],
                                    align="center",
                                    className="g-1",
                                ),
                                href="http://polynoes.wixsite.com/main",
                                style={"textDecoration": "none"},
                            ),
                            dbc.NavItem(dbc.NavLink("Home", href='/'), style = {'color': 'black', 'font-weight': 'bold'}),
                            get_emptyrow(h=10),
                            dbc.NavItem(dbc.NavLink("Data", href="/data"), style = {'color': 'black', 'font-weight': 'bold'}),
                            get_emptyrow(h=10),
                            dbc.NavItem(dbc.NavLink("Summary", href='/summary'), style = {'color': 'black', 'font-weight': 'bold'}),
                            get_emptyrow(h=10),
                            dbc.NavItem(dbc.NavLink("Business Intelligence", href='/business'), style = {'color': 'black', 'font-weight': 'bold'}),
                            get_emptyrow(h=10),
                            dbc.NavItem(dbc.NavLink("Machine Learning - AI", href='/ML'), style = {'color': 'black', 'font-weight': 'bold'}),
                            get_emptyrow(h=10),
                            dbc.NavItem(dbc.NavLink("Reporting", href='/reporting'), style = {'color': 'black',  'font-weight': 'bold'}),
                        ]
                ),
                expand=True,
                color="gray",
                dark=True,
                style={'margin-top':'0px', 'width': '100%', 'font-size': '24px', 'float': 'center', 'height': '75%', 'align':'center'},
            )
    return navbar