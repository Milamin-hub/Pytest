import test46
from PIL import Image, ImageDraw, ImageFont

# ♦ load_default() - шрифт по умолчанию (вывести символы кириллицы таким шрифтом нельзя — возникнет ошибка)

x = 10
y = 10

img = Image.new ("RGB", (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((x, y), "Hello", font=font, fill="black")

img.show()

