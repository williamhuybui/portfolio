from dash import dcc, html
import dash_bootstrap_components as dbc

color_mode_switch =  html.Div(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch(id="switch", value=True, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ],
    className = "switch"
)