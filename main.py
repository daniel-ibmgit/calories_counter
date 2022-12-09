from tkinter import*
from random import choice

first_window = Tk()
first_window.title("Calculate Your BMR")
first_window.geometry('500x400')


bg = PhotoImage(file='background.png')
label1 = Label(first_window, image=bg)
label1.place(x=0, y=0)
first_window.resizable(0, 0)

from breakfast import *
from lunch import *
from supper import *

def main():
    if float(mainB()) > sum((breakfast(), lunch(), supper())):
        print(f'Your calories are optimum')
    else:

        print('Your calories exceed your daily recommended limit')
        print("Consider the following balanced diet's which are at par with your bmr")
        bList = {'Bash & Coffee': 476, '2 Pancakes, Sausage, Egg': 394, 'Waakye,Spaghetti and Chicken': 645}
        lList = {'Jollof, Coleslaw & Chicken': 565, 'Friedrice, Coleslaw & Chicken': 650,
                 'Riceballs, Groundnut Soup & Beef': 559}
        sList = {'Fries & Chicken': 505, 'Plain Rice & Chicken': 467, 'Fried Yam & Gizzard': 214}
        h = [(i, j, k) for i in bList for j in lList for k in sList if sum((bList[i], lList[j], sList[k])) <= float(bmr)]
        a = choice(h)
        b = choice(h)
        for ele in (a,b):
            print('\n')
            print(f'Breakfast: {ele[0]}')
            print(f'Lunch: {ele[1]}')
            print(f'Supper: {ele[2]}')
            print('\n')

def mainB():
    Registration()
    return bmr

def take_details():
    w = float(weight.get())
    h = float(height.get())
    a = float(age.get())
    s = clicked1.get()
    ac = clicked.get()
    global bmr
    if s == 'Female':
        restingbmr = 10 * w + (6.25 *h)-(5*a)-161
        if ac =='Sedentary':
            bmr = restingbmr*1.2
            bmr = format(bmr, '.2f')
        elif ac =='Light':
            bmr = restingbmr*1.375
            bmr = format(bmr,'.2f')
        elif ac =='Moderate':
            bmr = restingbmr*1.55
            bmr = format(bmr, '.2f')
        elif ac =='Active':
            bmr = restingbmr*1.725
            bmr = format(bmr, '.2f')

        myLabel = Label(first_window, text=f'Your Basal Metabollic Rate is {bmr} calories').pack()

        return bmr
    elif s =='Male':
        restingbmr = 10 * w + (6.25 *h)-(5*a) + 5
        if ac =='Sedentary':
            bmr = restingbmr*1.2
            bmr = format(bmr, '.2f')
        elif ac =='Light':
            bmr = restingbmr*1.375
            bmr = format(bmr,'.2f')
        elif ac =='Moderate':
            bmr = restingbmr*1.55
            bmr = format(bmr, '.2f')
        elif ac =='Active':
            bmr = restingbmr*1.725
            bmr = format(bmr, '.2f')

        myLabel = Label(first_window, text=f'Your Basal Metabollic Rate is {bmr} calories')
        myLabel.pack()
        return bmr


def Registration():

    global weight
    global height
    global age

    weight = StringVar()
    height = StringVar()
    age = StringVar()

    Label(first_window, text="Please Enter Your Details").pack()
    Label(first_window, text="").pack()
    Label(first_window, text="Weight (kg) *").pack()
    weight_entry = Entry(first_window, textvariable=weight)
    weight_entry.pack()

    Label(first_window, text="Height (cm)*").pack()
    height_entry = Entry(first_window, textvariable=height)
    height_entry.pack()  # declare the entry to clear the fields


    Label(first_window, text="Age *").pack()
    age_entry = Entry(first_window, textvariable=age)
    age_entry.pack()  # declare the entry to clear the fields

    Label(first_window, text="Level of Activity *").pack()
    global clicked
    clicked = StringVar()
    clicked.set('Light')
    levelActivity = ['Sedentary','Light','Moderate','Active']
    option = OptionMenu(first_window,clicked,*levelActivity)
    option.pack()

    global activity
    activity =clicked.get()

    Label(first_window, text="").pack()
    Label(first_window, text="Sex *").pack()
    global clicked1
    clicked1 = StringVar()
    clicked1.set('Male')
    genderOption = ['Male','Female']
    option1 = OptionMenu(first_window,clicked1,*genderOption)
    option1.pack()

    Label(first_window, text="").pack()
    Label(first_window, text="").pack()
    Button(first_window, text="Calculate BMR", width=10, height=1, command=take_details).pack()
    first_window.mainloop()
if __name__ == '__main__':
    main()

