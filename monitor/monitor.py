import os
#from config.config import load_config
import config
from config import config
from feed import feed
from github_api import github_api
from filter import filter
from history import history
from notify import notify

def monitor_repositories():
    repositories = config.initialize_repositories()
    for repo in repositories:
        repo_id = repo[0]
        config_data = repo[1]
        repo_url = config_data['url']
        last_updated = history.load_last_updated(repo_id)

        new_last_updated = feed.check_for_update(repo_id, repo_url, last_updated)
        if new_last_updated:
            # Update detected, fetch complete file list
            complete_file_list = github_api.get_complete_file_list(repo_url, repo_id)
            # Filter files
            filtered_files = filter.filter_files(complete_file_list, config_data['filters'])

            if filtered_files is not None and filtered_files != []:
                # Create notification message
                message = notify.create_notification_message(filtered_files)

                # Send notification
                ntfy_url = config.load_notify()
                notify.send_notification(repo_id, ntfy_url, message)

            # Update last_updated timestamp in history
            history.save_last_updated(repo_id, new_last_updated)
