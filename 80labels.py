from tkinter import*

# label an area widgety that holds text and / pr an image within a window 

window = Tk()
photo = PhotoImage(file='Screenshot (25).png')
label = Label(window,
              text="bro do you even code ",
              font=('Arial',40,'bold'),
              fg='green',
              bg='black',
              relief=SUNKEN,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='center')
label.pack()

# label.place(x=100,y=100)



window.mainloop()