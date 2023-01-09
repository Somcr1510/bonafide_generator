import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from win32api import GetSystemMetrics
import subprocess
import sqlite3


wid=GetSystemMetrics(0)
hei=GetSystemMetrics(1)

dis_str=f"{wid}x{hei}"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def View():
    conn = sqlite3.connect("REG.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM register")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.close()


app=ctk.CTk()
app.geometry(dis_str)

frame=ctk.CTkFrame(master=app)
frame.place(x=wid//15,y=hei//2.5)

tree= ttk.Treeview(frame, column=("URN", "NAME", "DEPT", "YEAR", "REASON","DATE"))
tree.heading("URN",text="URN")
tree.heading("NAME",text="NAME")
tree.heading("DEPT",text="DEPT")
tree.heading("YEAR",text="YEAR")
tree.heading("REASON",text="REASON")
tree.heading("DATE",text="DATE")
tree.pack()

submit=ctk.CTkButton(master=app,text="SUBMIT",command=View,width=(wid)/5, height=(hei)/30)
submit.place(x=(wid)//2.5,y=(7*(hei//8)))

app.mainloop()