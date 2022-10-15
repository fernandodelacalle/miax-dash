
import dash
from dash import html
import pandas as pd

df = pd.read_csv('data/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    tabla = html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
    return tabla


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df),
    generate_table(df)
])

if __name__ == '__main__':
    app.run(debug=True)
