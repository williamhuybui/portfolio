from dash import dcc, html
import dash_bootstrap_components as dbc

# navigation = html.Div([
#     dcc.Tabs(id="tabs-content", value='about-tab', children=[
#         dcc.Tab(label='About', value='about-tab'),
#         dcc.Tab(label='Project', value='project-tab'),
#         dcc.Tab(label='Blog', value='blog-tab'),
#         dcc.Tab(label='Contact', value='contact-tab'),
#     ])
# ])

navigation = dbc.Tabs(
            [
                dbc.Tab(label='About', tab_id='about-tab'),
                dbc.Tab(label='Project', tab_id='project-tab'),
                dbc.Tab(label='Blog', tab_id='blog-tab'),
                dbc.Tab(label='Contact', tab_id='contact-tab'),
            ],
            id="tabs-content",
            active_tab="about-tab",
)
          
