import dash_bootstrap_components as dbc
from dash import html, dcc

def containerize_projects(projects):
    return dbc.Row(
                [
                    dbc.Col(width = 0, md = 1, lg = 2),
                    dbc.Col(
                        [
                            html.Div(projects, className = "project-container")
                        ],
                        width = 12, md = 10, lg = 8,
                        className="project-body-container",
                    ),
                    dbc.Col(width = 0, md = 1, lg = 2),
                ]
            )