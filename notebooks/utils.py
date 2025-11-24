import json

import os

import requests

from jsonpath_ng import jsonpath, parse

from github import Github

import base64

from more_itertools import chunked

from urllib.parse import urlparse

import traceback

import pandas as pd

import ast

from datetime import datetime

import matplotlib.pyplot as plt

import matplotlib.ticker as mtick

def load_file_as_json(file_path):
    """
    Given a file, returns its content as JSON.
    
    Args:
        file_path (str): The file path.
    """
    try:
        
        with open(file_path, 'r') as file:
            
            data = json.load(file)
            
            return data
    except Exception as e:
        
        print(f"Error loading file {file_path}: {e}")
        
        return {}

def load_url_as_json(url):
    """
    Given a file located at a given URL, returns its content as JSON.
    
    Args:
        url (str): Source url.
    """
    try:
        
        response = requests.get(url)

        if response.status_code == 200:
            
            data = response.json() 
            
            return data
            
        else:
            
            raise Exception(f"Error fetching data: {response.status_code}")
            
    except Exception as e:
        
        print(f"Error loading content from {url} as json: {e}")
        
        return {}

def get_validation_file_path(file_path):
    """Given a file path, generates the path to its validation file.
    
    Args:
        file_path (str): The file path.
    """
    filename = os.path.basename(file_path)
    
    filename = os.path.splitext(filename)[0]
    
    return filename

def get_jsonpath_match(content, jsonexpression, first_match=True):
    """
    Returns the part of content that matches the given jsonpath expression.
    
    Args:
        content (str): The content that contains potential matches.
        jsonexpression (str): The jsonpath expression to match.
        first_match (bool): Whether to return only the first match or a list of matches.
    """
    jsonpath_expr = parse(jsonexpression)

    matches =  [match.value for match in jsonpath_expr.find(content)]

    if not matches:

        return None

    return matches[0] if first_match else matches

def fetch_files_from_git_url(repo_url: str, folder_path: str, branch="main", download=False, download_path=""):
    """
    Fetches the contents of a GitHub repository (non-recursive).

    if download = True, downloads to the destination_directory.

    Args:
        repo_url (str): The full name of the repository.
        folder_path (str): The path to the folder within the repository.
        branch (str): The branch name.
        download(bool): Whether to download the repo.
        download_path (str): The local path to which files should be downloaded if download=True.
    """

    try:
        g = Github(os.getenv("GIT_TOKEN"))
        
        repo = g.get_user().get_repo(repo_url.split('/')[-1])
        
        contents = repo.get_contents(folder_path, ref=branch)

        if download and download_path:
        
            os.makedirs(download_path, exist_ok=True)

            for content_file in contents:
                
                file_path = os.path.join(download_path, content_file.name)
                
                if content_file.type == "dir":
                    
                    continue
    
                file_content = repo.get_contents(content_file.path, ref=branch)
                
                if file_content.content:
                    
                    decoded_content = base64.b64decode(file_content.content)
                    
                    with open(file_path, 'wb') as f:
                        
                        f.write(decoded_content)
                    
            print(f"Folder '{folder_path}' downloaded to '{download_path}' successfully using PyGithub.")
            
        return contents

    except Exception as e:
        
        print(f"Error fetching files from {repo_url}#{branch}: {e}")

def get_raw_github_url(repo_url: str, branch="main"):
    """Returns the corresponding raw github url."""

    try:

        repo_name, repo_user = repo_url.split('/')[-1], repo_url.split('/')[-2]

        return f"https://raw.githubusercontent.com/{repo_user}/{repo_name}/refs/heads/{branch}"

    except Exception as e:

        print(f"Error retrieving raw github repo for {git_repo}, branch {branch}: {e}")

        

