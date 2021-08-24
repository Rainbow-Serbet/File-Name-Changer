from tkinter import *
import webbrowser
from func import *

"""
    상속 구분 개요  #다중주석처리 - 헷갈려서 만듬
    window
        file_inout_frame
            button_frame
                button_add_file
                button_dell_file
                button_help
            file_frame
                list_frame
                    list_file
            save_path_frame
                path_frame
                    txt_dest_path
                    button_dest_path
        run_frame
            name_frame
                name_button
                name_textbox
        setting_frame
"""

window = Tk()
window.iconbitmap("icon.ico")
window.title("파일 이름변환기 Ver1.0")
window.geometry("500x600")
window.resizable(False, False)

# button_help_command = readme_url_connect()


# 파일 입출력 프레임
file_inout_frame = Frame(window, background="yellow")  # 프레임의 색은 파티션 구분을 위함
file_inout_frame.pack(side="top", fill="both")


## 버튼 프레임(파일 입출력 프레임 내부에 선언)
button_frame = Frame(file_inout_frame)
button_frame.pack(side="top", anchor="nw", fill="x")


### 버튼 라벨
button_add_file = Button(
    button_frame, padx=5, pady=3, width=14, text="파일추가", command=fileopen
)
button_add_file.pack(side="left")

button_del_file = Button(button_frame, padx=5, pady=3, width=14, text="선택 파일삭제")
button_del_file.pack(side=("left"))

button_help = Button(
    button_frame, padx=5, pady=3, width=14, text="도움말", command=readme_url_connect
)
button_help.pack(side="right")

## 파일 프레임(파일 입출력 프레임 내부에 선언)
file_frame = Frame(file_inout_frame)
file_frame.pack(side="top", fill="both")

### 파일 표시, 스크롤바
list_frame = Frame(file_frame)
list_frame.pack(side="left", fill="both")

Scrollbar = Scrollbar(list_frame)
Scrollbar.pack(side="right", fill="both")

list_file = Listbox(
    list_frame, selectmode="extended", width=80, height=20, yscrollcommand=Scrollbar.set
)
list_file.pack(side="left", fill="both", expand=True)
Scrollbar.config(command=list_file.yview)

## 저장경로 프레임
save_path_frame = Frame(file_inout_frame)
save_path_frame.pack(side="top", fill="both")


### 저장경로 설정, 버튼
path_frame = LabelFrame(save_path_frame, text="저장경로")
path_frame.pack(side="left", fill="both")

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipadx=140, ipady=4)

button_dest_path = Button(path_frame, text="찾아보기", width=10)
button_dest_path.pack(side="right")


# 작동 프레임
run_frame = Frame(window, background="green")
run_frame.pack(side="top", fill="both")

##
name_frame = LabelFrame(run_frame, text="파일 이름 형식 지정")
name_frame.pack(side="top", fill="both")

name_button = Button(name_frame, text="적용")
name_button.pack(side="right", ipadx=18)
name_textbox = Entry(name_frame)
name_textbox.pack(side="right", ipadx=140, ipady=4)


setting_frame = Frame(window, background="blue")
setting_frame.pack(side="top", fill="both")


window.mainloop()
