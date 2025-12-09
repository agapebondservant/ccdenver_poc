import json

import os

import requests

from jsonpath_ng import jsonpath, parse

from github import Github

import base64

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
        
        return None

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
        
        return None

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

def download_directory_from_git_url(repo_url, folder_path, destination_path, branch="main"):
    """
    Downloads a specific folder from a GitHub repository.

    Args:
        token (str): Your GitHub Personal Access Token.
        repo_url (str): The full name of the repository.
        branch (str): The branch name.
        folder_path (str): The path to the folder within the repository.
        destination_path (str): The local path where the folder should be downloaded.
    """
    g = Github(os.getenv("GITHUB_TOKEN"))
    
    repo = g.get_user().get_repo(repo_url.split('/')[-1]) # Adjust for organization repos if needed

    try:
        contents = repo.get_contents(folder_path, ref=branch)
        
        os.makedirs(destination_path, exist_ok=True)

        for content_file in contents:
            
            file_path = os.path.join(destination_path, content_file.name)
            
            if content_file.type == "dir":
                
                continue

            file_content = repo.get_contents(content_file.path, ref=branch)
            
            if file_content.content:
                
                decoded_content = base64.b64decode(file_content.content)
                
                with open(file_path, 'wb') as f:
                    
                    f.write(decoded_content)
                    
        print(f"Folder '{folder_path}' downloaded to '{destination_path}' successfully using PyGithub.")

    except Exception as e:
        
        print(f"Error downloading folder {folder_path} from {repo_url}: {e}")
