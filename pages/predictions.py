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
	    type='number',
	    value=""
	),
	dcc.Input(
	    id='BLK',
	    placeholder='Blocks (BLK)',
	    type='number',
	    value=""
	),
	dcc.Input(
	    id='STL',
	    placeholder='Steals (STL)',
	    type='number',
	    value=""
	),
	dcc.Input(
	    id='AST',
	    placeholder='Assits (AST)',
	    type='number',
	    value=""
	),
	dcc.Input(
	    id='TRB',
	    placeholder='Total Rebounds (TRB)',
	    type='number',
	    value=""
	),
	dcc.Input(
	    id='PTS',
	    placeholder='Points (PTS)',
	    type='number',
	    value=""
	),
	dcc.Dropdown(
	    id='Pos',
	    options = [
		{'label': 'PF', 'value': 'PF'},
		{'label': 'SG', 'value': 'SG'},
		{'label': 'C', 'value': 'C'},
		{'label': 'SF', 'value': 'SF'},
		{'label': 'PG', 'value': 'PG'},
		{'label': 'G', 'value': 'G'},
		{'label': 'F', 'value': 'F'},
		{'label': 'F-C', 'value': 'F-C'},
		{'label': 'G-F', 'value': 'G-F'},
		{'label': 'F-G', 'value': 'F-G'},
		{'label': 'C-F', 'value': 'C-F'},
		{'label': 'C-PF', 'value': 'C-PF'},
		{'label': 'PG-SG', 'value': 'PG-SG'},
		{'label': 'SF-SG', 'value': 'SF-SG'},
		{'label': 'PF-C', 'value': 'PF-C'},
		{'label': 'SG-SF', 'value': 'SG-SF'},
		{'label': 'PF-SF', 'value': 'PF-SF'},
		{'label': 'SF-PF', 'value': 'SF-PF'},
		{'label': 'SG-PF', 'value': 'SG-PF'},
		{'label': 'C-SF', 'value': 'C-SF'},
		{'label': 'SF-PG', 'value': 'SF-PG'},
		{'label': 'PG-SF', 'value': 'PG-SF'},
		{'label': 'SG-PG', 'value': 'SG-PG'},
	    ],
	    value = 'Position',
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
