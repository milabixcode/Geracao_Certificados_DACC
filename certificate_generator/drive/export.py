import io
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from .setup import get_service


def export(file_id):
    """Download a Document file in PDF format.
    Args:
        real_file_id : file ID of any workspace document format file
    Returns : IO object with location
    """
    try:
        # create drive api client
        service = get_service()

        # pylint: disable=maybe-no-member
        request = service.files().export_media(
            fileId=file_id, mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}.")

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None

    return file.getvalue()
