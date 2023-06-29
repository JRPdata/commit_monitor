import os
import json

HISTORY_DIRECTORY = os.path.join(os.path.dirname(__file__), "historydata")

def initialize_history_directory():
    # Create the history directory if it doesn't exist
    if not os.path.exists(HISTORY_DIRECTORY):
        os.makedirs(HISTORY_DIRECTORY)

def load_last_updated(repo_id):
    # Load the last updated time for the given repo_id
    history_file = os.path.join(HISTORY_DIRECTORY, f"{repo_id}_last_updated.json")
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history_data = json.load(file)
            return history_data.get("last_updated")
    else:
        return None

def save_last_updated(repo_id, updated_time):
    # Save the last updated time for the given repo_id
    history_data = {"last_updated": updated_time}
    history_file = os.path.join(HISTORY_DIRECTORY, f"{repo_id}_last_updated.json")
    with open(history_file, "w") as file:
        json.dump(history_data, file)
