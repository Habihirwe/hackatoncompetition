import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

# Load your data from the Excel file
data = pd.read_excel("SAS 2022_Tables.xlsx", sheet_name="Table 1", skiprows=2)
df = pd.DataFrame(data)
df = df.drop(df.index[-1:])
df = df.drop(columns=['Unnamed: 0'])
# Create a Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Pie Chart from Excel Data"),

    dcc.Graph(
        id='pie-chart',
        config={'displayModeBar': False},
        style={
            'width': '40%',  # Adjust the width to control the size
            'float': 'left',  # Float the graph to the left side
            'margin-left': '20px',  # Adjust the left margin
            'margin-top': '20px',  # Adjust the top margin
        }
    ),

    dbc.Button("DataFrame", id="show-data-button", color="primary", className="mr-1"),
    html.Div(id="data-display"),
    
    dcc.Store(id='data-store', data=df.to_json(orient='split')),
    dcc.Store(id='display-data', data=True)
])

# Define a callback function to update the pie chart
@app.callback(
    Output('pie-chart', 'figure'),
    Input('pie-chart', 'id')
)
def update_pie_chart(id):
    fig = px.pie(df, values='Percentage share', names='Land cover class name',
                 hover_data=['Area (Ha)'], labels={'Area (Ha)': 'Area (Ha)'})
    return fig

# Callback to toggle the display of the DataFrame when the button is clicked
@app.callback(
    Output('data-display', 'children'),
    Output('display-data', 'data'),
    Input('show-data-button', 'n_clicks'),
    Input('data-store', 'data'),
    Input('display-data', 'data')
)
def toggle_data_display(n_clicks, data, display_data):
    if n_clicks:
        display_data = not display_data
        if display_data:
            df = pd.read_json(data, orient='split')
            data_to_show = html.Pre(df.to_string(), style={'white-space': 'pre-wrap'})
        else:
            data_to_show = None
        return data_to_show, display_data
    return None, display_data

if __name__ == '__main__':
    app.run_server(debug=True)
