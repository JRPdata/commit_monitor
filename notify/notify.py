import subprocess

def create_notification_message(filtered_files):
    # Creates a notification message based on the repository ID and filtered list of files
    message = "\n".join(filtered_files)
    return message

def send_notification(repo_id, ntfy_url, message):
    # Sends the notification message to the desired destination using the ntfy program
    command = ['ntfy', 'publish', f'{ntfy_url}/{repo_id}', message]
    subprocess.run(command, check=True)
