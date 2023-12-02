import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Users/chuda/PycharmProjects/DataVisualisation/static/shopping_trends_updated.csv')

# Group by Age and count the number of occurrences
age_counts = df['Age'].value_counts().reset_index()
age_counts.columns = ['Age', 'Count']

# Create a pie chart
fig = px.pie(age_counts, names='Age', values='Count', title='Distribution of Ages')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div(children=[
    html.H1(children='Customer Shopping Trends Visualization'),

    html.Div(children='''
        Visualizing the distribution of ages in the dataset.
    '''),

    dcc.Graph(
        id='age-distribution-pie-chart',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
