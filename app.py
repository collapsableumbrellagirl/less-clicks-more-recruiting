# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from simple_demo import get_users

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

users = get_users(num_users=50)
users_html = [html.P(f"Name: {user[0]} ... Email: {user[1]} ... Followers: {user[2]} ... Blog: {user[3]} ... Hireable: {user[4]}") for user in users]

app.layout = html.Div(children=[
    html.H1(children='Veronica\'s Cool App!'),
    html.P(children=users_html)
])

if __name__ == '__main__':
    app.run_server(debug=True)
