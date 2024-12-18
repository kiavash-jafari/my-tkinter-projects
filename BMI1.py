from cProfile import label
from tkinter import *
tk = Tk()
from tkinter import messagebox
canvas=Canvas(tk,width=500,height=500)
canvas.pack()

label = Label(tk,text="heig?",)
label.pack()

entry = Entry(tk,bg="blue",bd=10,show="*")
entry.pack()

label1 = Label(tk,text="vazn?")
label1.pack()

entry1 = Entry(tk,bg="red",bd=10,show="*")
entry1.pack()
def Bmi ():
    w = float(entry1.get())
    h = float(entry.get())
    bmi = round((w/ (h*h)),2)
    canvas.create_text((200,200),text=str(bmi))
    if bmi < 18.5 :
        canvas.create_text((100,200),text="under weight")
    elif bmi < 18.5<= bmi <= 24.9 :
        canvas.create_text((100,200),text="normal") 
    elif 25 <= bmi <= 29.9 :
        canvas.create_text((100,200),text=" need  PE")
    elif 30 <= bmi <= 34.9:
          canvas.create_text((100,200),text="obese")
    elif bmi > 35 :
        canvas.create_text((100,200),text="chaqal")

btn =  Button(tk,text="BMI",command=Bmi)
btn.pack()
canvas.bind_all("<KeyPress-Return>",Bmi)
tk.mainloop()