from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd

# Local
from pages.project.card import generateCard
from modules.utilities import containerize_projects
from helper import encode_image

#Layout
page_layout = dbc.Container(
    [
        html.Div("My Blogs", className = "page-title"),
        html.H1("Under construction", className = "page-description")
    ],
    fluid=True,
    className="body-container",
)

layout = containerize_projects(page_layout)
