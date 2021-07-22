from os import read
from tkinter import *
import webbrowser



#도움말 클릭시 README 링크 열기 
def readme_url_connect():
    readme_url = "https://github.com/Rainbow-Serbet/File-Name-Changer/blob/main/README.md"
    webbrowser.open(readme_url)