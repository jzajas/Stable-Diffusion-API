import base64
import configparser

import requests
import random
import glob
import os
from tkinter import *
from PIL import Image, ImageTk
import subprocess

URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
CONFIG_FILE = 'config.ini'
# API_KEY = os.environ['STABILITY_KEY']


def api_call(steps, width, height, seed, cfg_scale, style_preset, text_prompt, API_KEY):
    body = {
        "steps": int(steps),
        "width": int(width),
        "height": int(height),
        "seed": int(seed),
        "cfg_scale": float(cfg_scale),
        "samples": 1,
        "style_preset": style_preset,
        "text_prompts": [
            {
                "text": text_prompt,
                "weight": 1
            },
            {
                "text": "bad, blurry",
                "weight": -1
            }
        ],
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    response = requests.post(
        URL,
        headers=headers,
        json=body,
    )

    if response.status_code != 200:
        print(f"HTTP {response.status_code}: {response.text}")
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    if not os.path.exists("./out"):
        os.makedirs("./out")

    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/{body["seed"]}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))

    show_image(body["seed"])


def show_image(seed):
    new_window = Toplevel()
    new_window.title("Display PNG Image")

    img = Image.open(f'./out/{int(seed)}.png')
    # img = img.resize((1024, 512), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    image_label = Label(new_window, image=img_tk)
    image_label.image = img_tk
    image_label.grid(column=0, row=10, columnspan=2)

    new_window.mainloop()


def random_seed():
    random_int = random.randint(0, 2147483647)
    files = glob.glob(os.path.join("./out", '*.png'))
    file_name = f"{random_int}.png"
    filenames = [os.path.basename(file) for file in files]

    if str(file_name) in filenames:
        random_seed()

    return int(random_int)


def open_folder():
    folder_path = os.path.abspath('./out')
    if not os.path.exists(folder_path):
        os.makedirs("./out")

    subprocess.Popen(['explorer', folder_path])


def save_api_key(api_key):
    if api_key:
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'API_KEY': api_key}
        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)


def load_api_key():
    if os.path.exists(CONFIG_FILE):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        api_key = config['DEFAULT'].get('API_KEY', '')
        return api_key
