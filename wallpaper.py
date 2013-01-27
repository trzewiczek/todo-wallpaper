import Image
import ImageDraw
import ImageFont
import os

# config parser for all
# TODO multiple wallpaper sizes
img  = Image.new('RGB', (1024, 768), (40, 40, 40))
draw = ImageDraw.Draw(img)
# TODO choose font
font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 18, encoding="unic")

# custom filepaths
for i, line in enumerate(open('todo.txt')):
    # TODO different positions
    # TODO relative positions
    # TODO antialiasing
    draw.text((650, (i*20)+50), line.strip().decode('utf-8'), font=font, fill=(200,200,200))

img.save("wallpaper.png")

# TODO different environments
os.system("xfdesktop --reload")
