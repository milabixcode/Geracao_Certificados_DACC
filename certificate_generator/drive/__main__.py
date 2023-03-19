from googleapiclient.errors import HttpError
from .setup import get_service


def main():
    service = get_service()

    try:
        # Call the Drive v3 API
        results = (
            service.files()
            .list(
                q="mimeType='application/vnd.google-apps.spreadsheet' and '1hnscQ5hzamzerYVoDduOGtYvIssNkqKw' in parents",
                fields="files(id, name, mimeType)",
            )
            .execute()
        )
        items: list = results.get("files", [])

        if not items:
            print("No files found.")
            return
        print("Files:")
        for item in items:
            print("{0} ({1}) {2}".format(item["name"], item["id"], item["mimeType"]))

        # dacc = next(filter(lambda item: item["name"] == "DACC", items))
        # dacc_media = service.files().get_media(fileId=dacc["id"])
        # print(inspect.getmembers(dacc_media))

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")


main()
