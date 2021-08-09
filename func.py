from os import read
from tkinter import *
from tkinter import filedialog
import webbrowser

#도움말 클릭시 README 링크 열기 
def readme_url_connect():
    readme_url = "https://github.com/Rainbow-Serbet/File-Name-Changer/blob/main/README.md"
    webbrowser.open(readme_url)

#파일추가 버튼 클릭시 파일 선택하는 창 띄워줌
def fileopen():
    filename = filedialog.askopenfilename(initialdir="/", title= "이름을 변환할 파일 선택", filetypes= (("PPTX files", "*.pptx"), ("all files", "*.*")))

def Save():
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("PPTX files", "*.pptx"),("all files", "*.*")))

#저장경로 - 찾아보기 버튼 클릭시 저장경로 열어줌
def directoryopen():
    global dir_path
    dir_path = filedialog.askdirectory(initialdir="/",title='폴더를 선택하세요')
    print(dir_path)
    



