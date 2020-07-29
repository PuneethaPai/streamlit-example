import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import spacy
from spacy import displacy
import flask
import pandas as pd
import time
import os
from .utils import convert_html_to_dash
model = spacy.load("en_core_web_sm")

# Initialisation
server = flask.Flask("app")
app = dash.Dash("app", server=server)

# Frontend
app.layout = html.Div(
    [
        html.H6("Change the value in the text box to see callbacks in action!"),
        html.Div(
            ["Input: ", dcc.Input(id="my-input", value="initial value", type="text")]
        ),
        html.Br(),
        html.Div(id="my-output"),
    ]
)

# Interaction
@app.callback(
    Output(component_id="my-output", component_property="children"),
    [Input(component_id="my-input", component_property="value")],
)
def update_output_div(input_value):
    return f"Your entered Text: {input_value}"
    # return displacy.render(model(input_value), style="ent")


if __name__ == "__main__":
    app.run_server()
