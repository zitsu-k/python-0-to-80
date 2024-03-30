from tkinter import*


    # print("you clicked the button!")
# button = you click it and it does stuff
count = 0
def click():
    global count
    count += 1
    print(f'you clicked the button {count} times')

window = Tk()

photo = PhotoImage(file="like.png")

button = Button(window,
                text="Click me!",
                command=click,
                font = ("Cocnsmic Sans",30),
                fg="red",
                bg="black",
                activebackground="red",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()


window.mainloop()