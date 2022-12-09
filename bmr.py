from tkinter import*
root = Tk()
root.title('BMR')
root.geometry('400x400')

def print():
    user=e.get()
e = Entry(root)
e.pack()
b = Button(root,text='Submit',command=print).pack()
root.mainloop()
"""
first.resizable(0,0)

clicked = StringVar()
clicked.set('Male')
Label(first,text='Weight').grid(row=0)

options = ['Male','Female']
drop=OptionMenu(first,clicked,*options).pack()
myVar = []
def show():
    myLab = Label(first,text=clicked.get()).pack()
    myVar.append(str(clicked.get()))
but =Button(first, text = 'Done', command=show).pack()
first.mainloop()
print(myVar)
"""