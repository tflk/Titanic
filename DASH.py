import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

gender = pd.read_csv("D:/Simplon/Brief projet/Titanic/gender_submission.csv")
test = pd.read_csv("D:/Simplon/Brief projet/Titanic/test.csv")
train = pd.read_csv("D:/Simplon/Brief projet/Titanic/train.csv")

def summary(serie):
    for k in range(len(serie.index)) :
        print(html.H3(serie.index[k], ":", serie.values[k]))

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H3("Dash App"),
    dcc.Dropdown(
        id = "my-dropdown",
        options = [
            {'label' : "Coke", "value" : "COKE"},
            {'label' : "Tesla", "value" : "TSLA"},
            {'label' : "Apple", "value" : "AAPL"}
        ],
        value = "COKE"
    ),
    dcc.Graph(
        id = "my-graph"
    ),
    html.H3(
        summary(train.Age.describe())
    )
])

""" @app.react("my-graph", ["my-dropdown"])

def update_graph(dropdown_properties):
    selected_value = dropdown_properties["value"]
    df = web.DataReader(
        dropdown_properties["value"], "yahoo",
        dt(2016, 1, 1), dt.now()
    )
    return {
        'figure' : go.Figure(
            data = [
                Scatter(
                    x = df.index,
                    y = df.Close,
                    name = selected_value
                )
            ]
        )
    }
 """

if __name__ == '__main__':
    app.run_server(debug=True)





















