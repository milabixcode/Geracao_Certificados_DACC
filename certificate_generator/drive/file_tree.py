from certificate_generator.drive.setup import get_creds
from getfilelistpy import getfilelist
import json


def store_file_tree(folder_id, file_name):
    result = getfilelist.GetFileList(
        {
            "oauth2": get_creds(),
            "id": folder_id,
            "fields": "files(name, id, mimeType)",
        }
    )

    with open(file_name, "w") as f:
        json.dump(result, f)


def load_file_tree(file_name):
    with open(file_name, "r") as f:
        return json.load(f)
