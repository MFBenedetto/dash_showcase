import dash
import dash_table
import pandas as pd
import dash_core_components as dash_core
import dash_html_components as dash_html
from dash.dependencies import Input, Output
import base64
import io

# starting app layout
app.layout = dash_html.Div([
    # upload button to take csv files
    dash_core.Upload(id='upload_data',
               children=dash_html.Div(['Drag and Drop or ',
                                  dash_html.A('Select Files')
                                  ]),
               style={'width': '100%',
                      'height': '60px',
                      'lineHeight': '60px',
                      'borderWidth': '1px',
                      'borderStyle': 'dashed',
                      'borderRadius': '5px',
                      'textAlign': 'center',
                      'margin': '10px'
                      },
               multiple=False),
    # Div to store json serialized dataframe
    dash_html.Div(id='json_df_store', style={'display':'none'}),
    # a 'Div' to return table output to
    dash_html.Div(id='dataframe_output'),
])

@app.callback(Output('json_df_store', 'children'),
              [Input('upload_data', 'contents'),
               Input('upload_data', 'filename')])
def load_df(content, filename):
    if content:
        # Modify the read_csv callback part
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)

        try:
            if 'csv' in filename:

                # Assume that the user uploaded a CSV file
                input_data  = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

                info_dataframe = pd.DataFrame(data={
                                              "data_types": input_data.dtypes,
                                              "blanks_count": input_data.isna().sum(),
                                              "unique_count": input_data.nunique()
                                                   })

                # adding index as a row
                info_dataframe.reset_index(level=0, inplace=True)
                info_dataframe.rename(columns={'index':'col_name'}, inplace=True)

                info_dataframe['data_types'] = info_dataframe['data_types'].astype(str)

                return info_dataframe.to_json(date_format='iso', orient='split')

        except Exception as e:
            #print(e)
            return pd.DataFrame(data={'Error': e}, index=[0]).to_json(date_format='iso', orient='split')



# callback to take and output the uploaded file
@app.callback(Output('dataframe_output', 'children'),
              [Input('json_df_store', 'children')])
def update_output(json_df):

   info_dataframe = pd.read_json(json_df, orient='split')

   data = info_dataframe .to_dict("rows")
   cols = [{"name": i, "id": i} for i in info_dataframe .columns]

   child = dash_html.Div([
                dash_table.DataTable(
                                id='table',
                                data=data, 
                                columns=cols,
                                style_cell={'width': '50px',
                                            'height': '30px',
                                            'textAlign': 'left'}
                                      )
                           ])
    return child

# running the app now
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)