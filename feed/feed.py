import feedparser
from datetime import datetime
from history.history import load_last_updated

def fetch_rss_feed(repo_url):
    # Fetches the RSS feed for a given repository URL and returns the feed data
    rss_url = f"{repo_url}/commits.atom"
    feed = feedparser.parse(rss_url)
    return feed

def get_latest_update(feed):
    entries = feed["entries"]
    if entries:
        latest_entry = entries[0]
        updated = latest_entry["updated"]
        return updated
    return None

def check_for_update(repo_id, repo_url, last_updated):
    # Compares the last updated time of a repository identified by its repo_id
    # with the latest update in the RSS feed. Returns True if an update is detected, False otherwise.
    feed = fetch_rss_feed(repo_url)
    latest_update = get_latest_update(feed)

    if latest_update:
        latest_update_time = datetime.strptime(latest_update, "%Y-%m-%dT%H:%M:%SZ")
        # Compare last_updated with stored last_updated for repo_id
        if last_updated is not None:
            last_updated_time = datetime.strptime(last_updated, "%Y-%m-%dT%H:%M:%SZ")
            if latest_update > last_updated:
                return latest_update  # Return the new (updated) timestamp
            else:
                return None
        else:
            return latest_update
    else:
        return None
