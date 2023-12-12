from dash  import Input, Output, html, dcc, Dash
import dash_bootstrap_components as dbc
#Local files
from pages.home import home
from pages.blog import blog
from pages.contact import contact
from pages.gallery import gallery
from pages.project import project
from modules import navigation, footer, color_mode_switch
from dash_bootstrap_templates import load_figure_template


#https://community.plotly.com/t/updating-external-stylesheets-via-callback/31635/10
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.CYBORG])
load_figure_template(["minty", "minty_dark"])
app = Dash(external_stylesheets=[dbc.themes.MINTY, dbc.icons.FONT_AWESOME])
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navigation.navigation,
    color_mode_switch.color_mode_switch,
    html.Div(id='page-content'),
    footer.footer
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/blog':
        return blog.layout
    elif pathname == '/contact':
        return contact.layout
    elif pathname == '/project':
        return project.layout
    elif pathname == '/gallery':
        return gallery.layout
    else:
        return home.layout

@app.callback(
    Output('url', 'pathname'),
    Input('tabs-content', 'active_tab'))
def nav_choice(tab):
    print(tab)
    if tab == 'about-tab':
        return '/'
    elif tab == 'project-tab':
        return '/project'
    elif tab == 'blog-tab':
        return '/blog'
    elif tab == 'contact-tab':
        return '/contact'
    else:
        return '/'


app.clientside_callback(
    """
    (switchOn) => {
       switchOn
         ? document.documentElement.setAttribute('data-bs-theme', 'light')
         : document.documentElement.setAttribute('data-bs-theme', 'dark')
       return window.dash_clientside.no_update
    }
    """,
    Output("switch", "id"),
    Input("switch", "value"),
)

if __name__ == '__main__':
    app.run_server(debug=True)