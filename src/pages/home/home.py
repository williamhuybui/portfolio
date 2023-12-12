from dash import html, dcc
import dash_bootstrap_components as dbc

# Local
from helper import encode_image
from modules.utilities import containerize_projects
from pages.home.chart import skill_radio_chart

page_layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Div("About Me", className="page-title"),
                html.Div("Hi, I'm Huy Bui. I work in data science and I love building things.", className ="page-description"),
                html.Hr(),
                dbc.Col(
                    [
                        html.Div("What I do", className = "page-section"),
                        html.Div("I have five years of experience as a Data Scientist, primarily in start-up settings, which I find thrilling. Tackling intricate issues and creating projects from the ground up is something I take great pleasure in. My expertise includes:",
                                 className = "section-content"),
                        # html.Ul([
                        #     html.Li("Machine learning"),
                        #     html.Li("Fullstack web application"),
                        #     html.Li("Math"),
                        #     html.Li("Experimentation"),
                        # ]),
                        dcc.Graph(figure = skill_radio_chart()),
                        html.Hr(),
                        html.Div("Learning All the Time", className = "page-section"),
                        html.Div("I think we never stop learning new things. I feel happy when I learn something. But sometimes, I realize there's a lot I don't know. That's why I made this website. It helps me remember what I learn. It also lets me show others what I've done and what I've learned.", 
                                 className = "section-content"),
                        html.Img(src = encode_image("assets/images/leetcode.png"), 
                                 className="home-image"),
                        html.Hr(),
                        html.Div("Away from the Computer", className = "page-section"),
                        html.Div("When I'm not working, I might be in a coffee shop reading a book or playing Dota.",
                                 className = "section-content"),
                        html.Img(src = encode_image("assets/images/dota.png"), 
                                 className="home-image"),
                        html.Hr(),
                        html.Div("Let's Talk", className = "page-section"),
                        html.Div("If you want to know more about data science, see some web designs, or just learn about my journey, I'm happy you're here. Feel free to get in touch if you want to work together, talk, or even just chat about games or coffee.", 
                                 className = "section-content"),
                        
            ], width=12, lg = 8),  # Half width on medium screens and up
                dbc.Col(
                    [
                        html.H3("Pics of Me", className = "page-section"),
                        html.Img(src = encode_image("assets/images/SteveBui.png"), 
                                 className="home-image"),
                        html.Div(style={"height": "20px"}),
                        html.Img(src = encode_image("assets/images/kobe.jpg"), 
                                 className="home-image")
                    ],
                    width = 12, lg = 4,
                    className="pics-container"
                ),  # Half width on medium screens and up
            ]
        ),
    ],
    fluid=True,
    className="body-container",
)

layout = containerize_projects(page_layout)

