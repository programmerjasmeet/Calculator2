from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()


root.geometry("644x970")
root.title("Calculator By CodeWithHarry")
# root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)
buttonframe = Frame(root,)

list1 = ["9", "8", "7", "C", "6", "5", "4", "/", "3", "2", "1", "*", "00", "0", ".", "-", "%", "DEL", "=", "+"]
i = 0
for n in list1:
    # here width of button means 1 text width
    button1 = Button(buttonframe, text=n, font="lucida 20 ", padx=35, width=1, )
    button1.grid(row=int(i / 4), column=i % 4)
    i = i + 1
    button1.bind("<Button-1>", click)

buttonframe.pack()


root.mainloop()
