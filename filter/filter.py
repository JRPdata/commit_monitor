import re
from config.config import load_config


def filter_files(complete_file_list, file_filters):
    # Filter the list of complete file names based on the specified file filters
    filtered_files = []
    for file_name in complete_file_list:
        for file_filter in file_filters:
            if re.match(file_filter, file_name):
                filtered_files.append(file_name)
                break
    return filtered_files
