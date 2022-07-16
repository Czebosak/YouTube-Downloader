from pytube import YouTube
from os import startfile, path
import PySimpleGUI as gui

gui.theme("gray gray gray")

layout = [
    [gui.Text("Enter the link to the video you want to download")],
    [gui.InputText()],
    [gui.HorizontalSeparator()],
    [gui.Text("Destination folder:"), gui.In(size=(25,1), enable_events=True ,key='-FOLDER-'), gui.FolderBrowse()],
    [gui.Submit(button_text="Download")]
]

window = gui.Window(title="YouTube Video Downloader", layout=layout, icon="icon.ico")

while True:
    event, values = window.read()
    print(event, values)

    if event == gui.WIN_CLOSED:
        print(event, "exiting")
        break
    elif event == "Download":
        try:
            path = path.realpath(values["Browse"])
        except:
            pass
        else:
            link = values[0]
            try:
                yt = YouTube(link)
            except:
                pass
            else:
                print(f"Downloading {yt.title}...")

                video = yt.streams.get_highest_resolution()
                video.download(values["Browse"])

                print("Video downloaded!\nOpening file explorer...")
                startfile(path)
