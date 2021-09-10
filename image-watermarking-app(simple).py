import tkinter
from PIL import Image, ImageDraw, ImageFont

# Using what you have learnt about Tkinter, you will create a desktop application with a Graphical User Interface (GUI)
# where you can upload an image and use Python to add a watermark logo/text.
# Normally, you would have to use an image editing software like Photoshop to add the watermark, but your program is
# going to do it automatically.
# Use case: e.g you want to start posting your photos to Instagram but you want to add your website to all
# the photos, you can now use your software to add your website/logo automatically to any image.

# A similar online service is: https://watermarkly.com/

# You might need:
# https://pypi.org/project/Pillow/
# https://docs.python.org/3/library/tkinter.html
# and some Googling.


# ---------------------------- work with an image ------------------------------- #

def make_watermark():
    print(image_name)
    im = Image.open(f"img/{image_name.get()}")
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = watermark_text.get()

    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    im.show()

    #Save watermarked image
    im.save('img/watermark.jpg')


# ---------------------------- GUI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Watermark a(o)n Image")
window.config(padx=50, pady=50, bg="white")

canvas = tkinter.Canvas(width=500, height=300, bg="white", highlightthickness=0)
image_preview = tkinter.PhotoImage(file="bg-1.png")
canvas.create_image(250, 100, image=image_preview)
canvas.grid(row=0, column=0)

how_to_text_1 = canvas.create_text(250, 250, text='1) Drop an image to "img" folder',
                                 font=("Courier", 14, "bold"))
how_to_text_2 = canvas.create_text(250, 280, text='2) Write the name of an image, with extension',
                                 font=("Courier", 14, "bold"))

image_name = tkinter.Entry(width=30, highlightthickness=1)
image_name.grid(row=1, column=0)

watermark_label = tkinter.Label(text="\nWatermark text", font=("Arial", 14), highlightthickness=1, bg="white", pady=10)
watermark_label.grid(row=2, column=0)

watermark_text = tkinter.Entry(width=40, highlightthickness=1)
watermark_text.grid(row=3, column=0)

convert_b = tkinter.Button(text="Make a Watermark", command=make_watermark, highlightthickness=0)
convert_b.grid(row=4, column=0)



window.mainloop()
