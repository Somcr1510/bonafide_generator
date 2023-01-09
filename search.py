import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from win32api import GetSystemMetrics
import subprocess
import sqlite3


wid=GetSystemMetrics(0)
hei=GetSystemMetrics(1)

dis_str=f"{wid}x{hei}+0+0"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app=ctk.CTk()
app.geometry(dis_str)

app.title("SEARCH")


urn=ctk.StringVar()
name=ctk.StringVar()
reason=ctk.StringVar()

urn.set("")
name.set("")
reason.set("")



ctk.CTkLabel(master=app, text="URN. No.",width=(wid)/5, height=(hei)/30,font=("Helvetica",25,"bold")).place(x=(wid)/18,y=(hei//10))
ctk.CTkLabel(master=app, text="NAME",width=(wid)/5, height=(hei)/30,font=("Helvetica",25,"bold")).place(x=(wid)/2,y=(hei//10))
ctk.CTkLabel(master=app, text="DEPARTMENT",width=(wid)/5, height=(hei)/30,font=("Helvetica",25,"bold")).place(x=(wid)/25,y=2*(hei//10))
ctk.CTkLabel(master=app, text="YEAR",width=(wid)/5, height=(hei)/30,font=("Helvetica",25,"bold")).place(x=(wid)/2,y=2*(hei//10))
ctk.CTkLabel(master=app, text="REASON",width=(wid)/5, height=(hei)/30,font=("Helvetica",25,"bold")).place(x=(wid)/18,y=3*(hei//10))


urn_ent=ctk.CTkEntry(master=app, width=(wid)/5, height=(hei)/30, corner_radius=5, border_width=None, bg_color="transparent", fg_color=None, border_color=None, text_color=None, placeholder_text_color=None, textvariable=urn, placeholder_text=None, font=None, state=tk.NORMAL)
urn_ent.place(x=(wid)/5,y=(hei)/10)

name_ent=ctk.CTkEntry(master=app, width=(wid)/5, height=(hei)/30, corner_radius=5, border_width=None, bg_color="transparent", fg_color=None, border_color=None, text_color=None, placeholder_text_color=None, textvariable=name, placeholder_text=None, font=None, state=tk.NORMAL)
name_ent.place(x=(wid)/1.55,y=(hei//10))


dept_ch=ctk.CTkOptionMenu(master=app,width=(wid)/5, height=(hei)/30,font=("Helvetica",15,"bold"),values=["CSE","ELE","MECH","FOOD","AERO","CIVIL","AI-DS","IOT-CS"])
dept_ch.set("--SELECT--")
dept_ch.place(x=(wid)/5,y=(2*(hei//10)))

year_ch=ctk.CTkOptionMenu(master=app,width=(wid)/5, height=(hei)/30,font=("Helvetica",18,"bold"),values=["1st","2nd","3rd","4th"])
year_ch.set("--SELECT--")
year_ch.place(x=(wid)/1.55,y=(2*(hei//10)))

reason_ent=ctk.CTkEntry(master=app, width=(wid)/5, height=(hei)/30, corner_radius=5, border_width=None, bg_color="transparent", fg_color=None, border_color=None, text_color=None, placeholder_text_color=None, textvariable=reason, placeholder_text=None, font=None, state=tk.NORMAL)
reason_ent.place(x=(wid)/5,y=(3*(hei//10)))



def back(app):
    app.destroy()
    subprocess.run("main_gui.py 1", shell=True)


def make_quary():
    quary="WHERE"
    global urn,name,reason,dept_ch,year_ch
    if urn.get()!="":
        if quary!="WHERE":
            quary+=f" AND URN=\"{urn.get()}\""
        else:
            quary+=f" URN=\"{urn.get()}\""
    if name.get()!="":
        if quary!="WHERE":
            quary+=f" AND NAME=\"{name.get()}\""
        else:
            quary+=f" NAME=\"{name.get()}\""
    if reason.get()!="":
        if quary!="WHERE":
            quary+=f" AND REASON=\"{reason.get()}\""
        else:
            quary+=f" REASON=\"{reason.get()}\""
    if year_ch.get()!="--SELECT--":
        if quary!="WHERE":
            quary+=f" AND YEAR=\"{year_ch.get()}\""
        else:
            quary+=f" YEAR=\"{year_ch.get()}\""
    if dept_ch.get()!="--SELECT--":
        if quary!="WHERE":
            quary+=f" AND DEPT=\"{dept_ch.get()}\""
        else:
            quary+=f" DEPT=\"{dept_ch.get()}\""
    View(quary)



def View(quary):
    for record in tree.get_children():
        tree.delete(record)
    stri="SELECT * FROM register "
    if quary!="WHERE":
         stri+=quary
    print(stri)
    conn = sqlite3.connect("REG.db")
    cur = conn.cursor()
    cur.execute(stri)
    rows = cur.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    conn.close()
    frame.configure()




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

submit=ctk.CTkButton(master=app,text="SUBMIT",command=make_quary,width=(wid)/5, height=(hei)/30)
submit.place(x=(wid)//2.5,y=(7*(hei//8)))
back_b=ctk.CTkButton(master=app,text="< BACK",command=lambda:back(app),width=(wid)/5, height=(hei)/30)
back_b.place(x=(wid)//18,y=(7*(hei//8)))


app.mainloop()