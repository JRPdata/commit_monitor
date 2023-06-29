import requests
import time
from datetime import datetime
from history.history import load_last_updated

def fetch_commits(repo_url, repo_id):
    # Fetches the commit history for a given repository URL using the GitHub API
    owner, project = extract_owner_project(repo_url)
    api_url = f"https://api.github.com/repos/{owner}/{project}/commits"
    token = load_github_token()
    last_updated = load_last_updated(repo_id)

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "Since": last_updated
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        raise Exception(f"Failed to fetch commits. Status code: {response.status_code}. API_URL: {api_url}")


def load_github_token():
    # Load the GitHub token from conf/github_token file
    with open("conf/github_token", "r") as file:
        token = file.read().strip()
    return token


def extract_owner_project(repo_url):
    # Extracts the owner and project from the repository URL
    url_parts = repo_url.split("/")
    owner = url_parts[-2]
    project = url_parts[-1]
    return owner, project


def get_commit_list(repo_url, repo_id):
    commits = fetch_commits(repo_url, repo_id)
    commit_list = [commit['sha'] for commit in commits]
    return commit_list


def fetch_commit(repo_url, commit_sha):
    owner, project = extract_owner_project(repo_url)
    api_url = f"https://api.github.com/repos/{owner}/{project}/commits/{commit_sha}"
    token = load_github_token()
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        commit_data = response.json()
        return commit_data
    else:
        raise Exception(f"Failed to fetch commit. Status code: {response.status_code}")


def get_files_from_commit_json(commit_data):
    files = commit_data['files']
    file_list = [file['filename'] for file in files]
    return file_list


def get_complete_file_list(repo_url, repo_id):
    commit_list = get_commit_list(repo_url, repo_id)
    complete_file_list = []

    # Rate limit variables
    requests_per_minute = 10
    seconds_per_minute = 60
    interval = seconds_per_minute / requests_per_minute

    # Loop through commit list
    for i, commit_sha in enumerate(commit_list):
        # Fetch commit data for each commit
        commit_data = fetch_commit(repo_url, commit_sha)
        # Get file list from commit data
        file_list = get_files_from_commit_json(commit_data)
        # Append file list to complete file list
        complete_file_list.extend(file_list)

        # Rate limiting delay
        if i < len(commit_list) - 1:
            time.sleep(interval)

    # Remove duplicates from the file list
    complete_file_list = list(set(complete_file_list))

    return complete_file_list
