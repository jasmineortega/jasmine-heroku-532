import altair as alt
import pandas as pd
from dash import Dash, html, dcc, Input, Output

df = pd.read_csv("netflix.csv")

alt.data_transformers.disable_max_rows()


def plot_altair(ycol):
    chart = alt.Chart(df).mark_point().encode(
        x='type',
        y=ycol).interactive()

    return chart.to_html()

app = Dash(__name__)
server = app.server 

app.layout = html.Div([
        dcc.Dropdown(
            id='ycol', value='release_year',
            options=[{'label': i, 'value': i} for i in df.columns]),
        html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'},
            srcDoc=plot_altair(ycol='release_year'))])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('ycol', 'value'))

def update_output(ycol):
    return plot_altair(ycol)

if __name__ == '__main__':
    app.run_server(
        port = 8070,
        debug=False)