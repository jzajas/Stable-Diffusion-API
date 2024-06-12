import base64
import requests
import os
from tkinter import *
from PIL import Image, ImageTk
import glob

URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
API_KEY = os.environ['STABILITY_KEY']


def api_call(steps, width, height, seed, cfg_scale, style_preset, text_prompt):
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
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    if not os.path.exists("./out"):
        os.makedirs("./out")

    # try:
    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/{body["seed"]}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))
    # except KeyError:
    #     body["seed"] = find_seed("./out")

    show_image(body["seed"])


def show_image(seed):
    print(seed)
    new_window = Toplevel()
    new_window.title("Display PNG Image")

    img = Image.open(f'./out/{int(seed)}.png')
    img = img.resize((512, 512), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    image_label = Label(new_window, image=img_tk)
    image_label.image = img_tk
    image_label.grid(column=0, row=10, columnspan=2)

    new_window.mainloop()


def find_seed(folder_path):
    files = glob.glob(os.path.join(folder_path, '*'))

    if not files:
        return None

    most_recent_file = max(files, key=os.path.getmtime)
    most_recent_filename = os.path.basename(most_recent_file)
    most_recent_filename_without_extension = os.path.splitext(most_recent_filename)[0]

    return most_recent_filename_without_extension
