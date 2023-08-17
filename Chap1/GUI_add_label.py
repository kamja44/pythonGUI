# GUI 폼에 라벨 추가하기

import tkinter as tk
from tkinter import ttk # ttk 모듈에는 GUI를 멋지게 보이게 하는 노트북, 프로그레스바, 라벨과 색다른 버튼과 같은 고급 위젯이 있다.

win = tk.Tk() # Create instance

win.title("Python GUI") # Title

ttk.Label(win, text="A Label").grid(column=0, row=0)



win.mainloop() # start GUI