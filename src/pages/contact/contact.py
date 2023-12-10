import dash_bootstrap_components as dbc
from dash import html
from modules.utilities import containerize_projects
import dash_mantine_components as dmc

page_layout = dbc.Container([
    html.H1("Leave a Message"),
    html.Div("Comment:"),
    dmc.Textarea(autosize=True, minRows=3),
    html.Div("Email:"),
    dmc.TextInput(),
    html.Div("Name:"),
    dmc.TextInput(),
    html.Div(dbc.Button("Submit"), 
        style = {"display":"flex", "justify-content": "right", "width": "100%", "margin-top": "20px"})
])


layout = containerize_projects(page_layout)