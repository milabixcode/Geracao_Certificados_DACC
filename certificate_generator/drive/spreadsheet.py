from functools import reduce

SPREADSHEET_TYPE = "application/vnd.google-apps.spreadsheet"


def select_spreadsheets(file_tree):
    return list(
        filter(_only_spreadsheets, reduce(_combine_files, file_tree["fileList"], []))
    )


def _combine_files(first, second):
    return first + second["files"]


def _only_spreadsheets(file):
    return file["mimeType"] == SPREADSHEET_TYPE
