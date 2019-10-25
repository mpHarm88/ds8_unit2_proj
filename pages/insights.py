import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights


            """
        ),
	dcc.Markdown(
	    """
	   #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The inherent usefulness of my model comes from the fact that a Coach can gain better insight into how a player will perform before the season starts or during the season. A team can better understand the role a traded player will have during the season and what to expect when bringing them onto the team. By taking the statistic predicted by the model and comparing it with the actual results, a Coach can determine which players should potentially be played more or less. Looking to the right, we can see an interaction of two features (Age and Points(PTS)). As long as your ability to score points in regulation games, your age has little to no impact on your chances of playing during the season. 
	    """
	)
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.Img(src='assets/interact.png', className='img-fluid')
    ]
)

column3 = dbc.Col(
    [
	dcc.Markdown(
	    """
	    #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Taking a closer look at an individual prediction, we can determine what features played the most prominent role when deciding what percent of the season should be played. For example, Hilton Armstrong was a Center that played ~79% of the NBA season during the year he played.
	    """
	)
    ]
)

column4 = dbc.Col(
    [
	html.Img(src='assets/hilton.png', className='img-fluid', style={'margin-left':'150px'})
    ]
)

column5 = dbc.Col(
    [
	dcc.Markdown(
	"""
	#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; When we take a look below at Hiltons' Shapley value, we can see the model predicted he would play less the games than he did. The Shapley chart allows us to take a very close look at individual prediction to determine what were the reasons for a single prediction. We see that his age and total rebounds (TRB) contributed the most to a higher percent season played. His points (PTS), assists (AST), and steals (STL) were lower than what is normally seen among similar athletes, and the model predicted he should play less than he did.
	"""
	)
    ]
)

column6 = dbc.Col(
    [
	html.Img(src='assets/shap.png', className='img-fluid', style={'margin-left':'150px'})
    ]  
)

column7 = dbc.Col(
    [
	dcc.Markdown(
	"""
	#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There can be multiple reasons for why Hilton played more than predicted. He was a center, and positions like this are hard to find the appropriate player. He might have been the best candidate for the job even though his stats did not show that. There're limitations of what an NBA team is capable of, and sometimes finding the right player for each position can be one of those limitations. Hilton also could've played more if someone that regularly plays his position was injured, forcing the Coach to play Hilton not out of choice but out of necessity. Even though I've gone over one use case for this statistic, I believe more use cases can be applied.
	"""
	)
    ]

)
row1 = dbc.Row([column1,column2])
row2 = dbc.Row(column3)
row3 = dbc.Row(column4)
row4 = dbc.Row(column5)
row5 = dbc.Row(column6)
row6 = dbc.Row(column7)
layout = dbc.Row([row1,row2,row3,row4,row5,row6])








