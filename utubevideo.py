from pytube import YouTube
from tqdm import tqdm


def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        video_size = stream.filesize

        # Create a progress bar
        progress_bar = tqdm(total=video_size, unit='bytes', unit_scale=True)

        # Download the video with progress monitoring
        stream.download(output_path, filename="video.mp4", skip_existing=False)
        progress_bar.close()

        message = "Video downloaded successfully!"
    except Exception as e:
        message = "Error: " + str(e)
    return message

