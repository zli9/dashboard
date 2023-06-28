from dash import html, dcc, dash_table
from preprocess import years, countries

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(children="World Population Analysis", className="header-title"),
                html.P(
                    children="Display the world population map, "
                             "and provide interactive analysis of population data by countries.",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.H1(children="World Population Map", className="card-title"),
        html.Div(
            children=[
                html.Div(children="Select a year:", className="menu-title"),
                dcc.RadioItems(
                    id="year-btn",
                    inputClassName="btn-check",
                    options=[
                        {
                            "label": html.Span(years[0], style={'font-size': 15, 'padding-right': 10}),
                            "value": years[0]
                        },
                        {
                            "label": html.Span(years[1], style={'font-size': 15, 'padding-right': 10}),
                            "value": years[1]
                        },
                        {
                            "label": html.Span(years[2], style={'font-size': 15, 'padding-right': 10}),
                            "value": years[2]
                        },
                        {
                            "label": html.Span(years[3], style={'font-size': 15, 'padding-right': 10}),
                            "value": years[3]
                        },
                        {
                            "label": html.Span(years[4], style={'font-size': 15, 'padding-right': 10}),
                            "value": years[4]
                        },
                        {
                            "label": html.Span(years[5], style={'font-size': 15, 'padding-right': 10}),
                            "value": years[5]
                        },
                        {
                            "label": html.Span(years[6], style={'font-size': 15, 'padding-right': 10}),
                            "value": years[6]
                        },
                    ],
                    value=2023,
                    inline=True,
                ),
                dcc.Graph(
                    id="world-map",
                    config={"displayModeBar": True},
                ),
            ],
            className="card",
        ),
        html.H1(children="Analytical Card", className="card-title"),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Select or type a country:", className="menu-title"),
                        dcc.Dropdown(
                            id="country-filter",
                            options=[
                                {
                                    "label": c.title(),
                                    "value": c,
                                }
                                for c in countries
                            ],
                            value="Germany",
                            clearable=False,
                            searchable=True,
                            className="dropdown",
                        ),
                        html.Br(),
                        html.Div(
                            children=[
                                dash_table.DataTable(
                                    id="table-by-country",
                                    editable=False,
                                    style_data={'text-align': 'right', 'padding': 8, 'font-family': 'Lato'},
                                    style_header={'text-align:': 'right', 'padding': 10, 'font-family': 'Lato'},
                                ),
                            ],
                            className="table",
                        ),
                    ],
                    className="single-chart",
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            id="population-by-year",
                            config={"displayModeBar": False},
                        ),
                    ],
                    className="single-chart",
                ),
            ],
            className="charts-wrapper",
        ),
    ],
)
