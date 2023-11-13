from dash import Dash, dcc, html, Input, Output
from dash import Dash
from practices import layout
from table_14 import layout_14
from app import app
from table_39 import layout_39
from table_61 import layout_61
from piechart import pielayout

alllayout=[
     html.Div([
        html.H1("Seasonal Agricultural survey 2022 Dash Board",style={'color':'blue', 'font-weight':'bold','display':'flex','justify-content':'center', 'font-size':'30px','align-item':'center','text-decoration': 'underline','position':'relative'}),
    * pielayout,
    * layout_14,
    * layout,
    * layout_39,
    * layout_61,
       
    ],style={'display':'flex', 'flex-direction':'column'})
   
]

app.layout = html.Div(alllayout)
# Create a Dash app

# app = Dash(__name__)

if __name__ == '__main__':
    app.run_server(debug=True)