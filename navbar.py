import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

LOGO = "static/logo.png"

def create_navbar():
    navbar =    dbc.Navbar(
                    dbc.Container(
                        [
                            html.A(
                                # Use row and col to control vertical alignment of logo / brand
                                dbc.Row(
                                    [
                                        dbc.Col(["made by",html.Br(), html.Img(src=LOGO, height="35px"), html.Br(), "Polynoes"], className="ms-2",
                                        style = {'color': 'white', 'font-size': '10px'}),
                                    ],
                                    align="right",
                                    className="g-0",
                                ),
                                href="http://polynoes.wixsite.com/main",
                                style={"textDecoration": "none"},
                            ),
                            dbc.NavItem(dbc.NavLink("Home", href='/'), style = {'color': 'black', 'font-size': '24px', 'font-weight': 'bold'}),
                            dbc.NavItem(dbc.NavLink("Data", href="/data"), style = {'color': 'black', 'font-size': '24px', 'font-weight': 'bold'}),
                            dbc.NavItem(dbc.NavLink("Summary", href='/summary'), style = {'color': 'black', 'font-size': '24px', 'font-weight': 'bolder'}),
                            dbc.NavItem(dbc.NavLink("Product analytics", href='/product'), style = {'color': 'black', 'font-size': '24px', 'font-weight': 'bold'}),
                            dbc.NavItem(dbc.NavLink("Business Intelligence", href='/business'), style = {'color': 'black', 'font-size': '24px', 'font-weight': 'bold'}),
                        ]
                ),
                color="lightgray",
                dark=True,
                style={'margin-top':'0px', 'width': '100%', 'float': 'right', 'font-size': '20px'},
            )
    return navbar