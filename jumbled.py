import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = [
    'python',
    'java',
    'mumbai',
    'database',
    'kotil',
    'jaipur',
    'dubai',
    'Andhra',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Goa',
    'Gujarat',
    'Harayana',
    'Himachal ',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya ',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',

]

words = [
    'thonpy',
    'ajav',
    'bmumia',
    'tabadaes',
    'tilko',
    'ipuraj',
    'ubaid',
    'Ndhara',
    'uracahnla',
    'sasam',
    'hirab',
    'hatithcgshra',
    'ago',
    'ujartga',
    'arayanh',
    'mhihala',
    'hrkajnadk',
    'arantkaka',
    'reaalk',
    'adhmay',
    'ahaartharm',
    'napirum',
    'hgaemlaya',
    'oriazm',
    'landnaag',
]


num = random.randrange(0,10,1)
def res():
    global words,answers,num
    num = random.randrange(0,10,1)
    b1.config(text = words[num])
    e1.delete(0,END)

def default():
    global words,answers,num
    b1.config(text = words[num])

def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Succes","This is a correct")
        res()
    else:
        messagebox.showerror("Error","This is not correct try again next")
        e1.delete(0, END)





root = tkinter.Tk()
root.geometry('350x400+400+300')
root.title('Jumbbled')
root.configure(background= '#000000')



b1 = Label(
    root,
    text = 'Your text here',
    font = ('Verdana',18),
    bg = "#000000",
    fg = '#ffffff',

)
b1.pack(pady = 30,ipady = 10, ipadx = 10)

ans = StringVar()
e1 = Entry(
    root,
    font = ('Verdana',16),
    textvariable = ans,
)
e1.pack(ipady = 5,ipadx = 5)

btncheck = Button(
    root,
    text = ('Check'),
    font = ('Comic sans ms',16),
    width = 16,
    bg = "#4C4B4B",
    fg = '#6ab04c',
    relief = GROOVE,
    command = checkans,
)
btncheck.pack(pady = 40)

btnreset = Button(
    root,
    text = ('Reset'),
    font = ('Comic sans ms',16),
    width = 16,
    bg = "#4C4B4B",
    fg = '#6ab04c',
    relief = GROOVE,
    command = res,
)
btnreset.pack(pady = 40)

default()
root.mainloop()
