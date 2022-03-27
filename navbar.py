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
                                    dbc.Col(html.Img(src=LOGO, height="40px")),
                                    dbc.Col(dbc.NavbarBrand("Polynoes", className="ms-2")),
                                ],
                                align="center",
                                className="g-0",
                            ),
                            href="/",
                            style={"textDecoration": "none"},
                        ),
                        dbc.NavItem(dbc.NavLink("Home", href='/')),
                        dbc.NavItem(dbc.NavLink("Upload data page", href='/data_page')),
                        dbc.NavItem(dbc.NavLink("Summary", href='/summary')),
                        dbc.NavItem(dbc.NavLink("Page 3", href='/page-3')),
                        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
                    ]
                ),
            color="dark",
            dark=True,
        )
    return navbar