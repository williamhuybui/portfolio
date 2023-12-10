from dash import html
import dash_bootstrap_components as dbc
# Local
from helper import encode_image

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("About Me"),
                        html.P(
                            """As a Data Scientist, Mathematician, Full Stack Developer, and Investor, 
                       I embody a rare combination of analytical acumen and technical expertise. 
                       My work in data science involves sifting through complex data sets to c
                       unearth insights, aided by my deep mathematical knowledge. Full stack 
                       development allows me to seamlessly blend front-end creativity with 
                       back-end functionality, creating comprehensive digital solutions. 
                       Investing, on the other hand, taps into my strategic thinking, 
                       enabling me to identify and capitalize on promising opportunities."""
                        ),
                        html.P(
                            """My personality is a blend of competitiveness, meticulousness, 
                        logical reasoning, and empathy. I thrive on challenges and hold myself 
                        to high standards, always paying close attention to the finer details. 
                        Logical thinking guides my professional approach, helping me solve problems 
                        efficiently. Despite my competitive nature, I remain deeply empathetic, 
                        always mindful of how my actions affect others. I believe in fair exchange 
                        of value, hence I neither seek financial gain from advice nor offer it freely."""),
                            html.P(
                                """My passion lies in making a difference. I am driven not just by personal 
                        or professional success, but by the opportunity to help those in need. 
                       This desire to contribute positively to the world motivates my 
                       every endeavor. I value meaningful interactions and always look 
                       forward to hearing interesting stories that offer new perspectives. 
                       These narratives not only enrich my understanding but also fuel my 
                       continuous journey of learning and personal growth."""
                            ),
                    html.H3("My favorite things to do are:"),
                    html.P("""Dota, Chess, and Reading"""),
                    html.H3("Favorite programming language:"),
                    html.P("""Python and Javascript"""),
                    html.H3("Favorite quote:"),
                    html.P("""“The only thing that is constant is change.” – Heraclitus"""),
            ], width=8, lg =5),  # Half width on medium screens and up
                dbc.Col(
                    [
                        html.H3("Pics of Me"),
                        html.Img(src = encode_image("assets/images/SteveBui.jpg"), 
                                 className="home-image"),
                        html.Div(style={"height": "20px"}),
                        html.Img(src = encode_image("assets/images/kobe.jpg"), 
                                 className="home-image")
                    ],
                    width=8, lg = 3,
                    className="pics-container"
                ),  # Half width on medium screens and up
            ]
        ),
    ],
    fluid=True,
    className="body-container",
)

