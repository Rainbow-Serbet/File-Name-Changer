from os import read
from tkinter import *
from tkinter import filedialog
import webbrowser


# 도움말 클릭시 README 링크 열기
def readme_url_connect():
    readme_url = (
        "https://github.com/Rainbow-Serbet/File-Name-Changer/blob/main/README.md"
    )
    webbrowser.open(readme_url)


# 파일추가 버튼 클릭시 파일 선택하는 창 띄워줌
def fileopen():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="이름을 변환할 파일 선택",
        filetypes=(("PNG files", "*.png"),
            ("JPEG files", "*.jpeg"),
            ("JPG files", "*.jpg"),
            ("all files", "*.*"),),
    )


def Save():
    filename = filedialog.asksaveasfilename(
        initialdir="/",
        title="Select file",
        filetypes=(
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpeg"),
            ("JPG files", "*.jpg"),
            ("all files", "*.*"),
        ),
    )
