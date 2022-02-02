from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from pytz import timezone
import os

import config


def get_current_time():
    return datetime.now(timezone('Asia/Tehran')).strftime('%H:%M')


def generate_image(text):
    image = Image.open(os.getcwd() + config.photo_filename)
    W, H = image.size
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font='resources/ds-digit.TTF', size=150)
    wt, ht = draw.textsize(text, font=font)

    border_size = config.image_border_size
    border_color = config.image_border_color

    draw.text(((W - wt) / 2 - border_size, (H - ht) / 1.25 - border_size), text, font=font, fill=border_color)
    draw.text(((W - wt) / 2 + border_size, (H - ht) / 1.25 - border_size), text, font=font, fill=border_color)
    draw.text(((W - wt) / 2 - border_size, (H - ht) / 1.25 + border_size), text, font=font, fill=border_color)
    draw.text(((W - wt) / 2 + border_size, (H - ht) / 1.25 + border_size), text, font=font, fill=border_color)

    draw.text(((W - wt) / 2, (H - ht) / 1.25), text, font=font, fill=config.image_text_color)

    image.save(config.image_filename)


def delete_image():
    os.remove(config.image_filename)


