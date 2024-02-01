#! /usr/bin/python3
from PIL import Image
import os

def resizer(in_folder, out_folder):
    for count, filename in enumerate(os.listdir(in_folder)):
        if filename[-4:] == ".jpg":
            image = Image.open(f"{in_folder}/{filename}")
            new_image = image.resize((1280,1280))
            new_image.save(f"{out_folder}/{filename}")
            print(image.size)
            print(new_image.size)
        else:
            print(f"wrong file ending: {filename}")

if __name__ == '__main__':
    resizer("/home/treenut/repos/ai_project1/data",
            "/home/treenut/repos/ai_project1/resized_data")