def group_files_by_id(git_repo: str, subdir: str, branch="main"):
    """Groups files in this directory using the provided mappings"""
    try:
        def get_application_id(file: str):
            """Hardcoded logic that retrieves the application_id from the given file"""
            return os.path.basename(file).split('.')[0]

        def get_extension(file: str):
            """Hardcoded logic that retrieves the file extension from the given file"""
            return file.split('.')[1]
        
        raw_url = get_raw_github_url(git_repo, branch="main")

        # fetch files
        listing = fetch_files_from_git_url(git_repo, subdir, branch="main")

        
        # sort files
        listing = sorted([item.path for item in listing])

        # build clusters of 2
        groups = list(chunked(listing, 2))

        # only include valid clusters (files must refer to the same application_id)
        groups = [sorted(items, key=lambda item: get_extension(item)=="json") 
                  for items in groups 
                  if len(items)==2 and 
                  get_application_id(items[0]) == get_application_id(items[1])]

        # transform into {'application_id': xxx, 'application_data': xxx, 'image_path': xxx} format
        groups = [{"application_id": get_application_id(item[0]), 
                   "application_data": {"data": load_url_as_json(f"{raw_url}/{item[1]}")},
                   "image_path": f"{raw_url}/{item[0]}"}
                  for item in groups]
    
        return groups

    except Exception as e:

        print(f"Error grouping files from {git_repo}/{subdir}: {e}")

        traceback.print_exc()

def convert_to_submitted_fields(applications: list, patterns_file_path: str) -> list:
    """Uses static pattern matching rules to extract a list of dicts representing the submitted application fields."""

    try:

        # extract the static pattern matching rules
        patterns = load_file_as_json(patterns_file_path)

        submitted_data = []
    
        # extract the submitted application data
        for application in applications:

            application_data = application["application_data"]

            _application_data = {"application_id": application["application_id"], 
                                 "image_path": application["image_path"]}
            
            for key in patterns:

                _application_data[key] = get_jsonpath_match(application_data, patterns[key])

            submitted_data.append(_application_data)
                
        return submitted_data

    except Exception as e:

        print(f"Error extracting submitted data: {e}")

        traceback.print_exc()

###############################################################################################
# Report Generation
###############################################################################################

def data_report_prep(data: pd.DataFrame):
    """
    Transforms the columns of the dataframe to a format more suitable for the reports/visualizations that will be created.
    """
    transformed_df = data.copy()

    def jsonize(obj): 
        try:
            return json.loads(obj)
        except Exception as e:
            return {}

    transformed_df["extracted_data_dict"]= transformed_df["extracted_data"].apply(jsonize)

    transformed_df["eval_data_dict"]= transformed_df["eval_data"].apply(jsonize)

    extracted_df = pd.json_normalize(transformed_df["extracted_data_dict"]).add_prefix("extracted_")

    eval_df = pd.json_normalize(transformed_df["eval_data_dict"]).add_prefix("eval_")

    transformed_df = transformed_df.drop(columns=["extracted_data", "eval_data", "extracted_data_dict", "eval_data_dict"])

    return transformed_df.join(extracted_df).join(eval_df)
    

def generate_visualizatioms(reporting_df: pd.DataFrame, target_dir: str):
    """Generates visualizations from the given dataframe."""
    
    groups = reporting_df['model_name'].unique()
    
    category_cols = [col for col in reporting_df.columns if col != "model_name"]
    
    fig, axes = plt.subplots(len(category_cols), len(groups), figsize=(12, 30), sharey=True)
    
    fig.suptitle('Accuracy by Model and Field')
    
    for i, group in enumerate(groups):
    
        for j, col in enumerate(category_cols):
            
            # Filter data for the current group
            group_data = reporting_df[reporting_df['model_name'] == group]
        
            # Calculate value counts (frequencies) of the categorical variable
            category_cols = [col for col in reporting_df.columns if col != "model_name"]
                    
            category_counts = (group_data[col].value_counts(normalize=True) * 100).sort_index()
            
            category_counts.plot.bar(ax=axes[j, i])
            
            axes[j, i].set_title(group.removeprefix("openrouter/"))
            
            axes[j, i].set_xlabel(col.removeprefix("eval_"))
            
            axes[j, i].set_ylabel('Percentage')
            
            axes[j, i].tick_params(axis='x', rotation=45)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent title overlap
    
    plt.savefig(f"{target_dir}/barplot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png") 
    
    plt.show()

def generate_csv_report(data: pd.DataFrame, target_dir: str):
    """Generates a CSV file from the given dataframe."""
    
    os.makedirs(target_dir, exist_ok=True)
    
    data.to_csv(f"{target_dir}/dataset_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

def generate_jsonl_report(data: pd.DataFrame, target_dir: str):
    """Generates a jsonl file from the given dataframe."""
    
    os.makedirs(target_dir, exist_ok=True)
    
    data.to_json(f"{target_dir}/dataset_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl", orient='records', lines=True)
