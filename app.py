import dash
from dash import Input, Output
import dash_mantine_components as dmc
import dash_ag_grid as dag
import polars as pl
import numpy as np


gridid = "grid"

app = dash.Dash(__name__)
app.clientside_callback(
    """
(id) => {
  dash_ag_grid.getApiAsync(id).then((api) => {
    api.addEventListener("cellFocused", (params) => {
      console.log(params);
    });
  });
  return dash_clientside.no_update;
};
    """,
    Output(gridid, "id"),
    Input(gridid, "id"),
)


height = 100
cols = ["A", "B", "C", "D"]
random_df = pl.DataFrame().with_columns(
    pl.lit(np.random.rand(height)).alias(col) for col in cols
)
col_defs = [dict(headerName=col, field=col, rowDrag=col == "A") for col in cols]
print(col_defs)
app.layout = dash.html.Div(
    dmc.MantineProvider(
        children=dag.AgGrid(
            id=gridid,
            rowData=random_df.to_dicts(),
            columnDefs=col_defs,
        ),
    )
)
if __name__ == "__main__":
    app.run()
