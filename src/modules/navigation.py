from dash import dcc, html

navigation = html.Div([
    dcc.Tabs(id="tabs-content", value='about-tab', children=[
        dcc.Tab(label='About', value='about-tab'),
        dcc.Tab(label='Project', value='project-tab'),
        dcc.Tab(label='Blog', value='blog-tab'),
        dcc.Tab(label='Contact', value='contact-tab'),
    ])
])


          
