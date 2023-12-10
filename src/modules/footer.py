import dash_bootstrap_components as dbc
from dash import html, dcc
from helper import encode_image

def logo_component(image_path, link):
    return html.A(
        html.Img(src= encode_image(image_path), className = "footer-logo"), 
        href = link, 
        )

logo_container = html.Div([
    logo_component("data/footer/linkedin.png", 'https://www.linkedin.com/in/huy-bui-ds/'),
    logo_component("data/footer/medium.png", 'https://medium.com/@williamhuybui'),
    logo_component("data/footer/github.png", 'https://github.com/williamhuybui'),
], className = "footer-logo-container")

email_container = html.Div(
    html.Div("williamhuybui@gmail.com", 
        className = "email"), 
    className = "footer-email-container")

footer = html.Div([
    html.Hr(),
    email_container,
    logo_container
], className = 'footer-container')
