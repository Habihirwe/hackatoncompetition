import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from app import app


# The provided data for Improved Seed
improved_seed_data = {
    'District': ["Nyarugenge", "Gasabo", "Kicukiro", "Nyanza", "Gisagara", "Nyaruguru", "Huye", "Nyamagabe",
                 "Ruhango", "Muhanga", "Kamonyi", "Karongi", "Rutsiro", "Rubavu", "Nyabihu", "Ngororero", 
                 "Rusizi", "Nyamasheke", "Rulindo", "Gakenke", "Musanze", "Burera", "Gicumbi", "Rwamagana", 
                 "Nyagatare", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Bugesera"],
    'Improved Seed (Overall)': [58.3,60.9,47.6,59.9,45.3,81.5,58,63.9,54.1,66.1,53.5,60.5,58.4,25.3,54.9,73.3,50.9,70.6,82.8,70.6,61.8,67.5,74.8,38.2,33,63.4,40.5,33.3,23,37.9],
    'Improved Seed (SSF)': [58.3,60.9,47.6,59.9,45.3,81.5,58,63.9,54.1,66.1,53.5,60.5,58.4,25.3,54.9,73.3,50.9,70.6,82.8,70.6,61.8,67.5,74.8,38.2,33,63.4,40.5,33.3,23,37.9],
    'Improved Seed (LSF)': [0,60,66.7,57.1,62.5,100,79,100,38.5,100,80,100,0,66.7,0,0,30,87.5,80,0,0,0,100,50,27.8,66.7,64.3,100,70,42.4]
}

# The provided data for Organic Fertilizer
organic_fertilizer_data = {
    'District': ["Nyarugenge", "Gasabo", "Kicukiro", "Nyanza", "Gisagara", "Nyaruguru", "Huye", "Nyamagabe",
                 "Ruhango", "Muhanga", "Kamonyi", "Karongi", "Rutsiro", "Rubavu", "Nyabihu", "Ngororero", 
                 "Rusizi", "Nyamasheke", "Rulindo", "Gakenke", "Musanze", "Burera", "Gicumbi", "Rwamagana", 
                 "Nyagatare", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Bugesera"],
    'Organic Fertilizer Land Size (Overall)': [52.2,59.7,55.9,56.1,42.6,77.9,56.8,61.4,49.8,61.7,48.9,59,54.9,24.5,53.6,71.3,48.4,68.6,78.1,70.5,59.8,66.5,71.9,36.5,30.9,59.0,37.7,30.8,21.5,35.7],
    'Organic Fertilizer Land Size (SSF)': [52.2,59.7,55.9,56.1,42.6,77.9,56.8,61.4,49.8,61.7,48.9,59,54.9,24.5,53.6,71.3,48.4,68.6,78.1,70.5,59.8,66.5,71.9,36.5,30.9,59.0,37.7,30.8,21.5,35.7],
    'Organic Fertilizer Land Size (LSF)': [0,50,71.4,69.2,62.5,81.8,69,100,31.6,100,57.1,100,0,42.9,0,0,23.1,77.8,61.5,0,0,0,50,26.8,35.3,62,31,66.7,52.1,42.5]
}

# The provided data for Farmers Applied Organic Fertilizer
farmers_organic_fertilizer_data = {
    'District': ["Nyarugenge", "Gasabo", "Kicukiro", "Nyanza", "Gisagara", "Nyaruguru", "Huye", "Nyamagabe",
                 "Ruhango", "Muhanga", "Kamonyi", "Karongi", "Rutsiro", "Rubavu", "Nyabihu", "Ngororero", 
                 "Rusizi", "Nyamasheke", "Rulindo", "Gakenke", "Musanze", "Burera", "Gicumbi", "Rwamagana", 
                 "Nyagatare", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Bugesera"],
    'Farmers Applied Organic Fertilizer (Overall)': [47.8,60,45.9,53,45.7,76.3,55.4,63.6,48.7,60.8,52.1,63.8,65,28.2,60.5,77.9,45,70.1,83.4,75,61.3,66.5,71.5,42.5,31.6,58.7,36.1,32,27.7,33.8],
    'Farmers Applied Organic Fertilizer (SSF)': [47.8,59.5,46.7,53,44.2,76.2,54.9,63.6,48.4,60.6,51.8,63.7,65,28.1,60.5,77.9,46.3,69.8,83.5,75,61.3,66.5,71.5,43,32.4,58.4,37.1,30.4,26.6,33],
    'Farmers Applied Organic Fertilizer (LSF)': [0,82.8,10.8,52.9,59.1,98.3,70.6,100,58.3,100,94,100,0,64.3,0,0,22.7,99.8,65.2,0,0,0,13.9,15,5.6,64.8,10.4,77.9,73.2,57.3]
}




# Load data
improved_seed_df = pd.DataFrame(improved_seed_data)
organic_fertilizer_df = pd.DataFrame(organic_fertilizer_data)
farmers_organic_fertilizer_df = pd.DataFrame(farmers_organic_fertilizer_data)

# Merge DataFrames
merged_df = pd.merge(improved_seed_df, organic_fertilizer_df, on='District')
merged_df = pd.merge(merged_df, farmers_organic_fertilizer_df, on='District')

# Reshape the DataFrame for nested bar chart
nested_df = pd.melt(merged_df, id_vars='District', var_name='Indicator', value_name='Value')

# Dash app
# app = dash.Dash(__name__)

layout_39 = [
    html.Div([
        html.H1("Season B 2022 use of organic fertilizers by farmer category",style={'font-weight':'bold', 'font-size':'30px'}),
        
        # Dropdown for selecting data
        dcc.Dropdown(
            id='data-dropdownn',
            options=[
                {'label': 'Improved Seed', 'value': 'Improved Seed'},
                {'label': 'Organic Fertilizer', 'value': 'Organic Fertilizer'},
                {'label': 'Farmers Applied Organic Fertilizer', 'value': 'Farmers Applied Organic Fertilizer'},
            ],
            value='Improved Seed',
            style={'width': '50%'}
        ),
        
        # Graph
        dcc.Graph(id='agricultural-graph')
    ])
]

# Define app layout
# app.layout = html.Div([
#     html.H1("Agricultural Data Visualization"),
    
#     # Dropdown for selecting data
#     dcc.Dropdown(
#         id='data-dropdown',
#         options=[
#             {'label': 'Improved Seed', 'value': 'Improved Seed'},
#             {'label': 'Organic Fertilizer', 'value': 'Organic Fertilizer'},
#             {'label': 'Farmers Applied Organic Fertilizer', 'value': 'Farmers Applied Organic Fertilizer'},
#         ],
#         value='Improved Seed',
#         style={'width': '50%'}
#     ),
    
#     # Graph
#     dcc.Graph(id='agricultural-graph')
# ])

# Define callback to update graph based on dropdown selection
@app.callback(
    Output('agricultural-graph', 'figure'),
    [Input('data-dropdownn', 'value')]
)
def update_graph(selected_data):
    # Determine the appropriate DataFrame based on the selected data
    if selected_data == 'Improved Seed':
        df = improved_seed_df
        title = 'Improved Seed Data'
    elif selected_data == 'Organic Fertilizer':
        df = organic_fertilizer_df
        title = 'Organic Fertilizer Data'
    else:
        df = farmers_organic_fertilizer_df
        title = 'Farmers Applied Organic Fertilizer Data'
    
    # Reshape the DataFrame for nested bar chart
    nested_df = pd.melt(df, id_vars='District', var_name='Indicator', value_name='Value')
    
    # Create the nested bar chart
    fig = px.bar(nested_df, x='District', y='Value', color='Indicator', barmode='group', title=title)
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
