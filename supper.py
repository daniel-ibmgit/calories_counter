from tkinter import *
from dictionary import *

def supper():
    root=Tk()
    root.title('Supper')
    root.geometry('400x400')
    bg = PhotoImage(file='background.png')
    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)

    clicked= StringVar()
    clicked.set('Jollof_Rice')
    options=list(sorted([i for i in food_dictionary]))
    drop=OptionMenu(root,clicked,*options)
    drop.pack()
    food_list=[]
    def show1():
        mylabel=Label(root, text=food_dictionary[clicked.get()][1]).pack()
        food_list.append(food_dictionary[clicked.get()][1])
    def show2():
        mylabel=Label(root, text=food_dictionary[clicked.get()][0]).pack()
        food_list.append(food_dictionary[clicked.get()][0])
    def show3():
        mylabel=Label(root, text=f'Total calories is {sum(food_list)}').pack()


    myButton=Button(root,text='Full Portion',command=show1).pack()
    myButton2=Button(root,text='Half Portion',command=show2).pack()
    myButton3 = Button(root, text='Total Calories', command=show3).pack()


    root.mainloop()
    return sum(food_list)

