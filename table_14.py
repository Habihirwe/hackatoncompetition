import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from app import app

# Load your data from the Excel file
data = pd.read_excel("SAS 2022_Tables.xlsx", sheet_name='Table 14', skiprows=2)
df1 = pd.DataFrame(data)
df1 = df1.drop(columns=['Unnamed: 0'])
df = df1.drop(df1.index[-4:])

# Create a Dash app
# app = Dash(__name__)

layout_14 = [
    html.Div([
        html.H1("Season A 2022_harvest area by crop type"),
        
        # Dropdown to select columns
        dcc.Dropdown(
            id='column-dropdown',
            options=[{'label': col, 'value': col} for col in df.columns],
            value='Maize',  # Default column to display
            style={'width': '50%'}
        ),
        

        # CSS styles
        dcc.Graph(id='bar-chart', style={'margin': '20px'}),
    ])
]

# Define the app layout
# app.layout = html.Div([
#     html.H1("Bar Chart with Dropdown"),
    
#     # Dropdown to select columns
#     dcc.Dropdown(
#         id='column-dropdown',
#         options=[{'label': col, 'value': col} for col in df.columns],
#         value='Maize'  # Default column to display
#     ),
    

#     # CSS styles
#     dcc.Graph(id='bar-chart', style={'margin': '20px'}),
# ])

# Define a callback function to update the bar chart based on the selected column
@app.callback(
    Output('bar-chart', 'figure'),
    Input('column-dropdown', 'value')
)
def update_bar_chart(selected_column):
    fig = px.bar(df, x='District/Crop category', y=selected_column, height=400)
    return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)