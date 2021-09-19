import test46
from wand.image import Image as Wandlmage
from wand.color import Color
from wand.drawing import Drawing
from PIL import Image, ImageDraw

# Сравнение рисунков двух библиотек

img = Wandlmage(width=400, height=300, background=Color("white"))
draw = Drawing()
draw.stroke_color = Color("red")
draw.fill_color = Color("white")
draw.circle((100, 100), (100, 0))
draw.draw(img)
img.save(filename="trip.bmp")
img = Image.open("trip.bmp")
draw = ImageDraw.Draw(img)
draw.ellipse((200, 0, 400, 200), fill="white", outline="red")
img.show()