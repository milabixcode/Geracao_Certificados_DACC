from certificate_generator.drive.spreadsheet import select_spreadsheets
from .file_tree import store_file_tree, load_file_tree


events_folder_id = "1kayHxaxggYsOWoFF2SJHrBAjK-kTDnfK"
file_tree_file = "file-tree.json"

# TODO make this run based on parameters passed on cli
# For now, turn this to `True`` to refresh local metadata
if False:
    store_file_tree(events_folder_id, file_tree_file)

file_tree = load_file_tree(file_tree_file)
spreadsheets = select_spreadsheets(file_tree)

print(len(spreadsheets))
print(file_tree["totalNumberOfFiles"])
