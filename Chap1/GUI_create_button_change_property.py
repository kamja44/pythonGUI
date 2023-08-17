# 버튼 생성 및 텍스트 속성 변경하기
import tkinter as tk
from tkinter import ttk # ttk 모듈에는 GUI를 멋지게 보이게 하는 노트북, 프로그레스바, 라벨과 색다른 버튼과 같은 고급 위젯이 있다.

win = tk.Tk() # Create instance

win.title("Python GUI") # Title

ttk.Label(win, text="A Label").grid(column=0, row=0)

# Adding a Label that will get modified
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

# Button Click Event
def click_me():
    action.configure(text="** I have been Clicked **")
    a_label.configure(foreground="red")
    a_label.configure(text="A Red Label")

# Adding Button
action = ttk.Button(win, text="Click me", command=click_me) # command에 콜백 함수를 지정한다.
action.grid(column=1, row=0)

win.mainloop() # start GUI