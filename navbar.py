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
                                        dbc.Col(["powered by", html.Br(), html.Img(src=LOGO, height="35px"), html.Br(), "Polynoes"], className="ms-2",
                                        style = {'color': 'white', 'font-size': '10px'}),
                                    ],
                                    align="right",
                                    className="g-0",
                                ),
                                href="http://polynoes.wixsite.com/main",
                                style={"textDecoration": "none"},
                            ),
                            dbc.NavItem(dbc.NavLink("Home", href='/')),
                            dbc.NavItem(dbc.NavLink("Upload", href='/upload')),
                            dbc.NavItem(dbc.NavLink("Summary", href='/summary')),
                            dbc.NavItem(dbc.NavLink("Raw data", href="/data")),
                            dbc.NavItem(dbc.NavLink("Page 3", href='/page-3')),
                        ]
                ),
                color="grey",
                dark=True,
                style={'margin-top':'0px', 'width': '100%', 'float': 'right', 'font-size': '25px'},
            )
    return navbar