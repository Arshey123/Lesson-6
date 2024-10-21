# activity 1
# from tkinter import *
# window=Tk()
# window.title("Lesson 6")
# window.geometry("400x400")
# a=Label(text="Lesson 6: Tkinter", bg="blue", fg="green", height=10, width=400)
# button= Button(text="Button", bg="blue")


# a.pack()
# button.pack()
# window.mainloop()
# activity 2
from tkinter import *
window=Tk()
window.title("Lesson 6")
window.geometry("400x400")
frame= Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label= Label(master=frame,text="Lesson 6: Activity 2",bg="blue")
label.pack()
label= Label(text="Lesson 6: Activity 2",bg="blue")
label.pack()
textbox= Text(fg="green", bg="blue")
textbox.pack()
window.mainloop()