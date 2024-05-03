import pytube

def progress_bar(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.2f}').format(current*100)
    bar_length = 20
    progress = int(bar_length*current)
    status = '█' * progress + '-' * (bar_length - progress)
    print(f"Downloading: {status} {percent} %", flush=True)

def complete_status(stream, file_path):
    print(f"DOWNLOADED : {stream.title}\nMB : {stream.filesize_mb}")
    print(f"Saved to : {file_path}")