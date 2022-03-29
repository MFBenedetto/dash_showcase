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
                                        dbc.Col(["made by", html.Br(), html.Img(src=LOGO, height="35px"), html.Br(), "Polynoes"], className="ms-2",
                                        style = {'color': 'white', 'font-size': '10px'}),
                                    ],
                                    align="right",
                                    className="g-0",
                                ),
                                href="http://polynoes.wixsite.com/main",
                                style={"textDecoration": "none"},
                            ),
                            dbc.NavItem(dbc.NavLink("Home", href='/')),
                            dbc.NavItem(dbc.NavLink("Data", href="/data")),
                            dbc.NavItem(dbc.NavLink("Summary", href='/summary')),
                            dbc.NavItem(dbc.NavLink("Product analytics", href='/product')),
                            dbc.NavItem(dbc.NavLink("Business Intelligence", href='/business')),
                        ]
                ),
                color="grey",
                dark=True,
                style={'margin-top':'0px', 'width': '100%', 'float': 'right', 'font-size': '20px'},
            )
    return navbar