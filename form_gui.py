import tkinter as tk
import customtkinter as ctk
from win32api import GetSystemMetrics
from form import entry
import subprocess


wid=GetSystemMetrics(0)
hei=GetSystemMetrics(1)

dis_str=f"{wid}x{hei}+0+0"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry(dis_str)

app.title("FORM")

urn=ctk.StringVar()
name=ctk.StringVar()
reason=ctk.StringVar()

def back(app):
    app.destroy()
    subprocess.run("main_gui.py 1", shell=True)

def print_file(urn,name,dept,year,reason):
	entry(urn,name,dept,year,reason)




#LEBALS
ctk.CTkLabel(master=app, text="URN. No.",width=(wid)/5, height=(hei)/30,font=("Helvetica",25,"bold")).place(x=(wid)/3.5,y=(hei//8))
ctk.CTkLabel(master=app, text="NAME",width=(wid)/5, height=(hei)/30,font=("Helvetica",25,"bold")).place(x=(wid)/3.5,y=2*(hei//8))
ctk.CTkLabel(master=app, text="DEPARTMENT",width=(wid)/5, height=(hei)/30,font=("Helvetica",25,"bold")).place(x=(wid)/3.5,y=3*(hei//8))
ctk.CTkLabel(master=app, text="YEAR",width=(wid)/5, height=(hei)/30,font=("Helvetica",25,"bold")).place(x=(wid)/3.5,y=4*(hei//8))
ctk.CTkLabel(master=app, text="REASON",width=(wid)/5, height=(hei)/30,font=("Helvetica",25,"bold")).place(x=(wid)/3.5,y=5*(hei//8))


urn_ent=ctk.CTkEntry(master=app, width=(wid)/5, height=(hei)/30, corner_radius=5, border_width=None, bg_color="transparent", fg_color=None, border_color=None, text_color=None, placeholder_text_color=None, textvariable=urn, placeholder_text=None, font=None, state=tk.NORMAL)
urn_ent.place(x=(wid)/2,y=(hei)/8)

name_ent=ctk.CTkEntry(master=app, width=(wid)/5, height=(hei)/30, corner_radius=5, border_width=None, bg_color="transparent", fg_color=None, border_color=None, text_color=None, placeholder_text_color=None, textvariable=name, placeholder_text=None, font=None, state=tk.NORMAL)
name_ent.place(x=(wid)/2,y=(2*(hei//8)))


dept_ch=ctk.CTkOptionMenu(master=app,width=(wid)/5, height=(hei)/30,font=("Helvetica",15,"bold"),values=["CSE","ELE","MECH","FOOD","AERO","CIVIL","AI-DS","IOT-CS"])
dept_ch.set("--SELECT--")
dept_ch.place(x=(wid)/2,y=(3*(hei//8)))

year_ch=ctk.CTkOptionMenu(master=app,width=(wid)/5, height=(hei)/30,font=("Helvetica",18,"bold"),values=["1st","2nd","3rd","4th"])
year_ch.set("--SELECT--")
year_ch.place(x=(wid)/2,y=(4*(hei//8)))

reason_ent=ctk.CTkEntry(master=app, width=(wid)/5, height=(hei)/30, corner_radius=5, border_width=None, bg_color="transparent", fg_color=None, border_color=None, text_color=None, placeholder_text_color=None, textvariable=reason, placeholder_text=None, font=None, state=tk.NORMAL)
reason_ent.place(x=(wid)/2,y=(5*(hei//8)))

submit=ctk.CTkButton(master=app,text="SUBMIT",width=(wid)/5, height=(hei)/30,command=lambda:print_file(urn.get(), name.get(), dept_ch.get(), year_ch.get(), reason.get()))
submit.place(x=(wid)//2,y=(7*(hei//8)))


back_b=ctk.CTkButton(master=app,text="< BACK",command=lambda:back(app),width=(wid)/5, height=(hei)/30)
back_b.place(x=(wid)//18,y=(7*(hei//8)))



app.mainloop()