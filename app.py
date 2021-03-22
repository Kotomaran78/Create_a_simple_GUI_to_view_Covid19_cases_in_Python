import json
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go



with open("data_covid.json", "r") as read_file:
    data = json.load(read_file)

x = []
for normal_date in data['Global']['data']:
    d = 0
    day = ''
    month = ''

    for l in normal_date:
        if l == ".":
            d = 1
        if d == 0:
            day += l 
        if d == 1:
            if l != ".":
                if last == 1:
                    if l == "0":
                        pass
                    else:
                        month +=l
                else:
                    month +=l
        if l == ".":
            last = 1

        if l != ".":
            last = 0

    x.append(datetime.datetime(year=2020,month=int(month), day=int(day)),)

figr = go.Figure()

figr.add_trace(go.Scatter(
    x=x,
    y=data['Global']['infected'],
    name="infected"
    ))

figr.add_trace(go.Scatter(
    x=x,
    y=data['Global']['deth'],
    name="deth"
    ))

figr.add_trace(go.Scatter(
    x=x,
    y=data['Global']['recovered'],
    name="recovered"
    ))

figr.update_layout(showlegend = True, hovermode = "x unified", autosize = True)

figr.update_yaxes(automargin=True)



def gener_dropdown():
    opt = []
    for contry in data:
        opt.append({'label': contry, 'value': contry},)
    return opt

config = dict ({ 
    'scrollZoom' :  True,
    'displayModeBar' :  True,
    'modeBarButtonsToRemove' :  ['lasso2d',  'select2d', 'toImage'],
    'displaylogo' :  False,
    })


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.H1(id = 'chil', children='Global')]),
    html.Div([
        html.Button('Update All', id='btn-1', n_clicks=0),
        html.Button('Update', id='btn-2', n_clicks=0),
        html.H1(children=' '),
        dcc.Dropdown(
            id='Dropdown',
            options=gener_dropdown(),
            value='Global'
        )
    ],style={'width': '30%', 'display': 'inline-block',}),

    html.Div(style={'height': '77vh'},
         children=dcc.Graph(
            id='example-graph',
            figure = figr,
            config = config,
            responsive = True,
            style = ({'height' : 'inherit'})
        )
    )
    
])

@app.callback(
    [Output(component_id='chil', component_property='children'),
    Output(component_id='example-graph', component_property='figure')],
    [Input(component_id='Dropdown', component_property='value')]
)

def update_output_div(contry):

    with open("data_covid.json", "r") as read_file:
        dat = json.load(read_file)


    x = []
    for normal_date in dat[contry]['data']:
        d = 0
        day = ''
        month = ''

        for l in normal_date:
            if l == ".":
                d = 1
            if d == 0:
                day += l 
            if d == 1:
                if l != ".":
                    if last == 1:
                        if l == "0":
                            pass
                        else:
                            month +=l
                    else:
                        month +=l
            if l == ".":
                last = 1

            if l != ".":
                last = 0

        x.append(datetime.datetime(year=2020,month=int(month), day=int(day)),)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=dat[contry]['infected'],
        name="infected"
        ))

    fig.add_trace(go.Scatter(
        x=x,
        y=dat[contry]['deth'],
        name="deth"
        ))

    fig.add_trace(go.Scatter(
        x=x,
        y=dat[contry]['recovered'],
        name="recovered"
        ))

    fig.update_layout(showlegend = True, hovermode = "x unified", autosize = True)

    fig.update_yaxes(automargin=True)

    return str(contry), fig


if __name__ == '__main__':
    app.run_server()