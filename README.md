# Commit File Monitor

Watch for file changes in public GitHub repositories using local tools, leveraging GitHub's RSS feeds (to reduce requests) and GitHub's API. This tool allows you to filter commits' files based on regular expressions and uses Ntfy to notify you of changes, including the file names.

You can even do almost all of this self-hosted on a local network: with GitHub API access, a locally running Ntfy server, this Python code running as a service on a local machine, and the Ntfy app on your wi-fi enabled phone, you can receive notifications on your phone and watch for specific files/folders being modified in public GitHub repositories.

## Requirements

- Python 3
- Dependencies:
  - feedparser (install using `pip install feedparser`)
- Ntfy
  - For self-hosting Ntfy, refer to the [Ntfy self-hosting documentation](https://docs.ntfy.sh/install/)

## Configuration

Before running the Commit File Monitor, make sure to modify the following configuration files:

1. `conf/ntfy_url`: Update this file with the URL of your (locally) running Ntfy server.
2. `conf/github_token`: With your GitHub API token, add it to this file (personal access tokens are the easiest to generate: Your github profile page->Settings->Developer Settings (at the bottom)).
3. `conf/poll_interval_min`: Change file this to how often (in minutes) you want to poll GitHub's RSS feeds for each repo to check for updates. Default is 5 min.
4. `conf/repos/REPO_ID.conf`: REPO_ID should be a short name for the repo (this will appear as the topic for notifications). The format of the file must have as the first line the github URL such as 'https://www.github.com/leela-zero/leela-zero' and the second line and the lines beyond must be regular expressions (separated by newlines) that compile with `re.compile()`. These are what you will use to match the file/folder names you want to watch for. Do not add quotes around the regular expressions as it will already be interpreted as a string.

Additionally, you can modify the `repos/test.conf` file as an example to specify the repositories you want to monitor. Feel free to create additional `.conf` files for more repositories, and delete the `test.conf` when you are done.

## Usage

1. Install the required dependencies by running: `pip install -r requirements.txt`.
2. Modify the configuration files for this project (see above).
3. Start the Ntfy server.
4. Run the Commit File Monitor: `python3 commit_monitor.py`.
5. Subscribe on your phone to your ntfy server, where the topic will be the name of the repo file in conf/repos/. For example, if your ntfy_url is `http://192.168.1.101` and your repo conf is named `leela-zero.conf`, the url will be for the subscription is `http://192.168.1.101/leela-zero`. You can also change the default server in the app to match yours and make it easier to only enter the topic `leela-zero`.
