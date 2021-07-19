from tkinter import *

window = Tk()
window.title("파일 이름변환기 Ver1.0")
window.geometry("800x400")
window.resizable(True, True)


# 좌측 프레임
left_frame = Frame(window, background="yellow")  # 프레임의 색은 파티션 구분을 위함
left_frame.pack(side="left", fill="y")


## 버튼 프레임(좌측 프레임 내부에 선언)
button_frame = Frame(left_frame)
button_frame.pack(side="top")


### 버튼 라벨
button_add_file = Button(button_frame, padx=5, pady=3, width=14, text="파일추가")
button_add_file.pack(side="left")

button_del_file = Button(button_frame, padx=5, pady=3, width=14, text="선택 파일삭제")
button_del_file.pack(side=("left"))


## 파일 프레임(좌측 프레임 내부에 선언)
file_frame = Frame(left_frame)
file_frame.pack(side="top")

### 파일 표시, 스크롤바
list_frame = Frame(file_frame)
list_frame.pack(side="left")

Scrollbar = Scrollbar(list_frame)
Scrollbar.pack(side="right", fill="both")

list_file = Listbox(
    list_frame, selectmode="extended", width=30, height=20, yscrollcommand=Scrollbar.set
)
list_file.pack(side="left", fill="both", expand=True)
Scrollbar.config(command=list_file.yview)

## 저장경로 프레임
save_path_frame = Frame(left_frame)
save_path_frame.pack(side="top")


### 저장경로 설정, 버튼
path_frame = LabelFrame(save_path_frame, text="저장경로")
path_frame.pack(side="left")

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

button_dest_path = Button(path_frame, text="찾아보기", width=10)
button_dest_path.pack(side="right")


# 우측 프레임
right_frame = Frame(window, background="green")
right_frame.pack(side="left", fill="y")

##

###
name_button = Button(right_frame, text="적용")
name_button.pack(side="right", ipadx=10)
name_textbox = Entry(right_frame)
name_textbox.pack(side="right", ipadx=35, ipady=3)

window.mainloop()
