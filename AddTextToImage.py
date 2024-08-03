from PIL import Image, ImageFont, ImageDraw


class PostMaker:
    def __init__(self,
                 path):
        self.image = Image.open(path)
        self.weight, self.height = self.image.size

    def paste_add_image(self,
                        path,
                        multipier_size=0):
        image_add = Image.open(path)

        weight, height = image_add.size
        if multipier_size > 0:
            image_add = image_add.resize((weight * multipier_size, height * multipier_size))
        elif multipier_size < 0:
            image_add = image_add.resize((weight // abs(multipier_size), height // abs(multipier_size)))
        weight, height = self.image.size
        self.image.paste(image_add, ((weight - 380), (height - 250)), image_add)

    def add_text(self):
        font = ImageFont.truetype("arial.ttf", 50)
        draw = ImageDraw.Draw(self.image)
        draw.text((10, 10), 'I hate work', font=font, fill='white')

    def show(self):
        self.image.show()


image = PostMaker('images\\img_(15).jpg')
image.paste_add_image('images\\wing.png', -10)
image.add_text()
image.show()
