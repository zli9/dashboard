'''
Define the HTML layout and run application.
'''
from dash import Dash, Input, Output
from layout import layout
import plotly.express as px
from numpy import linspace
from preprocess import data, years

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "World Population Dashboard"

app.layout = layout
app._favicon = 'icon.png'

@app.callback(
    Output("world-map", "figure"),
    Output("population-by-year", "figure"),
    Output("table-by-country", "columns"),
    Output("table-by-country", "data"),
    Input("country-filter", "value"),
    Input("year-btn", "value"),
)
def update_charts(country, year):
    filtered_data = data.query("country == @country")
    stat = filtered_data[['area', 'landArea', 'density', 'netChange', 'growthRate', 'worldPercentage']].transpose()
    stat.index = ['Area (km2)', 'Land area (km2)', 'Population density (km2)',
                  'Net change (%)', 'Growth rate (%)', 'World percentage (%)']
    stat.reset_index(inplace=True)
    stat.columns = ['Population Statistics', 'Values in 2023']
    time_series = filtered_data[[i for i in years]].transpose()
    time_series.index = years
    time_series.reset_index(inplace=True)
    time_series.columns = ['Years', 'Populations']

    world_map_figure = px.choropleth(data,
                                     locations="abbr",
                                     color=year,
                                     hover_name="country",
                                     labels={str(year): "population"},
                                     hover_data=['landArea', 'density', 'rank'],
                                     color_continuous_scale=px.colors.sequential.Mint)
    world_map_figure.update_geos(fitbounds="locations", visible=False)
    world_map_figure.update_layout(margin={"r":2,"t":15,"l":2,"b":15})

    ppl_figure = {
        "data": [
            {
                "x": time_series['Years'],
                "y": time_series['Populations'],
                "type": "lines",
                "hovertemplate": "%{x}<extra>%{y}</extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Population Trend",
                "x": 0.05,
                "xanchor": "left",
                "font": {
                    "family": "Lato",
                    # "color": "#076A72",
                    "size": 20,
                }
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#076A72"],
        }
    }

    stat_table_columns = [{'id': col, 'name': col} for col in stat.columns]
    stat_table_data = stat.to_dict('records')

    return world_map_figure, ppl_figure, stat_table_columns, stat_table_data


if __name__ == "__main__":
    app.run_server(debug=True)
