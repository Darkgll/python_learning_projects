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


class Watermarking:
    def __init__(self):
        self.image = None
        self.font_name = 'arial'
        self.font_size = 36

    def change_font(self, size_of_font):
        if size_of_font:
            self.font_size = int(size_of_font)
        else:
            print("Write the font size")

    def make_watermark(self, image, watermark):
        self.image = image
        if image:
            if watermark:
                self.image = Image.open(f"img/{image}")
                width, height = self.image.size

                draw = ImageDraw.Draw(self.image)
                text = watermark_text.get()

                font = ImageFont.truetype(f'{self.font_name}.ttf', self.font_size)
                text_width, text_height = draw.textsize(text, font)

                # calculate the x,y coordinates of the text
                margin = 10
                x = width - text_width - margin
                y = height - text_height - margin

                # draw watermark in the bottom right corner
                draw.text((x, y), text, font=font)

            else:
                print("Write the watermark text")
        else:
            print("Write the name of an image")

    def show_im(self, image, watermark):
        self.make_watermark(image, watermark)
        self.image.show()

    # Save watermarked image
    def save_im(self, image, watermark):
        self.make_watermark(image, watermark)
        self.image.save('img/watermark.jpg')


watermarking_image = Watermarking()


# ---------------------------- GUI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Watermark a(o)n Image")
window.config(padx=50, pady=50, bg="white")

canvas = tkinter.Canvas(width=800, height=400, bg="white", highlightthickness=0)
image_preview = tkinter.PhotoImage(file="bg-1.png")
image_bg = canvas.create_image(400, 100, image=image_preview)
canvas.grid(row=0, column=0, columnspan=2)

how_to_text_1 = canvas.create_text(400, 260, text='1) Drop an image to "img" folder',
                                 font=("Courier", 14, "bold"))
how_to_text_2 = canvas.create_text(400, 300, text='2) Fill the forms below',
                                 font=("Courier", 14, "bold"))
how_to_text_3 = canvas.create_text(400, 360, text="-----------------------------\nDefault font: 'arial', 36",
                                 font=("Courier", 14, "bold"))

image_name_label = tkinter.Label(text="Image name (with extension)", font=("Arial", 14), highlightthickness=1, bg="white", pady=10)
image_name_label.grid(row=1, column=0)
image_name = tkinter.Entry(width=40, highlightthickness=1)
image_name.grid(row=1, column=1)

watermark_label = tkinter.Label(text="Watermark text", font=("Arial", 14), highlightthickness=1, bg="white", pady=10)
watermark_label.grid(row=3, column=0)

watermark_text = tkinter.Entry(width=40, highlightthickness=1)
watermark_text.grid(row=3, column=1)

# watermarking options
options_test = tkinter.Label(text="You may change options of watermarking", font=("Arial", 14),
                             highlightthickness=1, bg="white", pady=10)
options_test.grid(row=4, column=0, columnspan=2)

# font_type = tkinter.Label(text="FONT TYPE", font=("Arial", 14), highlightthickness=1, bg="white", pady=10)
# font_type.grid(row=5, column=0)
#
# font_type_text = tkinter.Entry(width=40, highlightthickness=1)
# font_type_text.grid(row=5, column=1)

font_size = tkinter.Label(text="FONT SIZE", font=("Arial", 14), highlightthickness=1, bg="white", pady=10)
font_size.grid(row=7, column=0)

font_size_text = tkinter.Entry(width=40, highlightthickness=1)
font_size_text.grid(row=7, column=1)

change_font_b = tkinter.Button(text="Change FONT", font=("Arial", 14),
                               command=lambda: watermarking_image.change_font(font_size_text.get()), highlightthickness=0)
change_font_b.grid(row=8, column=0, columnspan=2)

# final steps
preview_b = tkinter.Button(text="Preview", font=("Arial", 14),
                           command=lambda: watermarking_image.show_im(image_name.get(), watermark_text.get()),
                           highlightthickness=0)
preview_b.grid(row=9, column=0, columnspan=2)

convert_b = tkinter.Button(text="Make a Watermark", font=("Arial", 14),
                           command=lambda: watermarking_image.save_im(image_name.get(), watermark_text.get()),
                           highlightthickness=0)
convert_b.grid(row=10, column=0, columnspan=2)


window.mainloop()
