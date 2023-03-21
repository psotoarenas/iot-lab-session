# import all dependencies
from cgitb import text
from textwrap import fill
import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
from datetime import datetime
from os.path import isfile

# Auxiliary functions

def get_data(url):
    # Read data from a URL
    return pd.read_csv(url)

def get_daily_data():
    return

def plot_cases(data, country):
    cases_per_country = data[data["Country"]==country] 
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x = cases_per_country['Date_reported'],
        y = cases_per_country['New_cases'],
        line = dict(color = 'firebrick', width = 4),
        name = 'daily_cases'
        )
    )
    fig.update_layout(title = 'Daily cases over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Cases'
                      )
    return fig

def plot_cum_cases(data, country):
    cases_per_country = data[data["Country"]==country] 
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x = cases_per_country['Date_reported'],
        y = cases_per_country['Cumulative_cases'],
        line = dict(color = 'firebrick', width = 4),
        fill = 'tozeroy'
        )
    )
    fig.update_layout(title = 'Cumulated cases over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Cases'
                      )
    return fig

def geo_summary(data):
    last_day_reported = data['Date_reported'].iloc[-1]
    last_report_overall = data[data['Date_reported']==last_day_reported]
    fig = px.scatter_geo(
        last_report_overall, 
        locations='Country', 
        locationmode='country names', 
        color='WHO_region', 
        hover_name='Country', 
        size='Cumulative_cases', 
        projection='natural earth'
        )
    fig.update_layout(
        title = f'Global COVID-19 Cases (Last Updated: {last_day_reported})'
        ),
    return fig

def top_countries(cases_data, vaccination_data):
    last_day_reported = cases_data['Date_reported'].iloc[-1]
    last_report_overall = cases_data[cases_data['Date_reported']==last_day_reported]
    fig = make_subplots(
    rows = 3, cols = 1,
    # specs=[
    #         [    None, None, None,               {"type": "bar", "colspan":1}, None, None],
    #         [    None, None, None,              {"type": "bar", "colspan":1}, None, None],
    #         [    None, None, None,               {"type": "bar", "colspan":1}, None, None],
    #       ]
    )

    # Top 10 Countries with recently discovered cases
    top_ten_cases_daily = last_report_overall.nlargest(n=10, columns=['New_cases'])
    fig.append_trace(go.Bar(
        x=top_ten_cases_daily['Country_code'],
        y=top_ten_cases_daily['New_cases'],
        name= "Confirmed Cases",
        ), 
        row=1, col=1
    )
    
    # Top 10 Countries with highest daily deaths
    top_ten_deaths_daily = last_report_overall.nlargest(n=10, columns=['New_deaths'])
    fig.append_trace(go.Bar(
        x=top_ten_deaths_daily['Country_code'],
        y=top_ten_deaths_daily['New_deaths'],
        name= "Confirmed Deaths",
        ), 
        row=2, col=1
    )
    
    # Top 10 Countries with highest number of people vaccinated
    top_ten_vaccinated = vaccination_data.nlargest(n=10, columns=['PERSONS_FULLY_VACCINATED'])
    fig.append_trace(go.Bar(
        x=top_ten_vaccinated['COUNTRY'],
        y=top_ten_vaccinated['PERSONS_FULLY_VACCINATED'],
        name= "Fully Vaccinated",
        ), 
        row=3, col=1
    )
    
    fig.update_layout(
        title_text=f"Top 10 Countries in daily cifers (Last Updated: {last_day_reported})",
        )

    return fig


#  official WHO data
# cases_who_path = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
cases_who_path = './data/WHO-COVID-19-global-data.csv'
# vaccination_who_path = 'https://covid19.who.int/who-data/vaccination-data.csv'
vaccination_who_path = './data/vaccination-data.csv'

cases = get_data(cases_who_path)
vaccination = get_data(vaccination_who_path)



countries = cases["Country"].unique()
countries.sort()



# Visualization
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)   

app.layout = html.Div(
    id = 'parent', 
    children = [
        html.H1(id = 'H1', 
        children = 'Coronavirus (COVID-19) Data', 
        style = {'textAlign':'center',} # 'marginTop':40,'marginBottom':40
        ),
        html.H3('Overall Numbers'),
        html.Div(children=[
            html.H5('Cumulated Cases'),
            dcc.Graph(id='geo_summary', figure=geo_summary(cases))
        ],
        style={'width': '49%', 'display': 'inline-block'}),
        html.Div(children=[
            html.H5('Daily Cases'),
            dcc.Graph(id='top_countries', figure=top_countries(cases, vaccination))
        ],
        style={'width': '49%', 'display': 'inline-block'}),            
        
        html.H5('Country'),
        dcc.Dropdown(
            id='country',
            options=[{'label':c, 'value':c} for c in countries],
            value='Belgium'
        ),
        dcc.Graph(id='daily_cases'),
        dcc.Graph(id='cum_cases')   
    ]
)

@app.callback(
    Output(component_id='daily_cases', component_property='figure'),
    Output(component_id='cum_cases', component_property='figure'),
    Input(component_id='country', component_property='value')
)
def update_plots(country):
    # Function for creating figures showing per country daily and cumulated cases over time
    data = get_data(cases_who_path)
    daily_fig = plot_cases(data=data, country=country)
    cum_fig = plot_cum_cases(data=data, country=country)
    return daily_fig, cum_fig

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True) # opens a port on http://0.0.0.0:8050/