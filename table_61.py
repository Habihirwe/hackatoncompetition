import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from app import app

# Load your data from the Excel file
data = pd.read_excel("SAS 2022_Tables.xlsx", sheet_name='Table 61', skiprows=2)
df1 = pd.DataFrame(data)
df1 = df1.drop(columns=['Unnamed: 0'])
df = df1.drop(df1.index[-2:])

# Create a Dash app
# app = Dash(__name__)

# Define the app layout
layout_61 =[
    html.Div([
    html.H1("Types of anti-errosion activities"),

    # Dropdown to select columns
    dcc.Dropdown(
        id='column-dropdownn',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='Ditches',  # Default column to display
        style={'width': '50%'}
    ),

    # CSS styles
    html.Div([
        dcc.Graph(id='bar-chartt', style={'margin': '20px'}),
    ]),  # Adjust the width to control the size
])
] 

# Define a callback function to update the bar chart based on the selected column
@app.callback(
    Output('bar-chartt', 'figure'),
    Input('column-dropdownn', 'value')
)
def update_bar_chart(selected_column):
    # Check if the selected column is in the DataFrame columns
    if selected_column not in df.columns:
        raise ValueError(f"Selected column '{selected_column}' is not present in the DataFrame columns. Available columns: {df.columns}")

    fig = px.bar(df, x='Disrtict', y=selected_column, height=400)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
