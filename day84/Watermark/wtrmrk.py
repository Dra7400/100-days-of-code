from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import random
from PIL import Image, ImageDraw, ImageFont

FONT_NAME = "Courier"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

root = Tk()
root.title('IMG_WATERMARK')
root.config(padx=25, pady=25)
img_file = ''


def watermark(img_file, img_output, text_watermark, xy_pos):
    image = Image.open(img_file).convert("RGBA")
    txt = Image.new('RGBA', image.size, (255,255,255,0))

    edit_image = ImageDraw.Draw(txt)

    font_watermark = ImageFont.truetype("arial.ttf", 400)
    width, height = image.size
    textwidth, textheight = edit_image.textsize(text_watermark, font_watermark)
    x=width/2-textwidth/2
    y=height-textheight-300
    edit_image.text((x,y), text_watermark, font=font_watermark, fill=(255,255,255, 125))

    marked_image = Image.alpha_composite(image, txt)
    marked_image.show()
    marked_image.save(img_output)


def select_file():
    global img_file
    img_file = askopenfilename()


def watermark_img():
    if img_file == '':
        messagebox.showerror("No image found", "Please select an image first.")
    else:
        img_output = r'watermarked.png'
        text_watermark = text_entry.get()
        watermark(img_file, img_output, text_watermark=text_watermark, xy_pos=(2, 300))
        messagebox.showinfo("Complete", "Successfully watermarked!")


title_label = Label(text="IMG Watermark", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=0, row=1, rowspan=4)

b1 = Button(root, text="1. Select IMG", highlightbackground='blue', font=20, width=15,
            command=select_file)
b2 = Button(root, text="3. Watermark IMG", highlightbackground='blue', font=20, width=15,
            command=watermark_img)
b1.grid(column=1, row=1, columnspan=2, padx=25, pady=25)
b2.grid(column=1, row=4, columnspan=2, padx=25, pady=25)

text_label = Label(text="2. Watermark Text", font=20)
text_label.grid(column=1, row=2, padx=25, pady=25)
text_entry = Entry(width=26)
text_entry.grid(column=1, row=3)

root.mainloop()