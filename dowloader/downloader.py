import pytube

class YouTubeDownloader:
    def __init__(self, url):
        self.url = url
        self.video = pytube.YouTube(url)

    def get_streams(self):
        video_streams = self.video.streams.filter(progressive=True)
        audio_streams = self.video.streams.filter(only_audio=True)
        return video_streams, audio_streams

    def download(self, stream):
        stream.download()

def main():
    url = input("Digite a URL do vídeo: ")
    downloader = YouTubeDownloader(url)
    streams, audio_streams = downloader.get_streams()

    print("Vídeos:")
    for i, stream in enumerate(streams):
        print(f"{i+1}. {stream}")

    print("\nÁudios:")
    for i, stream in enumerate(audio_streams):
        print(f"{i+1}. {stream}")

    choice = int(input("Escolha o tipo de download (vídeo ou áudio): "))
    if choice == 1:
        video_choice = int(input("Escolha a resolução do vídeo: "))
        downloader.download(streams[video_choice - 1])
    else:
        audio_choice = int(input("Escolha a qualidade do áudio: "))
        downloader.download(audio_streams[audio_choice - 1])

if __name__ == "__main__":
    main()