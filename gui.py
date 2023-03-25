import PySimpleGUI as sg
import PySimpleGUI
import model_downloader

urls = 'urls'
download = "Download :D"
sg.theme("DefaultNoMoreNagging")

layout = [
    [sg.Text('Enter model URLs separated by a comma :]')],
    [sg.Text('This will open a bunch of tabs, sorry :[')],
    [sg.Input(key=urls)],
    [sg.Button(download)]
]

window = sg.Window('Model Downloader', layout)

i = 2

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == download:
        model_urls = values[urls].split(",")
        model_downloader.download_models(model_urls)
        print(model_urls)

window.close()
