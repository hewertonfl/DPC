# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from pickle import TRUE
from pydoc import classname
from turtle import position, width
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash_bootstrap_templates import load_figure_template
import waitress
from assets.npdr import database
from yolov5app.custom_detect import run

dash.register_page(__name__,path='/')

## Elementos do layout
#Navbar
navbar = dbc.NavbarSimple(
    [
        dbc.NavItem(dbc.NavLink("DPC", href="/dpc"),style={}),
        # dbc.DropdownMenu(
        #     children=[
        #         dbc.DropdownMenuItem("Mais", header=True),
        #         dbc.DropdownMenuItem("Page 2", href="#",),
        #         dbc.DropdownMenuItem("Page 3", href="#",),
        #     ],
            # nav=True,
            # in_navbar=True,
            # label="More",
            # style={""},
        # ),
    ],
    brand="Cadastro",
    brand_href="/",
    brand_style={"margin-left":""},
    color="primary",
    dark=True,
    style={"display":"inline-block","visibility":"visible","z-index":"10"},
)
#Função que retorna os nomes e as caixas com os inputs
def input_box(item,id):
    return html.Div(
        [
            dbc.Card(
                dbc.CardBody([
                    html.Div([
                        dbc.Row(html.P(f"{item}"),className="text-box-style"),
                        dbc.Row(dcc.Input(id=f"{id}", type="text", placeholder="",style={"border":"none","border-radius":"20px 20px 20px 20px"}),
                                style={"margin":"5px 0 0 0","width":"100%"}),
                    ],style={"border":"none","width":"100%"}), 
                ],className="input-box-style",
                )
            ,outline=True,style={"border":"none","opacity":"60%"}),
        ],style={"margin-top":"20px","border-radius":"20px 20px 20px 20px"},)

#Layout do card de cadastro
cad= html.Div([
                dbc.Container(
                    [
                        dbc.Row([
                            dbc.Col([html.P(["RP-Registrador de Placas"],className="NDPR-title")],
                        width={"size":9})],justify="center"),
                        dbc.Row([
                            dbc.Col([input_box("Nome:","input1")],width={"size":9},className="COL_STYLE"),
                        ],justify="center",align="center"),

                        dbc.Row([
                            dbc.Col([input_box("Carro:","input2")],width={"size":9},
                            className="COL_STYLE"),
                        ],justify="center"),

                        dbc.Row([
                            dbc.Col([input_box("Placa:","input3")],width={"size":9},
                            className="COL_STYLE"),
                        ],justify="center"),

                        dbc.Row([
                            dbc.Col(dbc.Button('Salvar Dados', id='save-button', n_clicks=0,
                            style={"width":"100%",},
                            className="save-button-style"),width={"size":9}, style={"padding":"20px"})
                        ],justify="center"),

                    ],className="cad-style"),
            ],style={"display":"block","height":"100%","background-color":"",})

# Função que builda o card com o carro
def fig_card(text):
    return html.Div([
            dbc.Container(
            [
                dbc.Row([html.Img(id='img',src="./assets/carro.jpg",alt='image',
                className="fig-style")],justify="center"),

                dbc.Row([html.P(f"{text}",
                style={"text-align":"center","border":"5px solid","background-color":"white","margin-right":"2px","margin-top":"2px",})])
            ],style={"padding-top":"50px","border-radius":"50%",})
        ],className="fig-card")

#Layout da grade de cards
def content_cam(xs=dict(order=2, size=12),sm=dict(order=2, size=12),md=dict(order=2, size=12)):
    return html.Div([
            dbc.Row([
                dbc.Row([dbc.Col([fig_card("Cam 1")],xs,sm,md),dbc.Col([fig_card("Cam 2")],xs,sm,md)],className="adapter"),
                dbc.Row([dbc.Col([fig_card("Cam 3")],xs,sm,md),dbc.Col([fig_card("Cam 4")],xs,sm,md)],className="adapter"),
                dbc.Row([dbc.Col([fig_card("Cam 5")],xs,sm,md),dbc.Col([fig_card("Cam 6")],xs,sm,md)],className="adapter"),
            ])
        ],className="content-cam-style",)


#Montagem do layout
layout = html.Div(
[
    dbc.Row(
    [
        dbc.Row([navbar],
        style={"width":"100%","margin":"0"}),

        dbc.Row([
            dbc.Col([
                dbc.Row([cad],
                justify="center",align="center")],
                width={'size':12},
                xs=dict(order=1, size=12),
                sm=dict(order=1, size=12),
                md=dict(order=1, size=12),
                lg=dict(order=1, size=12),
                xl=dict(order=1, size=12), 
                ),
            # dbc.Col([
            #     dbc.Row([content_cam()],
            #     justify="center")],
            #     align="center",width={'size':7},
            #     xs=dict(order=2, size=12),
            #     sm=dict(order=2, size=12),
            #     md=dict(order=2, size=12),
            #     lg=dict(order=2, size=7),
            #     xl=dict(order=2, size=7), 
            #     )
        ],
        align="center",
        className="root-container body-style"),
        
        dbc.Row(
            [
                dbc.Col(html.Img(id='img',src="./assets/logo.png",alt='logo',className="footer-logo-style"),
                align="center",style={"display":"flex","justify-content":"center"})            
            ],
            justify="center",
            className="footer-style",
           ),
    
    ],justify="center"),

    html.P(id='placeholder'),

],style={"height":"100vh","width":"100vw","overflow":"hidden","margin":"0"})

# Retorna os valores dos inputs digitados na barra de cadastro
@dash.callback(
    Output('input1','value'),
    Output('input2','value'),
    Output('input3','value'),
    Output('save-button','n_clicks'),
    Input('input1','value'),
    Input('input2','value'),
    Input('input3','value'),
    Input('save-button','n_clicks'),
    prevent_initial_call=True
)
def _(input1,input2,input3,n_clicks):
    if n_clicks>0:
        database(input1,input2,input3)
        return '','','',0
    else:
        return
    
if __name__ == '__main__':
    dash.run_server(host='0.0.0.0',port='8050',debug=False)
