from os import pathsep
from tkinter import *
from tkinter import filedialog


def add_file():
    files = filedialog.askopenfilenames(
        title="파일을 선택하세요",
        filetypes=(("PNG파일", "*.png"), ("모든 파일", "*.*")),
        initialdir="C:/",
    )


window = Tk()
window.title("파일 이름변환 프로그램")
window.geometry("800x400")


# 파일 프레임
file_frame = Frame(window)
file_frame.pack(fill="x")


button_add_file = Button(file_frame, padx=5, pady=3, width=14, text="파일추가")
button_add_file.pack(side="left")

button_del_file = Button(file_frame, padx=5, pady=3, width=14, text="선택 파일삭제")
button_del_file.pack(side=("left"))


# 리스트 프레임
list_frame = Frame(window)
list_frame.pack()

Scrollbar = Scrollbar(list_frame)
Scrollbar.pack(side="right", fill="y")

list_file = Listbox(
    list_frame,
    selectmode="extended",
    width=30,
    height=20,
    yscrollcommand=Scrollbar.set,
)
list_file.pack(side="left", fill="both", expand=True)
Scrollbar.config(command=list_file.yview)


# 저장 경로 설정
path_frame = LabelFrame(window, text="저장경로")
path_frame.pack(fill="x")

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

button_dest_path = Button(path_frame, text="찾아보기", width=10)
button_dest_path.pack(side="right")


window.resizable(False, False)
window.mainloop()
