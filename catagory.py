#!/usr/bin/env python3
# Group Assignment 2 - S25-NBB-Group-2
# Author: Chanho Lee
# Assigned work: File type categorization

'''
Prerequisite:
1) Use either 'du', 'fd' or 'find' linux command
2) Output should display file extension types: filename.fileextension 
'''

import os
import subprocess

def categorize_files_by_type(file_paths):
    """
    Categorizes files by their extension and lists filenames.

    Expected Output:
        dict: {extension name: [filename.extension]}
    """
    categorized = {}
    for absolute_path in file_paths:
        filename = os.path.basename(absolute_path) # Extract just the filename from the full path
        if '.' in filename: 
            ext = filename.split('.')[-1] # If the filename contains an '.' = extension, get the extension
        else:
            ext = 'no_extension' # Otherwise no catagorize as no extension

        # heck if key exists
        if ext not in categorized:
            categorized[ext] = [] # If the detected extension hasn't been listed, create one
        categorized[ext].append(filename) # Add the filename to the list for its extension

    return categorized

def categorize_files_find(path: str, extension_filter: str = None) -> dict:
    """
    Uses `find` to locate files and categorizes them by extension.

    Returns:
        dict: Extension -> [filenames]
    """
    absolute_path = os.path.expanduser(path) # Requires full directory path
    
    # Build the shell command to find files
    if extension_filter:
        cmd = ["find", absolute_path, "-type", "f", "-name", f"*.{extension_filter}"] # If a specific extension is provided, search only for files matching that extension
    else:
        cmd = ["find", absolute_path, "-type", "f"] # Otherwise, search for all files

    try:
        # Run the find command and capture its output
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = result.stdout.strip() # Remove any whitespace from the output
        if not output: # If no files exists
            return {} # An empty dictionary
        file_paths = output.split('\n') # Split the output into a list of file paths
        return categorize_files_by_type(file_paths)
    except subprocess.CalledProcessError as e: # If the find command fails (e.g., invalid path), print an error message
        print("Error running find:", e)
        return {} # An empty dictionary