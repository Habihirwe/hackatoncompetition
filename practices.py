import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from app import app

# Provided data for Improved Seed
farmers_protect_landerrosion_data = {
    'District': ["Nyarugenge", "Gasabo", "Kicukiro", "Nyanza", "Gisagara", "Nyaruguru", "Huye", "Nyamagabe",
                 "Ruhango", "Muhanga", "Kamonyi", "Karongi", "Rutsiro", "Rubavu", "Nyabihu", "Ngororero", 
                 "Rusizi", "Nyamasheke", "Rulindo", "Gakenke", "Musanze", "Burera", "Gicumbi", "Rwamagana", 
                 "Nyagatare", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Bugesera"],
    'Farmers against erosion (Overall)': [98.7, 95.3, 85.1, 99, 100, 99.6, 97.7, 98.6, 98.1, 93.8, 96.1, 100, 98.8, 87.7, 98.6, 95.4, 97.6, 98.6, 100, 92.5, 93.7, 94.5, 99.4, 94, 72.8, 99, 99, 92.8, 96.6, 75.8],
    'Farmers against erosion (SSF)': [95.5, 94.4, 66.7, 100, 100, 100, 97.4, 100, 100, 97, 97.4, 100, 100, 87.3, 97.6, 100, 100, 100, 100, 89.7, 91.7, 95.9, 100, 86.4, 89.3, 100, 91.7, 93.8, 100, 71],
    'Farmers against erosion (SITE)': [100, 95.5, 87.8, 98.9, 100, 99.5, 97.8, 98.5, 97.9, 93, 95.8, 100, 98.6, 90, 100, 95.2, 97.1, 98.6, 100, 98.9, 94.4, 94, 99.3, 95.4, 64.2, 98.8, 100, 92.7, 96.3, 76.9]
}

# Provided data for Organic Fertilizer
mechanical_equipment_agriculture_activities_data = {
    'District': ["Nyarugenge", "Gasabo", "Kicukiro", "Nyanza", "Gisagara", "Nyaruguru", "Huye", "Nyamagabe",
                 "Ruhango", "Muhanga", "Kamonyi", "Karongi", "Rutsiro", "Rubavu", "Nyabihu", "Ngororero", 
                 "Rusizi", "Nyamasheke", "Rulindo", "Gakenke", "Musanze", "Burera", "Gicumbi", "Rwamagana", 
                 "Nyagatare", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Bugesera"],
    'Mechanical equipment (Overall)': [0, 0.9, 2.1, 0.3, 0, 0, 0.5, 0, 0, 0, 0.6, 0, 0, 0, 0.5, 0, 0.8, 0, 0, 0, 1.1, 0, 0.6, 0, 1.2, 1, 1.1, 0.6, 0.8, 0],
    'Mechanical equipment (SSF)': [0, 0, 0, 0, 0, 0, 2.6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.7, 0, 0, 0, 0, 0, 0],
    'Mechanical equipment (SITE)': [0, 1.1, 2.4, 0.4, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0, 1.2, 0, 1, 0, 0, 0, 1.5, 0, 0, 0, 1.9, 1.2, 1.2, 0.7, 0.9, 0]
}

# Provided data for Farmers Applied Organic Fertilizer
farmers_practiced_irrigation_data = {
    'District': ["Nyarugenge", "Gasabo", "Kicukiro", "Nyanza", "Gisagara", "Nyaruguru", "Huye", "Nyamagabe",
                 "Ruhango", "Muhanga", "Kamonyi", "Karongi", "Rutsiro", "Rubavu", "Nyabihu", "Ngororero", 
                 "Rusizi", "Nyamasheke", "Rulindo", "Gakenke", "Musanze", "Burera", "Gicumbi", "Rwamagana", 
                 "Nyagatare", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Bugesera"],
    'Practiced irrigation (Overall)': [66.7, 93.4, 72.3, 91.6, 66.7, 69.7, 90.5, 20.1, 90.1, 83.2, 93.9, 65.4, 2.5, 7.7, 4.8, 11.6, 83.5, 83, 96.3, 77.9, 4.1, 20.8, 89, 88.7, 56.8, 85, 95.8, 94.6, 74, 59.4],
    'Practiced irrigation (SSF)': [36.4, 94.4, 50, 85.7, 40.6, 55.6, 76.3, 37.5, 76.2, 57.6, 76.9, 46.7, 12.5, 0, 3.2, 40, 87.5, 66.7, 85.7, 2.1, 56.6, 20.6, 66.7, 68.2, 82.1, 60, 91.7, 93.8, 83.3, 45.2],
    'Practiced irrigation (SITE)': [78.6, 93.2, 75.6, 92, 75, 72.2, 93.4, 19.1, 91.6, 89.8, 98.6, 67.4, 1.4, 50, 7.1, 10.5, 82.5, 83.3, 100, 80.6, 3.6, 20.9, 93.4, 92.3, 43.4, 89.4, 96.4, 94.7, 72.9, 62.7]
}

farmers_practiced_agroforestry_data = {
    'District': ["Nyarugenge", "Gasabo", "Kicukiro", "Nyanza", "Gisagara", "Nyaruguru", "Huye", "Nyamagabe",
                 "Ruhango", "Muhanga", "Kamonyi", "Karongi", "Rutsiro", "Rubavu", "Nyabihu", "Ngororero", 
                 "Rusizi", "Nyamasheke", "Rulindo", "Gakenke", "Musanze", "Burera", "Gicumbi", "Rwamagana", 
                 "Nyagatare", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Bugesera"],
    'Practiced agroforestry (Overall)': [0, 0, 0, 5.5, 6.9, 4, 11.8, 15.3, 23.9, 3.6, 7, 34.8, 43.9, 31.4, 62.7, 45.5, 21.3, 44.6, 33.3, 30.3, 35.3, 28.7, 17.9, 7.9, 37.7, 23.3, 11.4, 24.4, 17.7, 15.2],
    'Practiced agroforestry (SSF)': [0, 16, 0, 5.5, 6.9, 4, 11.8, 15.3, 23.9, 3.6, 7, 34.8, 43.9, 31.4, 62.7, 45.5, 21.3, 44.6, 33.3, 30.3, 35.3, 28.7, 17.9, 7.9, 37.7, 23.3, 11.4, 24.4, 17.7, 15.2],
    'Practiced agroforestry (SITE)': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Load data
protect_landerrosion_df = pd.DataFrame(farmers_protect_landerrosion_data)
mechanical_equipment_agriculture_activities_df = pd.DataFrame(mechanical_equipment_agriculture_activities_data)
practiced_irrigation_df = pd.DataFrame(farmers_practiced_irrigation_data)
practiced_agroforestry_df = pd.DataFrame(farmers_practiced_agroforestry_data)

# Merge DataFrames
merged_df = pd.merge(protect_landerrosion_df, mechanical_equipment_agriculture_activities_df, on='District')
merged_df = pd.merge(merged_df, practiced_irrigation_df, on='District')
merged_df = pd.merge(merged_df, practiced_agroforestry_df, on='District')

# Reshape the DataFrame for nested bar chart
nested_df = pd.melt(merged_df, id_vars='District', var_name='Indicator', value_name='Value')

layout = [
    html.Div([
        html.H1("Percentage of Farmers by Agricultural practices"),

        # Dropdown for selecting data
        dcc.Dropdown(
            id='data-dropdown',
            options=[
                {'label': 'Farmers Against Erosion', 'value': 'Farmers against erosion'},
                {'label': 'Mechanical Equipment', 'value': 'Mechanical equipment'},
                {'label': 'Practiced Irrigation', 'value': 'Practiced irrigation'},
                {'label': 'Practiced Agroforestry', 'value': 'Practiced agroforestry'}
            ],
            value='Farmers against erosion',
            style={'width': '50%'}
        ),

        # Graph
        dcc.Graph(id='agricultural-graphh')
    ])
]

# # Dash app
# app = dash.Dash(__name__)

# # Define app layout
# app.layout = html.Div([
#     html.H1("Farmers Agricultural Practices"),

#     # Dropdown for selecting data
#     dcc.Dropdown(
#         id='data-dropdown',
#         options=[
#             {'label': 'Farmers Against Erosion', 'value': 'Farmers against erosion'},
#             {'label': 'Mechanical Equipment', 'value': 'Mechanical equipment'},
#             {'label': 'Practiced Irrigation', 'value': 'Practiced irrigation'},
#             {'label': 'Practiced Agroforestry', 'value': 'Practiced agroforestry'}
#         ],
#         value='Farmers against erosion',
#         style={'width': '50%'}
#     ),

#     # Graph
#     dcc.Graph(id='agricultural-graph')
# ])

# Define callback to update graph based on dropdown selection
@app.callback(
    Output('agricultural-graphh', 'figure'),
    [Input('data-dropdown', 'value')]
)
def update_graph(selected_data):
    # Determine the appropriate DataFrame based on the selected data
    df = merged_df[['District', selected_data + ' (Overall)', selected_data + ' (SSF)', selected_data + ' (SITE)']]

    # Reshape the DataFrame for nested bar chart
    nested_df = pd.melt(df, id_vars='District', var_name='Indicator', value_name='Value')

    # Create a nested bar chart
    fig = px.bar(nested_df, x='District', y='Value', color='Indicator', barmode='group',
                 labels={'Value': 'Percentage'},
                 title=f"{selected_data} by District",
                 height=600)

    return fig
if __name__ == '__main__':
    app.run_server(debug=True)
