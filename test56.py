import test46
from wand.image import Image as WandImage
from wand.drawing import Drawing
from wand.color import Color
from wand.display import display

img = WandImage(width=400, height=300, background=Color("white"))
draw = Drawing()

draw.stroke_color = Color("black")
draw.line((0, 0), (400, 300))
draw.rectangle(left=300, top=0, width=50, height=100, xradius=5, yradius=15)
draw.polygon([ (30, 50), (30, 30), (30, 20), (50, 20)])
draw.circle ( (20, 150), (10, 150))
draw.fill_color = Color("grey")
draw.ellipse( (50, 100), (10, 20))
draw.bezier([ (70, 167), (220, 109), (53, 390), (122, 14)])
draw.draw(img)
display(img)