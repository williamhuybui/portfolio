from dash_iconify import DashIconify
from dash import html, dcc
import dash_bootstrap_components as dbc
from helper import encode_image

def generateCard(title, link, description, techs, img_path, other_pairs = None):
    """
    other_pairs: pair of name and link
    """
    others_comp = []
    if other_pairs:
        for name, link in eval(other_pairs):
            others_comp.append(dbc.Button([name, DashIconify(icon = "fluent:open-16-regular", className = 'project-others-icon')],
                                          href = link, className = 'project-others-btn'))
        others = html.Div(others_comp, className = 'project-others')
    return dbc.Row([
        dbc.Col(html.Img(src = encode_image(img_path), className="responsive-image"),
          md = 4, sm = 12, 
          className = "img-container"),
        dbc.Col([
            html.A(title, href = link, className = 'project-title'),
            html.P(description, className = 'project-description'),
            html.Div([html.Div(tech, className="tech-tag") for tech in eval(techs)], className = 'project-techs'),
            others
        ], 
        md = 8, sm = 12, 
        className = 'project-content')
    ], className = "project-card")