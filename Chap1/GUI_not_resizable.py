# GUI의 크기 변환 막기
import tkinter as tk

win = tk.Tk() # Create instance

win.title("Python GUI") # Title

win.resizable(False, False) # Disable Resizing the GUI



win.mainloop() # start GUI