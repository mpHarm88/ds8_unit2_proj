import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

url = "https://raw.githubusercontent.com/mpHarm88/ds8_unit2_proj/master/nba-players-stats(1)/Seasons_Stats.csv"
season = pd.read_csv(url)
season = season[['Year','PTS', 'Player', 'G', 'Age', 'PF']]
season = season.rename(columns={'PTS':'Total Points', 'G':'Games Played', 'PF':'Personal Fouls'})

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## What does it take?

            This app helps determine how many games someone would play in an NBA season dependent on their prior stats.

            Learn if your over or under utilizing your bench based on their stats!

            Or plug in your own stats and see how you compare against the NBA!
            """
        ),
        dcc.Link(dbc.Button('Make my prediction!', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(season, x="Year", y="Total Points", hover_data=['Player', 'Age', 'Games Played', 'Personal Fouls'])
fig.update_layout(title='Shooting Your Shot - NBA Point Totals')
column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
