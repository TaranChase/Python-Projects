#  Title: Create Address Book in Python - Using Tkinter
#  Author: deepanshu_rustagi
#  Date: 28 Apr,2021
#  Code version: Python3
#  Availability: https://www.geeksforgeeks.org
# ----------------------------------------------
# (Version Python3)[Source code].https://www.geeksforgeeks.org

#-----------------------------------------------------------------

# Import Module
from tkinter import *

# Object
root = Tk()

# geometry
root.geometry('1200x1200')

root.title("Address Book")

root.config(bg = "#8877EE")

# Contact List
data = []

# Add Contacts
def add():
	global data
	data.append([First_Name.get(),Last_Name.get(),Number.get(),Email.get(1.0, "end-1c"),address.get(1.0, "end-1c")])
	update_book()

# View Contacts
def view():
	First_Name.set(data[int(select.curselection()[0])][0])
	Last_Name.set(data[int(select.curselection()[0])][1])
	Number.set(data[int(select.curselection()[0])][2])
	Email.insert(1.0,data[int(select.curselection()[0])][3])
	Email.delete(1.0, "end")
	address.delete(1.0,"end")
	address.insert(1.0, data[int(select.curselection()[0])][4])

# Delete Contacts
def delete():
	del data[int(select.curselection()[0])]
	update_book()

def reset():
	First_Name.set('')
	Last_Name.set('')
	Number.set('')
	Email.delete(1.0,"end")
	address.delete(1.0,"end")

# Update Contacts
def update_book():
	select.delete(0,END)
	for n,l_n,p,e,a in data:
		select.insert(END, (n,l_n))

# Buttons, Label, ListBox
First_Name = StringVar()
Last_Name = StringVar()
Number = StringVar()

frame = Frame()
frame.pack(pady=10)
frame.place(x=20, y=50)

frame1 = Frame()
frame1.pack(pady=10)
frame1.place(x=20, y=100)

frame2 = Frame()
frame2.pack(pady=10)
frame2.place(x=20, y=150)

frame3 = Frame()
frame3.pack(pady=50)
frame3.place(x=20, y=195)

frame4 = Frame()
frame4.pack(pady=50)
frame4.place(x=20, y=270)


Label(frame, text = 'First Name', font='arial 10 bold', bg="WHITE").pack(side=LEFT)
Entry(frame, textvariable = First_Name,width=45).pack()

Label(frame1, text = 'Last Name', font='arial 10 bold', bg="WHITE").pack(side=LEFT)
Entry(frame1, textvariable = Last_Name,width=45).pack()

Label(frame2, text = 'Phone No.', font='arial 10 bold', bg="WHITE").pack(side=LEFT)
Entry(frame2, textvariable = Number,width=45).pack()

Label(frame3, text = 'Email.', font='arial 10 bold', bg="WHITE").pack(side=LEFT)
Email = Text(frame3,width=45,height=3)
Email.pack()

Label(frame4, text = 'Address', font='arial 10 bold', bg="WHITE").pack(side=LEFT)
address = Text(frame4,width=45,height=20)
address.pack()

Button(root,text="Add",font="arial 12 bold",bg="WHITE",command=add).place(x= 800, y=50)
Button(root,text="View",font="arial 12 bold",bg="WHITE",command=view).place(x= 800, y=100)
Button(root,text="Delete",font="arial 12 bold",bg="WHITE",command=delete).place(x= 800, y=150)
Button(root,text="Reset",font="arial 12 bold",bg="WHITE",command=reset).place(x= 800, y=200)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=900,y=45)

root.mainloop()
