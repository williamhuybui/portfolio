from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd

# Local
from pages.project.card import generateCard
from modules.utilities import containerize_projects
from helper import encode_image


data = pd.read_excel('data/projects.xlsx')

#Layout
page_layout = dbc.Container(
    [
        html.H3("Filter by:", className = "label"),
        dmc.Grid([
            dmc.Col(html.Div("Skill", className = 'label'), span = 1),
            dmc.Col(dcc.Dropdown(
                options = sorted(list(set(item for sublist in data['techs'].apply(eval) for item in sublist))),
                multi=True,
                id = 'skills-dd'
                ), span = 5),
                ]),
        dmc.Grid([
            dmc.Col(html.Div("Name", className = 'label'), span = 1),
            dmc.Col(dcc.Dropdown(
                options = data['title'],
                id = 'name-dd'
                ), span = 5),
            ]),
        html.Div(id = 'project-result'),
    ],
    fluid=True,
    className="body-container",
)

layout = containerize_projects(page_layout)

#Callback
def filter_project(filter_data):
    img_root = 'data/app_img/'
    return [ 
        generateCard(
            title= filter_data.iloc[i]['title'],
            link=filter_data.iloc[i]['link'],
            description=filter_data.iloc[i]['description'],
            techs=filter_data.iloc[i]['techs'],
            img_path = f"{img_root}{filter_data.iloc[i]['img']}",
            other_pairs=filter_data.iloc[i]['other_pairs']
        ) for i in range(len(filter_data))
    ]


@callback(
    Output("project-result", 'children'),
    Input("skills-dd", 'value'),
)
def filter_by_skills(skills):
    filter_data = data.copy()
    if skills:
        filter_data = filter_data[filter_data['techs'].apply(lambda x: set(skills).issubset(eval(x)))]
    return filter_project(filter_data)

@callback(
    Output("project-result", 'children', allow_duplicate=True),
    Input("name-dd", 'value'),
    prevent_initial_call = True
)
def filter_by_skills(name):
    filter_data = data.copy()
    if name:
        filter_data = filter_data[filter_data['title'].str.lower().str.contains(name.lower())]
    return filter_project(filter_data)