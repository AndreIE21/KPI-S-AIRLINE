import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

import dash_auth


# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}

January = pd.read_csv('kpi_2101.csv')
February = pd.read_csv('kpi_2102.csv')
March = pd.read_csv('kpi_2103.csv')
April = pd.read_csv('kpi_2104.csv')

df = pd.concat([January, February, March, April], ignore_index=True)
df = df.drop(columns='Unnamed: 0')
df = df.rename(index={0: 'January', 1: 'February', 2: 'March', 3: 'April'})
df = df.transpose()

kpi3 = df.iloc[2:6]
kpi4 = df.iloc[23:27]
kpi5 = df.iloc[10:23]

external_stylesheets = [dbc.themes.BOOTSTRAP]


def create_dash_application(flask_app):

    app = dash.Dash(server=flask_app, external_stylesheets=external_stylesheets, name="Dashboard", url_base_pathname="/dash/")
    app.title = "AIREBI"
    auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
    app.layout = html.Div([

    dbc.Row(
        [
            dbc.Col(html.Div(dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': i, 'value': i} for i in df.columns
                ],
                value='January'
            ), style={'margin-top': '20px'}), width=2
            ),

            dbc.Col(html.Div(id='critical-incidences',
                             className='card-container'), width=1.8),
            dbc.Col(html.Div(id='total-incidences',
                    className='card-container'), width=1.8),
            dbc.Col(html.Div(id='incidences-P1-meeting-SLA',
                             className='card-container'), width=1.8),
            dbc.Col(html.Div(id='Percent-of-incidences-P1-meeting-SLA',
                             className='card-container'), width=1.8),
            dbc.Col(html.Div(id='incidences-P1-not-meeting-SLA',
                             className='card-container'), width=1.8),
            dbc.Col(html.Div(id='Percent-of-incidences-P1-not-meeting-SLA',
                             className='card-container'), width=1.8),
        ]
    ),

    html.Div([dbc.Row([

        dbc.Col(html.Div(dcc.Graph(
            id='kpi3-graph')
        ), width=4
        ),


        dbc.Col(html.Div(dcc.Graph(
            id='kpi4-graph')
        ), width=4
        ),

        dbc.Col(html.Div(dcc.Graph(
            id='bar-graph')
        ), width=4
        )
    ])

    ]),


])


    @app.callback(
        Output('critical-incidences', 'children'),
        Input('dropdown', 'value')
    )
    def critical_incidences(month):
        return 'Critical Incidences: ' + str(df.loc['Kpi1', month])


    @app.callback(
        Output('total-incidences', 'children'),
        Input('dropdown', 'value')
    )
    def total_incidences(month):
        return 'Total Incidences: ' + str(df.loc['Kpi2', month])


    @app.callback(
        Output('incidences-P1-meeting-SLA', 'children'),
        Input('dropdown', 'value')
    )
    def incidences_meeting_SLA(month):
        return 'Incidences P1 Meeting SLA: ' + str(df.loc['Kpi6', month])


    @app.callback(
        Output('Percent-of-incidences-P1-meeting-SLA', 'children'),
        Input('dropdown', 'value')
    )
    def percent_incidences_meeting_SLA(month):
        return 'Percent of P1 Meeting SLA: ' + str(df.loc['Kpi7', month])


    @app.callback(
        Output('incidences-P1-not-meeting-SLA', 'children'),
        Input('dropdown', 'value')
    )
    def incidences_not_meeting_SLA(month):
        return 'Incidences P1 Not Meeting SLA: ' + str(df.loc['Kpi8', month])


    @app.callback(
        Output('Percent-of-incidences-P1-not-meeting-SLA', 'children'),
        Input('dropdown', 'value')
    )
    def percent_incidences_not_meeting_SLA(month):
        return 'Percent of P1 Not Meeting SLA: ' + str(df.loc['Kpi9', month])


    @app.callback(
        Output('kpi3-graph', 'figure'),
        Input('dropdown', 'value')
    )
    def updtae_kpi3_pie(month):
        fig = px.pie(kpi3, values=month, names=kpi3.index,
                    title='Raised Incidences', hole=.3)
        fig.update_layout(paper_bgcolor='#1f2c56',
                        plot_bgcolor='#1f2c56', font_color='white')
        return fig


    @app.callback(
        Output('kpi4-graph', 'figure'),
        Input('dropdown', 'value')
    )
    def updtae_kpi4_pie(month):
        fig = px.pie(kpi4, values=month, names=kpi4.index,
                    title='Backlog Incidences', hole=.3)
        fig.update_layout(paper_bgcolor='#1f2c56',
                        plot_bgcolor='#1f2c56', font_color='white')
        return fig


    @app.callback(
        Output('bar-graph', 'figure'),
        Input('dropdown', 'value')
    )
    def updtae_bar_graph(month):
        fig = px.bar(kpi5, y=month, x=kpi5.index,
                    title='Incidences per cause', color=kpi5.index)
        fig.update_layout(paper_bgcolor='#1f2c56', showlegend=False,
                        plot_bgcolor='#1f2c56', font_color='white')
        fig.update_yaxes(showgrid=False)
        return fig

    return app 
