import os
import re

CONFIG_DIRECTORY = "conf/repos"

def load_notify():
    # Load ntfy_url from conf/ntfy_url
    with open("conf/ntfy_url", "r") as file:
        ntfy_url = file.read().strip().rstrip("/")

    return ntfy_url

def load_config(repo_id):
    """
    Load the configuration data for a repository.

    Args:
        repo_id (str): The unique identifier for the repository.

    Returns:
        dict: The configuration data for the repository.
    """
    config_file = os.path.join(CONFIG_DIRECTORY, f"{repo_id}.conf")
    with open(config_file, "r") as file:
        lines = file.readlines()

    url = lines[0].strip().rstrip("/")
    filters = [re.compile(line.strip()) for line in lines[1:]]

    return {
        "url": url,
        "filters": filters
    }

def initialize_repositories():
    """
    Initialize the repositories by loading the configuration data.

    Returns:
        list: A list of tuples containing the repository ID and configuration data.
    """
    repositories = []
    config_files = [file for file in os.listdir(CONFIG_DIRECTORY) if file.endswith(".conf")]
    for file in config_files:
        repo_id = file.split(".")[0]
        config_data = load_config(repo_id)
        repositories.append((repo_id, config_data))
    return repositories
