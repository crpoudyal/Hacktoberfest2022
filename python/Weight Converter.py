from tkinter import *

#window
mwindow = Tk()
mwindow.title('Weight Converter')

#function for conversion
def conv():
    
    pound = float(val.get())*2.20462
    ounce = float(val.get())*35.274
 
    pr1.insert(END, pound)
    pr2.insert(END, ounce)
 

#part1
show1 = Label(mwindow, text='Weight in kilograms:')
show1.grid(row=0,column=0)

val = StringVar()
u_in = Entry(mwindow,fg="black" , bg="white", width=15,textvariable=val)
u_in.grid(row=0,column=1)

convbutton = Button(mwindow, text='Convert',fg='white',bg='black',width=6, command =conv)
convbutton.grid(row=1,column=1)

#part2
pd = Label(mwindow, text='Pounds')
pd.grid(row=2,column=0)
pr1 = Text(mwindow, height = 1, width=20)
pr1.grid(row=2,column=1)
oc = Label(mwindow, text='Ounce')
oc.grid(row=3,column=0)
pr2 = Text(mwindow, height = 1, width=20)
pr2.grid(row=3,column=1)



mwindow.mainloop()