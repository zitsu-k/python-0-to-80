from tkinter import*


def tick():
    if(x.get()==1):
        print("you agree!")
    else:
        print("you don't agree")


window = Tk()


python_photo = PhotoImage(file='like.png')

x=IntVar()

check_box= Checkbutton(window,
                       text="I agree to this terms and condition ",
                       font=('Arial',15),
                       fg='lightgreen',
                       activebackground='black',
                       bg='black',
                       activeforeground='green',
                       padx=20,
                       pady=20,
                       variable=x,
                       onvalue=1,
                       offvalue=0,
                       command=tick,
                       image=python_photo,
                       compound='left')
check_box.pack()


window.mainloop()