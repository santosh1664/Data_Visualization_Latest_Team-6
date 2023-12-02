import base64
import io
import pandas as pd
import plotly.express as px
from dash import html, dcc, dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from django_plotly_dash import DjangoDash
from dash.dependencies import ClientsideFunction
import requests

# Initialize the Dash app
app = DjangoDash('SimpleGraph')

toggleState = requests.get('/readCookies').text

# Define the app layout with styled components
app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Button('Upload File', style={
            'color': 'white',
            'backgroundColor': '#007BFF',
            'padding': '10px',
            'border': 'none',
            'borderRadius': '5px',
            'cursor': 'pointer'
        }),
        multiple=False,
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        }
    ),
    html.Div(id='page-load-trigger', style={'display': 'none'}),
    html.Div([
        dcc.RadioItems(
            id='graph-type-radio',
            options=[
                {'label': 'Bar', 'value': 'bar'},
                {'label': 'Pie', 'value': 'pie'},
                {'label': 'Scatter', 'value': 'scatter'},
                {'label': 'Line', 'value': 'line'},
                {'label': 'Histogram', 'value': 'histogram'},
            ],
            value='bar',
            labelStyle={'display': 'inline-block', 'marginRight': '10px'},
            style={'display': 'inline-block'}
        ),
        html.Div([
            html.Label('X-Axis:', style={'marginRight': '10px'}),
            dcc.Dropdown(id='x-axis-dropdown')
        ], style={'display': 'inline-block', 'marginRight': '20px', 'width': '180px'}),
        html.Div([
            html.Label('Y-Axis:', style={'marginRight': '10px'}),
            dcc.Dropdown(id='y-axis-dropdown', disabled=False)
        ], style={'display': 'inline-block', 'width': '180px'}),
    ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'marginBottom': '20px'}),
    dcc.Graph(id='graph-output'),
    html.Div(id='initial-cookie-value', style={'display': 'none'})
], style={'width': '80%', 'margin': '0 auto'})

# Function to parse uploaded file contents
def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename or 'xlsx' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            return None
    except Exception as e:
        print(e)
        return None
    return df

# Callbacks
@app.callback(
    [Output('x-axis-dropdown', 'options'),
     Output('y-axis-dropdown', 'options')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def update_dropdowns(contents, filename):
    if contents is None:
        return [], []
    df = parse_contents(contents, filename)
    options = [{'label': i, 'value': i} for i in df.columns]
    return options, options

@app.callback(
    Output('graph-output', 'figure'),
    [Input('graph-type-radio', 'value'),
     Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value'),
     Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def update_graph(graph_type, x_axis, y_axis, contents, filename):
    if contents is None or graph_type is None:
        return dash.no_update

    if (graph_type == 'pie' or graph_type == 'histogram') and x_axis is None:
        return dash.no_update
    elif (graph_type != 'pie' and graph_type != 'histogram') and (x_axis is None or y_axis is None):
        return dash.no_update

    df = parse_contents(contents, filename)
    if df is None:
        return dash.no_update

    df = df.sort_values(by=x_axis) if x_axis in df else df

    if graph_type == 'bar':
        fig = px.bar(df, x=x_axis, y=y_axis)
    elif graph_type == 'pie':
        fig = px.pie(df, names=x_axis, values=y_axis)
    elif graph_type == 'scatter':
        fig = px.scatter(df, x=x_axis, y=y_axis)
    elif graph_type == 'line':
        fig = px.line(df, x=x_axis, y=y_axis)
    elif graph_type == 'histogram':
        fig = px.histogram(df, x=x_axis)
    else:
        fig = dash.no_update

    return fig

@app.callback(
    Output('y-axis-dropdown', 'disabled'),
    [Input('graph-type-radio', 'value')]
)
def toggle_y_axis_dropdown(graph_type):
    return graph_type in ['pie', 'histogram']
