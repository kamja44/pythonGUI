# 텍스트박스 위젯 생성하기
# tkinter에는 일반적인 한 줄짜리 텍스트박스 위젯을 엔트리(Entry)라고 한다.
import tkinter as tk
from tkinter import ttk # ttk 모듈에는 GUI를 멋지게 보이게 하는 노트북, 프로그레스바, 라벨과 색다른 버튼과 같은 고급 위젯이 있다.

win = tk.Tk() # Create instance

win.title("Python GUI") # Title

# Adding a Label that will get modified
ttk.Label(win, text="Enter a name: ").grid(column=0, row=0)

# Adding a Text box Entry widget
name = tk.StringVar() # name 변수를 StringVar을 사용하여 문자열 타입으로 지정한 이유 <- tkinter는 파이썬이 아니라 동적 타입 유추가 안되기 때문이다.
name_entered = ttk.Entry(win, width=12, textvariable=name) # 14Line의 name <- 엔트리 위젯에 텍스트를 입력할 때마다 이 텍스트는 name 변수에 저장된다.
name_entered.grid(column=0, row=1)

# Button Click Event
def click_me():
    action.configure(text="Hello "+name.get()) # name.get()을 사용하여 엔트리 위젯의 값을 가져온다. <- 엔트리 위젯은 한 줄짜리 텍스트박스 위젯을 말한다.

# Adding Button
action = ttk.Button(win, text="Click me", command=click_me) # command에 콜백 함수를 지정한다.
action.grid(column=1, row=1)
action.configure(state="disabled") # button을 비활성화한다.

name_entered.focus()

win.mainloop() # start GUI