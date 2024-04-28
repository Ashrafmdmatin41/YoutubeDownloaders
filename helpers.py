import pytube

def progress_bar(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.2f}').format(current*100)
    progress = int(40*current)
    status = '█' * progress + '-' * (40 - progress)
    print(f"Downloading: {status} {percent} %")

def complete_status(stream, file_path):
    print(f"DOWNLOADED : {stream.title}\nMB : {stream.filesize_mb}")
    print(f"Saved to : {file_path}")