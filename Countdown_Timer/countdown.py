from plyer import notification 
from tkinter import messagebox
from tkinter import *
import time

window = Tk()
window.geometry("300x200")
window.title("Countdown timer")

def timer(): 
    try:
        timer_time = int(hour_entry.get())*3600 + int(min_entry.get())*60 + int(sec_entry.get())
        
    except:
        messagebox.showerror(message="Enter Valid Time")
       
    if timer_time >0:
        hour = 0
        min = 0 
        sec = 0    
    
        while timer_time >= 0:
            min, sec = divmod(timer_time,60)
            if min > 60:
                hour, min = divmod(min,60) 
                       
            hours.set(hour)
            mins.set(min)
            secs.set(sec)
          
            time.sleep(1)   
           
            window.update()
          
            timer_time -= 1
       
        notification.notify(
        
            title = "TIMER ALERT",
          
            message = "Hey amigo!\nDid you do what you wanted to achieve? \nIf not, try again with a new timer",
            app_icon = "D:\CODING\hacktoberfest projects\Countdown Timer\Countdown_Timer\bell.ico",
       
            timeout  = 30,
        )
    
        messagebox.showinfo(message="Timer Complete!")         

def h_click(event):
        hour_entry.delete(0,'end')         
def m_click(event):
        min_entry.delete(0,'end')
def s_click(event):    
        sec_entry.delete(0,'end')
        
title_label_1 = Label(window, text="Countdown Timer ",font=("Gayathri", 11)).pack()
title_label_2 = Label(window, text="Put 0 in fields not of use",font=("Gayathri", 10)).pack()


hours = IntVar()
mins = IntVar()
secs = IntVar()

hour_entry = Entry(window, width=3,textvariable=hours,font=("Ubuntu Mono",18))
min_entry = Entry(window, width=3,textvariable=mins,font=("Ubuntu Mono",18))
sec_entry = Entry(window, width=3,textvariable=secs,font=("Ubuntu Mono",18))


hour_entry.insert(0,00)
min_entry.insert(0,00)
sec_entry.insert(0,00)

hour_entry.place(x=80,y=40)
min_entry.place(x=130,y=40)
sec_entry.place(x=180,y=40)


hour_entry.bind("<1>", h_click)
min_entry.bind("<1>", m_click)
sec_entry.bind("<1>", s_click)

button = Button(window,text='Activate Timer', bg = 'Red',command=timer).pack(pady=40)

window.mainloop()
