import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SLATE,"assets/style.css"],suppress_callback_exceptions=True, use_pages=True,meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}])

app.css.config.serve_locally = True,

app.layout = html.Div([
	dash.page_container,
])


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port='8050', debug=True)
