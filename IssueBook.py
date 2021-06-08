from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from datetime import date
import datetime

mypass = "1234"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued"
bookTable = "books"

# List To store all Book IDs
allBid = []


def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    bid = inf1.get()
    bid=str(bid)
    issueto = inf2.get()
    issueto=str(issueto)

    # issueBtn.destroy()
    # labelFrame.destroy()
    # lb1.destroy()
    # inf1.destroy()
    # inf2.destroy()

    extractBid="select * from books where bid="+bid
    pq = "select * from mem where roll='" + issueto + "'"

    try:
        cur.execute(pq)
        con.commit()
        r = cur.fetchone()
        if r == None:
            messagebox.showerror('Error', "Member doesn't exist")
            return
        else:
            roletype=r[3]
    except:
        return
    cur.execute(extractBid)
    con.commit()
    stat='avail'
    present=0
    for i in cur:
        stat=i[3]
        present=1
    if present==1:
        if stat=='avail':
            check=True
            #messagebox.showinfo("Message","Book present"+bid)
        else:
            check=False
    else:
        messagebox.showerror("Error","Book ID is not present")
        return
    CheckNumIssued = "select * from books_issued where roll='"+issueto+"'"
    c=0
    try:
        cur.execute(CheckNumIssued)
        con.commit()
        issuedcou = 0
        for i in cur:
            issuedcou += 1

        yesorno = True

        if roletype == '1' and issuedcou == 2:
            yesorno = False
        elif roletype == "2" and issuedcou == 4:
            yesorno = False
        elif roletype == '3' and issuedcou == 6:
            yesorno = False
        elif roletype == '4' and issuedcou == 10:
            yesorno = False

        if yesorno == False:
            messagebox.showinfo('Error', "Book issue Maximum Limit Reached")
        else:
            try:
                if check == True:
                    todaydate = datetime.datetime.now()
                    #todaydate=str(todaydate)
                    #todaydate=date.today()
                    #todaydate=str(todaydate)
                    pr=(bid,issueto,todaydate,roletype)
                    issueSql = "insert into books_issued values (%s, %s, %s,%s)"
                    updateStatus = "update books set status = 'issued' where bid = '" + bid + "'"
                    cur.execute(issueSql,pr)
                    con.commit()
                    cur.execute(updateStatus)
                    con.commit()
                    messagebox.showinfo('Success', "Book Issued Successfully")
                    root.destroy()
                else:
                    allBid.clear()
                    messagebox.showinfo('Message', "Book Already Issued")
                    root.destroy()
            except:
                messagebox.showinfo("Search Error", "The value entered is wrong, Try again")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs ")

def issueBook():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()