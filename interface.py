from tkinter import *
from backend import api_call, show_image

FONT_NAME = "Arial"
FONT = (FONT_NAME, 15)
options = ["enhance", "anime", "cinematic", "digital-art", "comic-book", "fantasy-art", "line-art", "analog-film",
           "neon-punk", "isometric", "low-poly", "origami", "modeling-compound", "3d-model", "pixel-art",
           "tile-texture"]
NAME = 200256006


class Interface:
    def __init__(self):

        self.NAME = NAME

        self.window = Tk()
        self.window.title("Image Generator Api Interface")
        self.window.config(padx=40, pady=40)

        self.prompt_label = Label(text="Prompt:", font=FONT)
        self.prompt_label.grid(column=0, row=1)
        self.prompt_entry = Entry(width=50, font=FONT)
        self.prompt_entry.grid(column=1, row=1, columnspan=2)
        self.prompt_entry.focus()

        self.style_label = Label(text="Style", font=FONT)
        self.style_label.grid(column=0, row=2)
        self.selected_var = StringVar(self.window)
        self.selected_var.set(options[0])
        self.dropdown = OptionMenu(self.window, self.selected_var, *options)
        self.dropdown.config(width=19, font=FONT)
        self.dropdown.grid(column=1, row=2)

        self.seed_label = Label(text="Seed:", font=FONT)
        self.seed_label.grid(column=0, row=3)
        self.seed_entry = Entry(width=25, font=FONT)
        self.seed_entry.grid(column=1, row=3)
        self.seed_entry.insert(0, "0")

        self.steps_label = Label(text="Steps:", font=FONT)
        self.steps_label.grid(column=0, row=4)
        self.steps_entry = Entry(width=25, font=FONT)
        self.steps_entry.grid(column=1, row=4)
        self.steps_entry.insert(0, "50")

        self.cfg_label = Label(text="CFG:", font=FONT)
        self.cfg_label.grid(column=0, row=5)
        self.cfg_entry = Entry(width=25, font=FONT)
        self.cfg_entry.grid(column=1, row=5)
        self.cfg_entry.insert(0, "8.0")

        self.width_label = Label(text="Width:", font=FONT)
        self.width_label.grid(column=0, row=6)
        self.width_entry = Entry(width=25, font=FONT)
        self.width_entry.grid(column=1, row=6)
        self.width_entry.insert(0, "1024")

        self.height_label = Label(text="Height:", font=FONT)
        self.height_label.grid(column=0, row=7)
        self.height_entry = Entry(width=25, font=FONT)
        self.height_entry.grid(column=1, row=7)
        self.height_entry.insert(0, "1024")

        self.generate_button = Button(text="Generate", command=self.api_call, width=50, font=FONT)
        self.generate_button.grid(column=0, row=8, columnspan=2)

        self.show_image_button = Button(text="Show Image", command=self.show_image_button, width=50, font=FONT)
        self.show_image_button.grid(column=0, row=9, columnspan=2)

        self.window.mainloop()

    def api_call(self):
        api_call(
            self.get_steps(),
            self.get_width(),
            self.get_height(),
            self.get_seed(),
            self.get_cfg(),
            self.get_style(),
            self.get_prompt()
        )

    def show_image_button(self):
        seed = self.NAME
        show_image(seed)

    def get_steps(self):
        return int(self.steps_entry.get())

    def get_width(self):
        return int(self.width_entry.get())

    def get_height(self):
        return int(self.height_entry.get())

    def get_seed(self):
        return int(self.seed_entry.get())

    def get_cfg(self):
        return float(self.cfg_entry.get())

    def get_style(self):
        return self.selected_var.get()

    def get_prompt(self):
        return self.prompt_entry.get()
