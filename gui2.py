from tkinter import *

def get_style_string():
    style_string = ''
    if bold.get():
        style_string = 'bold'
    if italic.get():
        style_string += ' italic'
    if underline.get():
        style_string += ' underline'
    return style_string
def style_update():
    style_string = ''
    if bold.get():
        style_string = 'bold'
    if italic.get():
        style_string += ' italic'
    if underline.get():
        style_string += ' underline'
    quote.configure(font = (family.get(), size.get(), style_string))
    
def quote_update():
    quote.configure(text = quote_list[quote_index.get()])
    
def size_update(new_size):
    style_string = get_style_string()
    quote.configure(font = (family.get(), new_size, style_string))
    
def family_update(new_family):
    style_string = get_style_string()
    quote.configure(font = (new_family, size.get(), style_string))

root = Tk()
root.title('Another GUI')
root.configure(background = 'lightblue')
root.minsize(600, 350)

quote_list = ['I think, therefore I am.',
              'Measure twice. Cut once.',
              "I am serious. And don't call me Shirley."]

quote = Label(root, text = quote_list[0], font = ('Arial', 24))
quote.pack(pady = (50, 20))
quote.configure(background = root['background'])

controls = Frame(root)
controls.pack()
controls.configure(background = root['background'])

quote_index = IntVar()

quote_frame = Frame(controls, background = root['background'])
quote_frame.pack(side = LEFT, padx = (0, 50))

Radiobutton(quote_frame, text = 'Philosophy', value = 0, var = quote_index,
            command = quote_update, background = root['background']).pack(anchor = W)
Radiobutton(quote_frame, text = 'Carpentry', value = 1, var = quote_index,
            command = quote_update, background = root['background']).pack(anchor = W)
Radiobutton(quote_frame, text = 'Comedy', value = 2, var = quote_index,
            command = quote_update, background = root['background']).pack(anchor = W)

bold = BooleanVar()
italic = BooleanVar()
underline = BooleanVar()

style_frame = Frame(controls, background = root['background'])
style_frame.pack(side = LEFT)

Checkbutton(style_frame, text = 'Bold', var = bold,
            command = style_update, background = root['background']).pack(anchor = W)
Checkbutton(style_frame, text = 'Italic', var = italic,
            command = style_update, background = root['background']).pack(anchor = W)
Checkbutton(style_frame, text = 'Underline', var = underline,
            command = style_update, background = root['background']).pack(anchor = W)


size = IntVar()

size_slider = Scale(root, orient = HORIZONTAL, from_ = 12, to = 54, var = size,
                    length = 200, command = size_update)
size_slider.set(24)
size_slider.pack(pady = 15)
size_slider.configure(background = root['background'], troughcolor = 'blue')


family_list = ['Arial', 'Courier', 'Times New Roman']

family = StringVar()
family.set(family_list[0])

family_button = OptionMenu(root, family, *family_list, command = family_update)
family_button.pack()
family_button.configure(background = root['background'])

root.mainloop()