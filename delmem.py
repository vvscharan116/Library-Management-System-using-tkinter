from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk

cn = pymysql.connect(host="localhost", user="root", password="1234", database="db")
cr = cn.cursor()


def delmem():
    global rot
    p1 = e1.get()
    pq = "select * from mem where roll='" + p1 + "'"
    pr = "delete from mem where roll='" + p1 + "'"
    cr.execute(pq)
    cn.commit()
    r = cr.fetchone()
    if r is None:
        messagebox.showerror('Error', "Member doesn't Exist")
    else:
        try:
            cr.execute(pr)
            cn.commit()
            messagebox.showinfo('Successful', 'Member entry deleted')
            rot.destroy()
        except:
            messagebox.showerror('Error', "Something went wrong")


def delm():
    global rot
    rot = Tk()
    rot.resizable('False', 'False')
    rot.title("Library")
    rot.minsize(width=400, height=400)
    rot.geometry("600x500")

    global e1
    c1 = Canvas(rot, bg='#0f624c', bd=4, relief='flat')
    c1.pack(expand=True, fill=BOTH)
    l0 = Label(rot, text="Delete Member", bg='#0f624c', fg="white", font=('Arial', 30, 'bold'))
    l0.place(x=50, y=50)
    hF = Frame(rot, bg="#FFBB00", bd=5)
    hF.place(x=50, y=100, width=500, height=300)

    e1 = Entry(hF, text="roll", font=('Arial', 10))
    e1.place(x=200, y=50)
    l1 = Label(hF, text="Roll no.", font=('Arial', 10))
    l1.place(x=50, y=50)

    SubmitBtn = Button(hF, text="Delete", bg='#d1ccc0', fg='black', command=delmem)
    SubmitBtn.place(x=100, y=200, width=50, height=30)

    quitBtn = Button(hF, text="Quit", bg='#f7f1e3', fg='black', command=rot.destroy)
    quitBtn.place(x=200, y=200, width=50, height=30)
    rot.mainloop()
