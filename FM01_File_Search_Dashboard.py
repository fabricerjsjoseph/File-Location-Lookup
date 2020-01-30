import dash
import dash_table
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from dash.dash import no_update
import pandas as pd
from datetime import date
import webbrowser

def create_app():
    # importing csv into DataFrame
    df=pd.read_csv('FM02_File_Search_df.csv')

    folder_list=df['Root_Folder'].unique()


    # Create Dash object
    app = dash.Dash(__name__)


    # Creating app layout
    app.layout=html.Div([
    html.Div([html.H1('File Path Lookup'),
    dcc.Dropdown(
    id='folder-dropdown',
    options=[{'label': k, 'value': k} for k in folder_list],
    multi=True,
    value=folder_list),
    html.H3('Search by Keyword:'),
    dcc.Input(id='keyword-box',placeholder='Enter keyword seperated by comma',value='',type='text',style={'width':'40%'})]),
    html.Div([
    dash_table.DataTable(
            id='datatable-interactivity',
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            data=df.to_dict('records'),
            style_header={'backgroundColor': 'rgb(221, 65, 36)','fontWeight': 'bold','color':'white'},
            style_data_conditional=[{'if': {'row_index': 'odd'},'backgroundColor': 'rgb(204, 204, 255)'}],
            style_cell={'textAlign': 'left'},
            style_as_list_view=True,
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable=False,
            row_selectable=False,
            row_deletable=False,
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 10)], style={'width': '80%','font-family':'Arial Black','margin-left':'auto','margin-right':'auto',
            'display': 'inline-block'})
            ])



    @app.callback(Output(component_id='datatable-interactivity', component_property='data'),
    [Input(component_id='keyword-box', component_property='value'),Input(component_id='folder-dropdown', component_property='value')])
    def filter_table(keywords,folders):
        keywords_split=keywords.split(',')
        keywords_split_upper=[word.upper() for word in keywords_split]
        keywords_regex= '|'.join(keywords_split_upper)
        df_filter=df.File_Path.str.upper().str.contains(keywords_regex)
        filtered_df=df[df_filter]
        df_folder_filter=filtered_df.Root_Folder.isin(folders)
        filtered_df=filtered_df[df_folder_filter]
        return filtered_df.to_dict('records')

    return app

# Assign dash object to app
app=create_app()

# Register webbrowser
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))

# Run app
if __name__ == '__main__':
        webbrowser.get('chrome').open_new('http://127.0.0.1:8050/')
        app.run_server(debug=False)
