# import the classes for accessing DSS objects from the recipe
import dataiku
import pandas as pd
import os
import time
from itertools import islice
import openpyxl
# Import the helpers for custom recipes
from dataiku.customrecipe import *
from dataiku import recipe

#
# The configuration is simply a map of parameters, and retrieving the value of one of them is simply:
#
regex = get_recipe_config()['regex']
regexpression = get_recipe_config()['regexpression']

#
# Pull list of datasets already in project
#
client = dataiku.api_client()
project = client.get_project(dataiku.default_project_key())
existing_datasets=project.list_datasets()

#
# Get files in folder
#
folder_id = get_input_names_for_role('input_folder')[0].split(".")[1]
folder = project.get_managed_folder(folder_id)
folder_info = folder.list_contents()
path = folder_info["folderPath"]
df = pd.DataFrame(folder_info["items"]).sort_values(by='lastModified', ascending=False).reset_index()

#
# Process filenames with Regex
#
if regex:
    expression = re.compile(regexpression)
    match_df = df
    match_df["keep"] = df["path"].str.match(expression)
    match_df = match_df.loc[match_df.keep, :]

    fileName=match_df["path"][0]

else:
    fileName=df['path'][0]


# For outputs, the process is the same:
tableName = get_output_names_for_role('main_output')[0].split(".")[1]

file_df = pd.read_excel(path+fileName, engine='openpyxl')

output_dataset = dataiku.Dataset(tableName)
output_dataset.write_with_schema(file_df)    