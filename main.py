import os
import pytube
from pytube import Playlist, YouTube

from helpers import progress_bar, complete_status


def download_playlist(url:str, quality:int):
    plist = Playlist(url)
    playlist_name = plist.title
    download_path = os.path.join(os.getcwd(), "downloads", playlist_name)

    for video in plist.videos:
        video.register_on_progress_callback(lambda stream, chunk, bytes_remaining  : progress_bar(stream, chunk, bytes_remaining))
        video.register_on_complete_callback(lambda stream, file_path : complete_status(stream, file_path))

        try:
            stream:pytube.Stream = video.streams.filter(res=f"{quality}p")[0]
        except IndexError as ie:
            print(f"Resolution: {quality}p not available!. Try other resolutions")
        if stream:
            stream.download(output_path=download_path)

def download_video(url:str, quality:int):
    download_path = os.path.join(os.getcwd(), "downloads")
    video = YouTube(
        url=url,
        on_progress_callback=lambda stream, chunk, bytes_remaining  : progress_bar(stream, chunk, bytes_remaining),
        on_complete_callback=lambda stream, file_path : complete_status(stream, file_path)
        )

    try:
        stream:pytube.Stream = video.streams.filter(res=f"{quality}p")[0]
    except IndexError as ie:
        print(f"Resolution: {quality}p not available!. Try other resolutions")
    if stream:
        stream.download(output_path=download_path)


if __name__ == "__main__":
    while True:
        print("\n****** Youtube Downloader ******")
        print("1.Youtube Video 2.Youtube Playlist 3.Exit")
        choice = int(input(": "))
        if choice == 1:
            link = input("Enter video url : ")
            quat = int(input("Enter video quality (720p) : "))
            download_video(url=link, quality=quat)

        elif choice == 2:
            link = input("Enter playlist url : ")
            quat = int(input("Enter video quality (720p) : "))
            download_playlist(url=link, quality=quat)

        elif choice == 3:
            break

        else:
            print("Invalid choice!")
            break
