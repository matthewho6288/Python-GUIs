import tkinter

def button_pushed():
    label.configure(text = 'Hello ' + text_field.get() + '!' )

root = tkinter.Tk()
root.title('My First GUI')
root.configure(width = 400, height = 200, background = 'lightblue')

label = tkinter.Label(root, text='Hello!', font=('Helvetica', 18, 'bold'))
#label.pack()
label.place(relx = 0.5, rely = 0.25, anchor = tkinter.CENTER)


button = tkinter.Button(root, text = 'Push Me', font = ('Helvetica', 18),
                        command = button_pushed)
#button.pack()
button.place(relx = 0.5, rely = 0.50, anchor = tkinter.CENTER)
                        
text_field = tkinter.Entry(root)
text_field.place(relx = 0.5, rely = 0.75, anchor = tkinter.CENTER)

root.mainloop()