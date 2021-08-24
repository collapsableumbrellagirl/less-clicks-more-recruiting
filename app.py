# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from simple_demo import get_users

external_stylesheets = [dbc.themes.BOOTSTRAP, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

users = get_users(num_users=50)

app.layout = html.Div(children=[
    dbc.Container(children=[
        dbc.Row(children=[
            dbc.Col(children=[
                html.H1(children='Veronica\'s Cool App!'),
            ])
        ]),
        dbc.Row(children=[
            dbc.Col(
                children=[
                    dash_table.DataTable(
                        id='table',
                        columns=[
                            {"name": "name", "id": "name"},
                            {"name": "followers", "id": "followers"}
                        ],
                        data=users,
                    )
                ],
                width=4
            ),
            dbc.Col(children=[
                html.Iframe(
                    src="https://profile-summary-for-github.com/user/tipsy",
                    height=660,
                    width=800,
                    id="profile-summary-iframe"
                )
            ])
        ])
    ], fluid=True)
])

@app.callback(
    Output(component_id="profile-summary-iframe", component_property="src"),
    Input(component_id="table", component_property="active_cell"),
    State(component_id="table", component_property="derived_virtual_data")
)
def handle_table_click(
    active_cell,
    data,
):
    if not active_cell or not active_cell.get("row"):
        return "https://profile-summary-for-github.com/search"

    username = data[active_cell["row"]]["username"]
    return f"https://profile-summary-for-github.com/user/{username}"


if __name__ == '__main__':
    app.run_server(debug=True)
