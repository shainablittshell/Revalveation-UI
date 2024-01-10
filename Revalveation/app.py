from dash import Dash, html
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

current = pd.read_csv("TestDataI.csv")
voltage = pd.read_csv("TestDataV.csv")
data = current.merge(voltage, on="Time")

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Scatter(x=data["Time"], y=data["Current_A"], name="Current (A)"), secondary_y=False)
fig.add_trace(go.Scatter(x=data["Time"], y=data["Voltage_A"], name="Voltage (V)"), secondary_y=True)
fig.update_layout(title_text="Current and Voltage")
fig.update_yaxes(title_text="Current (A)", secondary_y=False)
fig.update_yaxes(title_text="Voltage (V)", secondary_y=True)
fig.update_xaxes(title_text="Time")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Revalveation"), sm=1, align="start"),
        dbc.Col(dbc.Button("Refresh"), sm=2, align="end")
    ], justify="between"),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Row(html.H3("Details")),
            dbc.Row(html.B("Board ID")),
            dbc.Row(html.Div("0xEE3355AA")),
            dbc.Row(html.B("Firmware")),
            dbc.Row(html.Div("1.0.0-r1")),
            html.Br(),
            dbc.Row(html.H3("IP Address")),
            dbc.Row(html.B("IPv4 Address")),
            dbc.Row(html.Div(dbc.Input(placeholder="xxx.xxx.xxx.xxx"))),
            dbc.Row(html.B("Subnet Mask")),
            dbc.Row(html.Div(dbc.Input(placeholder="255.255.255.0"))),
            dbc.Row(html.B("Gateway")),
            dbc.Row(html.Div(dbc.Input(placeholder="xxx.xxx.xxx.xxx"))),
            dbc.Row(html.Div(dbc.Button("Add"), style={"margin-top": "8px"}))
        ], sm=3),
        dbc.Col([
            dcc.Graph("data", figure=fig)
        ], sm=6),
        dbc.Col([
            dbc.Row(html.H3("Confidence Score")),
            dbc.Row(html.Div("Opening")),
            dbc.Row(html.H3("82%")),
            dbc.Row(html.Div("Closing")),
            dbc.Row(html.H3("59%"))
        ], sm=3)
    ]),
    dbc.Row([ 
        dbc.Col([
            html.H3("Statistics"),
            dbc.Row([
                dbc.Col([
                    html.Div("Up Time"),
                    dbc.Row(html.B("117 seconds")),
                    html.Br(),
                    dbc.Row(html.Div("Max Time to Open")),
                    dbc.Row(html.B("32 seconds")),
                    html.Br(),
                    dbc.Row(html.Div("Max Time to Close")),
                    dbc.Row(html.B("54 seconds"))
                ]),
                dbc.Col([
                    html.Div("Latency"),
                    dbc.Row(html.B("2 Seconds")),
                    html.Br(),
                    dbc.Row(html.Div("Min Time to Open")),
                    dbc.Row(html.B("19 seconds")),
                    html.Br(),
                    dbc.Row(html.Div("Min Time to Close")),
                    dbc.Row(html.B("48 seconds"))
                ]),
                dbc.Col([
                    html.Div("Actuations"),
                    dbc.Row(html.B("12")),
                    html.Br(),
                    dbc.Row(html.Div("Average Time to Open")),
                    dbc.Row(html.B("25 seconds")),
                    html.Br(),
                    dbc.Row(html.Div("Average Time to Close")),
                    dbc.Row(html.B("51 seconds"))
                ])
            ])
        ], width=6)
    ], justify="center")
])

if __name__ == "__main__":
    app.run(debug=True, port="8050")
