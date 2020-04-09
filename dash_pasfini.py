import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.offline as pyo
import numpy as np
import scipy
from statsmodels.stats import weightstats
import seaborn as sns
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

test = pd.read_csv("D:/Simplon/Brief projet/Titanic/test.csv")
train = pd.read_csv("D:/Simplon/Brief projet/Titanic/train.csv")

train["Age"].fillna(train["Age"].mean(), inplace = True)
del train["Cabin"]
train.dropna(inplace= True)

#===============================================================================================

def generate_table(dataframe):
    cols = dataframe.columns
    return html.Table([
        html.Thead(
            html.Tr(
                [html.Th("Index")] + [html.Th(col) for col in cols]
            )
        ),
        html.Tbody([
            html.Tr([html.Td(dataframe.index[i])] + [html.Td(dataframe.iloc[i][col]) for col in cols]) for i in range(len(dataframe))
        ])
    ])

def generate_serie(serie, title) :
    return html.Table([
        html.Thead(
            html.Tr([html.Th(title)])
        ),
        html.Tbody([
            html.Tr([
                html.Td(serie.index[i]),
                html.Td(serie.values[i])
            ]) for i in range(len(serie))
        ])
    ])


#===============================================================================================

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

app.layout = html.Div(style = {"backgroundColor" : colors['background']}, children=[
    html.H1(children='Le Titanic',
            style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.H3(children='Il était une fois ...',
            style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),
    html.Div([
        html.Img(src="/assets/Route_Titanic.PNG",
                style={
                    'height' : '75%',
                    'width' : '75%'
                })
    ],
    style={'textAlign': 'center'}
    ),
    html.H3(children='Embarquement à Southampton :',
            style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div([
        generate_table(train[["Age", "Pclass", "Fare"]][train.Embarked == "S"].describe())
    ]),
    html.H3(children='Embarquement à Cherbourg :',
            style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div([
        generate_table(train[["Age", "Pclass", "Fare"]][train.Embarked == "C"].describe())
    ]),
    html.H3(children='Embarquement à Queenstown :',
            style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div([
        generate_table(train[["Age", "Pclass", "Fare"]][train.Embarked == "Q"].describe())
    ]),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash DataT Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {'color': colors['text']}
            }
        }
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)





































