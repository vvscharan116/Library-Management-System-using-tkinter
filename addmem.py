from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk

cn = pymysql.connect(host="localhost", user="root", password="1234", database="db")
cr = cn.cursor()
q=0

def addmem():

    global rot
    p1 = e1.get()
    p2 = e2.get().lower()
    p3 = e3.get()
    p4 = e4.get()
    global rot
    if p4 == "Bachelor Degree":
        p4 = '1'
    elif p4 == "Master Degree":
        p4 = '2'
    elif p4 == "Research Scholar":
        p4 = '3'
    elif p4 == "Staff":
        p4 = '4'
    # messagebox.showinfo("Error",p4)
    pr = "insert into mem values('" + p1 + "','" + p2 + "','" + p3 + "','" + p4 + "')"
    pq = "select * from mem where roll= '" + p2 + "'"
    cr.execute(pq)
    cn.commit()
    p = cr.fetchone()
    if p is None:
        try:
            cr.execute(pr)
            cn.commit()
            messagebox.showinfo("Successful", "Member successfully added")
            rot.destroy()
        except:
            messagebox.showinfo("Error", "Something went wrong")
            rot.destroy()
    else:
        messagebox.showinfo("Error", "Member already exists")
        rot.destroy()

def add():
    global rot
    rot = Tk()
    rot.resizable('False', 'False')
    rot.title("Library")
    rot.minsize(width=400, height=400)
    rot.geometry("600x500")

    global e1, e2, e3, e4

    c1 = Canvas(rot, bg='#0f624c', bd=4, relief='flat')
    c1.pack(expand=True, fill=BOTH)

    l0 = Label(rot, text="Member Details", bg='#0f624c', fg="white", font=('Arial', 30, 'bold'))
    l0.place(x=50, y=50)

    hF = Frame(rot, bg="#FFBB00", bd=5)
    hF.place(x=50, y=100, width=500, height=300)

    l1 = Label(hF, text="Name", font=('Arial', 10))
    l1.place(x=50, y=45)

    l2 = Label(hF, text="Roll no.", font=('Arial', 10))
    l2.place(x=50, y=70)

    l3 = Label(hF, text="Gender", font=('Arial', 10))
    l3.place(x=50, y=95)

    l4 = Label(hF, text="Member type", font=('Arial', 10))
    l4.place(x=50, y=120)

    e1 = Entry(hF)
    e1.place(x=200, y=45)

    e2 = Entry(hF)
    e2.place(x=200, y=70)

    gendlist = ["Male", "Female", "Others"]

    memlist = ["Bachelor Degree", "Master Degree", "Research Scholar", "Staff"]

    e3 = ttk.Combobox(hF, values=gendlist)
    e3['state'] = 'readonly'
    e3.place(x=200, y=95)

    e4 = ttk.Combobox(hF, values=memlist)
    e4["state"] = 'readonly'
    e4.place(x=200, y=120)

    SubmitBtn = Button(hF, text="Add", bg='#d1ccc0', fg='black', command=addmem)
    SubmitBtn.place(x=100, y=200, width=50, height=30)

    quitBtn = Button(hF, text="Quit", bg='#f7f1e3', fg='black', command=rot.destroy)
    quitBtn.place(x=200, y=200, width=50, height=30)
    rot.mainloop()
