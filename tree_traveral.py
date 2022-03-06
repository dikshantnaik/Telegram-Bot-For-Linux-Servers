from tkinter import *

root =Tk()
root.title("Codemy.com - Canvas")
root.geometry("500x500")

my_canvas = Canvas(root,width=300,height = 200,bg="white")
my_canvas.pack(pady=20)

my_canvas.create_line(0,100,300,100,fill="red")
my_canvas.create_line(150,0,150,200,fill="red")

my_canvas.create_oval(100,100,210,210)

root.mainloop()