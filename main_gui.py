import tkinter as tk
import customtkinter as ctk
from win32api import GetSystemMetrics
import subprocess

wid=GetSystemMetrics(0)
hei=GetSystemMetrics(1)

dis_str=f"{wid}x{hei}+0+0"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



def entry(app):
	app.destroy()
	subprocess.run("form_gui.py 1", shell=True)


def search(app):
	app.destroy()
	subprocess.run("search.py 1", shell=True)

app=ctk.CTk()
app.geometry(dis_str)
app.title("BONAFIDE CERTIFICATE")

ctk.CTkLabel(master=app, text="BONAFIDE CERTIFICATE",width=(wid)/5, height=(hei)/30,font=("Helvetica",40,"bold")).place(x=(wid)/2.8,y=(hei//8))


ent=ctk.CTkButton(master=app,text="Entry",width=(wid)/5, height=(hei)/30,command=lambda:entry(app), corner_radius=7.5)
ent.place(x=(wid)//2.5,y=(hei//3))


search_b=ctk.CTkButton(master=app,text="Search",width=(wid)/5, height=(hei)/30,command=lambda:search(app), corner_radius=7.5)
search_b.place(x=(wid)//2.5,y=3*(hei//6))


app.mainloop()