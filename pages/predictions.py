import dash
import pandas as pd
import dash_daq as daq
from joblib import load
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Enter in Season Stats Below


            """

	),
	dcc.Input(
	    id='Age',
	    placeholder='Age',
	    type='number'
	),
	dcc.Input(
	    id='BLK',
	    placeholder='Blocks (BLK)',
	    type='number'
	),
	dcc.Input(
	    id='STL',
	    placeholder='Steals (STL)',
	    type='number'
	),
	dcc.Input(
	    id='AST',
	    placeholder='Assits (AST)',
	    type='number'
	),
	dcc.Input(
	    id='TRB',
	    placeholder='Total Rebounds (TRB)',
	    type='number'
	),
	dcc.Input(
	    id='PTS',
	    placeholder='Points (PTS)',
	    type='number'
	),
	dcc.Dropdown(
	    id='Pos',
	    options = [
		{'label': 'PF', 'value': 4},
		{'label': 'SG', 'value': 5},
		{'label': 'C', 'value': 2},
		{'label': 'SF', 'value': 3},
		{'label': 'PG', 'value': 1},
		{'label': 'G', 'value': 7},
		{'label': 'F', 'value': 8},
		{'label': 'F-C', 'value': 9},
		{'label': 'G-F', 'value': 12},
		{'label': 'F-G', 'value': 6},
		{'label': 'C-F', 'value': 10},
		{'label': 'C-PF', 'value': 13},
		{'label': 'PG-SG', 'value': 15},
		{'label': 'SF-SG', 'value': 19},
		{'label': 'PF-C', 'value': 11},
		{'label': 'SG-SF', 'value': 14},
		{'label': 'PF-SF', 'value': 16},
		{'label': 'SF-PF', 'value': 18}, 
		{'label': 'SF-PG', 'value': 20},
	    ],
	    placeholder='Position (POS)'
	)
    ],
    md=4,
)

column2 = dbc.Col(
    [
	html.H2('Percent of the season predicted to be played', className='mb-5'),
	html.Div(id='prediction-content', className='lead')    
    ] 	
)

@app.callback(
	Output('prediction-content', 'children'),
	[Input('Pos', 'value'), 
	 Input('BLK', 'value'), 
	 Input('STL', 'value'), 
	 Input('AST', 'value'), 
	 Input('Age', 'value'), 
	 Input('TRB', 'value'), 
	 Input('PTS', 'value')],
)

def predict(Pos, BLK, STL, AST, Age, TRB, PTS):
    df = pd.DataFrame(
	columns = ['Pos', 'BLK', 'STL', 'AST', 'Age', 'TRB', 'PTS'],
	data=[[Pos, BLK, STL, AST, Age, TRB, PTS]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'It is predicted that someone with these stats will play {round(y_pred,2)*100} of an NBA season'

layout = dbc.Row([column1, column2])
