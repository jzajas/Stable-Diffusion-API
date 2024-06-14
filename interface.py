from tkinter import *
from backend import api_call, show_image, open_folder, random_seed, save_api_key, load_api_key

FONT_NAME = "Arial"
FONT = (FONT_NAME, 20)
options = ["enhance", "anime", "cinematic", "digital-art", "comic-book", "fantasy-art", "line-art", "analog-film",
           "neon-punk", "isometric", "low-poly", "origami", "modeling-compound", "3d-model", "pixel-art",
           "tile-texture"]
BACKGROUND = "light gray"


class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Generator Api Interface")
        self.window.config(padx=40, pady=40, background=BACKGROUND)

        self.api_key = load_api_key()

        self.prompt_label = Label(text="Prompt:", font=FONT, background=BACKGROUND)
        self.prompt_label.grid(column=0, row=1)
        self.prompt_entry = Entry(width=50, font=FONT, background=BACKGROUND)
        self.prompt_entry.grid(column=1, row=1, columnspan=2)
        self.prompt_entry.focus()

        self.style_label = Label(text="Style", font=FONT, background=BACKGROUND)
        self.style_label.grid(column=0, row=2)
        self.selected_var = StringVar(self.window)
        self.selected_var.set(options[0])
        self.dropdown = OptionMenu(self.window, self.selected_var, *options)
        self.dropdown.config(width=19, font=FONT, background=BACKGROUND)
        self.dropdown.grid(column=1, row=2)

        self.seed_label = Label(text="Seed:", font=FONT, background=BACKGROUND)
        self.seed_label.grid(column=0, row=3)
        self.seed_entry = Entry(width=25, font=FONT, background=BACKGROUND)
        self.seed_entry.grid(column=1, row=3)
        self.seed_entry.insert(0, random_seed())

        self.steps_label = Label(text="Steps:", font=FONT, background=BACKGROUND)
        self.steps_label.grid(column=0, row=4)
        self.steps_entry = Entry(width=25, font=FONT, background=BACKGROUND)
        self.steps_entry.grid(column=1, row=4)
        self.steps_entry.insert(0, "50")

        self.cfg_label = Label(text="CFG:", font=FONT, background=BACKGROUND)
        self.cfg_label.grid(column=0, row=5)
        self.cfg_entry = Entry(width=25, font=FONT, background=BACKGROUND)
        self.cfg_entry.grid(column=1, row=5)
        self.cfg_entry.insert(0, "8.0")

        self.width_label = Label(text="Width:", font=FONT, background=BACKGROUND)
        self.width_label.grid(column=0, row=6)
        self.width_entry = Entry(width=25, font=FONT, background=BACKGROUND)
        self.width_entry.grid(column=1, row=6)
        self.width_entry.insert(0, "1024")

        self.height_label = Label(text="Height:", font=FONT, background=BACKGROUND)
        self.height_label.grid(column=0, row=7)
        self.height_entry = Entry(width=25, font=FONT, background=BACKGROUND)
        self.height_entry.grid(column=1, row=7)
        self.height_entry.insert(0, "1024")

        self.generate_button = Button(text="Generate", command=self.api_call, width=50, font=FONT,
                                      background=BACKGROUND)
        self.generate_button.grid(column=0, row=8, columnspan=2)

        self.show_images_button = Button(text="Show Images", command=open_folder, width=50, font=FONT,
                                         background=BACKGROUND)
        self.show_images_button.grid(column=0, row=9, columnspan=2)

        self.randomize_seed_button = Button(text="Randomize", command=self.randomize_seed, width=10, font=FONT,
                                            background=BACKGROUND)
        self.randomize_seed_button.grid(column=2, row=3)

        self.authentication_button = Button(text="Authentication", command=self.authentication_window, width=50,
                                            font=FONT, background=BACKGROUND)
        self.authentication_button.grid(column=0, row=10, columnspan=2)

        self.window.mainloop()

    def api_call(self):
        api_call(
            self.get_steps(),
            self.get_width(),
            self.get_height(),
            self.get_seed(),
            self.get_cfg(),
            self.get_style(),
            self.get_prompt(),
            self.api_key
        )

    def randomize_seed(self):
        new_seed = random_seed()
        self.seed_entry.delete(0, END)
        self.seed_entry.insert(0, new_seed)

    def show_image_button(self):
        seed = self.get_seed()
        show_image(seed)

    def authentication_window(self):
        self.new_window = Toplevel()
        self.new_window.title("Authentication Window")
        self.new_window.config(background=BACKGROUND, padx=30, pady=20)

        self.authentication_label = Label(self.new_window, text="API KEY:", font=FONT, background=BACKGROUND)
        self.authentication_label.grid(column=0, row=0)
        self.authentication_entry = Entry(self.new_window, width=40, font=FONT,background=BACKGROUND, show='*')
        self.authentication_entry.grid(column=1, row=0)

        self.save_api_key_button = Button(self.new_window, text="Save Key", command=self.save_api_key, width=50,
                                     font=FONT, background=BACKGROUND)
        self.save_api_key_button.grid(column=0, row=1, columnspan=2)

    def save_api_key(self):
        api_key = self.get_api_key()
        save_api_key(api_key)

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

    def get_api_key(self):
        return str(self.authentication_entry.get())
