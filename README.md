## Introduction
This custom recipe reads a Dataiku [Mangaged Folder](https://knowledge.dataiku.com/latest/courses/folders/managed-folders.html) and imports the most recent file. The current version only supports Excel files.

## Basic Usage
1. Create a new Managed Folder
2. Modify the Settings

![Example settings](/Managed_Folder_Settings.png "managed_folder")
3. Select the Plugin Recipe from the Actions Menu (also displayed when the managed folder is selected from the flow)

![Plugin Location](/Recipe_Location.png "plugin")

4. Optional: Process Filenames with Regex to subset the file list to import last modified from.

## Additional Configuration
There may be additional configuration required if the [User Isolation Framework](https://doc.dataiku.com/dss/latest/user-isolation/index.html) is enabled at your site. In this case, you may see an error related to the dssuser not having the proper permissions to modify the file. You must modify the [dataiku-security](https://doc.dataiku.com/dss/latest/user-isolation/initial-setup.html#additional-setup-for-local-filesystem-access) file in order to allow Dataiku to access the directories of the file system. Add the location your Managed Folder is pointing to to this file in order to allow the recipe to run.
