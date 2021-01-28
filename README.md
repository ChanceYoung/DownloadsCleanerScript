# DownloadsCleanerScript
*An installation of Python is required to run this script*

This is a script adapted from the open-source solution provided by geeksambhu.
The original script can be found at: https://geeksambhu.github.io/python/2018/08/09/organize-your-downloads-directory-mess.html

This is a python script designed to organize your downloads folder into subdirectories when run. 
My modifications:
Created a new "Extracted" folder that will be populated with any directories created from extracting folders found in the "Zipped" folder.
Created a procedure to delete all files or folders not contained within the curated list of organized folders or the .ini layout file provided by default by the Microsoft File system. 

To run:
1. Clone this repo
2. Extract the zip to desired location
3. Navigate to the folder where the script is located using cmd prompt and the *cd* command e.g. "> cd C:\Users\Chance\Documents\Coding Projects"
4. Type "python clean_dir.py /Users/Chance/Downloads/" *remember the last "/" after Downloads

Expected Result:
Your Downloads should be organized into the following folders:
-Photos
-Docs
-TextFiles
-Zipped
-Extracted
-Book
-ExeFiles
-Audio

