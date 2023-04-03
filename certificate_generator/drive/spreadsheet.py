from functools import reduce

SPREADSHEET_TYPE = "application/vnd.google-apps.spreadsheet"


def select_spreadsheets(file_tree):
    files = []

    for node in file_tree["fileList"]:
        files += node["files"]

    spreadsheets = []

    for file in files:
        if is_spreadsheet(file):
            spreadsheets.append(file)

    return spreadsheets


def is_spreadsheet(file):
    return file["mimeType"] == SPREADSHEET_TYPE
