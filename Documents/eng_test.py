import os

print()

def files_in_dir(top_dir, end):
    """Returns list of path of files with ending end \
    in top_dir and all subdirs."""
    path_list = []
    for root, dirs, files in os.walk(str(top_dir)):
        for file_ in files:
            if file_.endswith(str(end)):
                path_list.append(os.path.join(root, file_))
    return path_list
