# radio button = similar to checkbox , but you can only select one from a group 
from tkinter import*


food = ['pizza','hamburger','hotdog']

def order():
    if(x.get()==0):
        print("you ordered pizza!")
    elif(x.get()==1):
        print("you ordered a hamburger!")
    else:
        print("you ordered hotdog")




window= Tk()

pizzaimage= PhotoImage(file='pizza.png')
burgerimage= PhotoImage(file='burger.png')
hotdogimage= PhotoImage(file='hotdog.png')
foodImages = [pizzaimage,burgerimage,hotdogimage]
x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value= index,
                              padx=95,
                              font=("Impact",50),
                              image=foodImages[index],
                              compound=LEFT,
                              indicatoron=0 ,
                              width=875,
                              command=order,
                              pady=65,
                              fg='red',
                              bg = 'black')
    radiobutton.pack(anchor=W)
window.mainloop()