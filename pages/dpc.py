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
from dash.exceptions import PreventUpdate
from assets.npdr import read_database
from yolov5app.custom_detect import run

dash.register_page(__name__)

# Estilos
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "25.4vw",
    "height": "100%",
    "padding":" 15vh 5vw",
    "background-color": "#1e1e1e",
    "overflow-y":"auto",
}

H2_STYLE = {
    "font-family":"'open sans'",
    "font-weight":"700",
    "line-height": "1.25", 
    "padding-left": "12px",
    "font-size":"18px","letter-spacing":"2.1px",
    "color":"#d8d8d8",
    "margin-bottom":"1.8rem",
    "margin-top":"1.8rem",
    "text-decoration":"none",
}

P_STYLE = {
    "font-family":"'open sans'",
    "font-size":"10px",
    "padding-left": "12px",
    "text-decoration":"none",
    "font-wight" : "300"
}

LIST_STYLE = {
    "textAlign":"center",
    "padding" : "30px",
    "margin" : "5px",
    "text-decoration":"none",
    "border-radius":"2%"
}

# Elementos do layout
sidebar = html.Div(
    [
        html.H2("DPC - DETECÇÃO DE PLACA DE CARRO",style=H2_STYLE),
        html.Hr(),
        html.P("Clique em detectar para exibir os dados",style=H2_STYLE),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("Aguardando ação...",id="box1",style=LIST_STYLE,className="item-style"),
                dbc.ListGroupItem("Aguardando ação...",id="box2",style=LIST_STYLE,className="item-style"),
                dbc.ListGroupItem("Aguardando ação...",id="box3",style=LIST_STYLE,className="item-style"),
            ],
            flush=True),
        dbc.Row([
            dbc.Col(dbc.Button('Home', id='home',href='/home', n_clicks=0,style={"width":"100%"}),style={"padding":"5px"}),
            dbc.Col(dbc.Button('Detectar', id='detectar', n_clicks=0,style={"width":"100%"}),style={"padding":"5px"}),
            # dbc.Col(dbc.Button('Submit', id='3', n_clicks=0,style={"width":"100%"}),style={"padding":"5px"}),
        ],justify ="center",style={"margin":"0","position":"relative","top":"20px"}),
        dbc.Row([dbc.Col( dbc.RadioItems(
            options=[
                {"label": "Placa", "value": "imagens/placa.jpg"},
                {"label": "Carro", "value": "carro.jpg"},
            ],
            className= "radio-hover",
            value="lupa.png",
            id="radioitems_input",
            inline=True),style={"display":"flex","justify-content":"center","position":"relative","top":"30px"})

            ])
    ],
    style=SIDEBAR_STYLE,
)

imgCard = html.Div(
    [   
        dbc.Row([
            dbc.Col([
            html.Img(id='img',src="./assets/lupa.png",alt='image',className="img")#)
            ],align="center")],justify="center"
    
    ),     
    ],style={"display":"flex","justify-content":"center","overflow-y":"auto",},
)

#Montagem do layout
layout = html.Div(
    [
        dbc.Row(
            [
            dbc.Col([sidebar,],
           ),

            dbc.Col(
            [
               
                dbc.Col([imgCard],align="center")                            
      
            ],align="center",
            width=9)
        ],style={"height":"100vh","overflow":"hidden",},align="center")
    ],style={"overflow":"hidden","background-color":"rgb(20,20,20)"}
)

@dash.callback(
    Output('img','src'),
    Input('radioitems_input','value')
)

def _(radioitems_input):
    img=f'./assets/{radioitems_input}'
    #print(img)
    return img
    
@dash.callback(
    Output('box1','children'),
    Output('box2','children'),
    Output('box3','children'),
    Input('detectar','n_clicks'),
)

def __(n_clicks):
    if n_clicks ==1:
        run()
        f=open("./assets/imagens/digitosplaca.txt", "r+")
        digitosplaca = f.readline()
        if(digitosplaca == ""):
            box1,box2,box3 = ["ERRO", "ERRO", "ERRO"]
        else:
            box1,box2,box3=read_database(digitosplaca)
        return ["Nome: "+box1],["Carro: "+box2],["Placa: "+ box3]
    else:
        raise PreventUpdate


if __name__ == '__main__':
    dash.run_server(host='0.0.0.0', port='8050', debug=True,)

# if __name__ == "__main__":
#     from waitress import serve
#     print('Run server on 0.0.0.0:8888')
#     serve(app.server, port=8000, host="0.0.0.0")