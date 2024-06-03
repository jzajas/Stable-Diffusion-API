from tkinter import *
FONT_NAME = "Arial"
FONT = (FONT_NAME,20)
options = ["Option 1", "Option 2", "Option 3", "Option 4"]


class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Generator Api Interface")
        self.window.config(padx=40, pady=40)

        self.prompt_label = Label(text="Prompt:")
        self.prompt_label.grid(column=0, row=1)
        self.prompt_entry = Entry(width=50)
        self.prompt_entry.grid(column=1, row=1, columnspan=2)
        self.prompt_entry.focus()

        self.style_label = Label(text="Style")
        self.style_label.grid(column=0, row=2)
        self.selected_var = StringVar(self.window)
        self.selected_var.set(options[0])
        self.dropdown = OptionMenu(self.window, self.selected_var, *options)
        self.dropdown.config(width=19)
        self.dropdown.grid(column=1, row=2)

        self.seed_label = Label(text="Seed:")
        self.seed_label.grid(column=0, row=3)
        self.seed_entry = Entry(width=25)
        self.seed_entry.grid(column=1, row=3)
        self.seed_entry.insert(0,"0")

        self.steps_label = Label(text="Steps:")
        self.steps_label.grid(column=0, row=4)
        self.steps_entry = Entry(width=25)
        self.steps_entry.grid(column=1, row=4)
        self.steps_entry.insert(0,"50")

        self.cfg_label = Label(text="CFG:")
        self.cfg_label.grid(column=0, row=5)
        self.cfg_entry = Entry(width=25)
        self.cfg_entry.grid(column=1, row=5)
        self.cfg_entry.insert(0,"8.0")

        self.width_label = Label(text="Width:")
        self.width_label.grid(column=0, row=6)
        self.width_entry = Entry(width=25)
        self.width_entry.grid(column=1, row=6)
        self.width_entry.insert(0,"1024")

        self.height_label = Label(text="Height:")
        self.height_label.grid(column=0, row=7)
        self.height_entry = Entry(width=25)
        self.height_entry.grid(column=1, row=7)
        self.height_entry.insert(0, "1024")

        self.generate_button = Button(text="Generate", command=self.api_call, width=50)
        self.generate_button.grid(column=0, row=8, columnspan=2)


        self.window.mainloop()

    def api_call(self):
        pass