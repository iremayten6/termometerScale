from tkinter import *


def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()
window.title("TEMPERATURE")


# hotImage = PhotoImage(file="hot.png")
# hotLabel = Label(image=hotImage,compound="bottom")
# hotLabel.pack()


scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              orient=VERTICAL,
              font=("Consolas",20),
              tickinterval= 10,
              showvalue= 0,
              troughcolor= "blue",
              fg="#FF1C00",
              relief= "solid",
              borderwidth=2,
              )

#scale.set(70)
scale.pack()

# coldImage = PhotoImage(file="cold.png")
# coldLabel = Label(image=coldImage,compound="bottom")
# coldLabel.pack()


button = Button(window,text="submit",command=submit,bg="powder blue",fg="black",activebackground="powder blue")
button.pack()

window.mainloop()
