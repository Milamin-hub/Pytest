import test46
from PIL import Image, ImageDraw
from PIL import ImageFilter

print(Image.__version__)

f = open("tmp.jpg", "rb")
img = Image.open(f)
print(img)

img_1 = Image.open("tmp.jpg")
obj = img_1.load()
print(obj[1,3])

# img.show() Просматриваем изображение

img.save("tmp.bmp") # Меняет формат

# ♦ 1 — 1 бит, черно-белое;
# ♦ L — 8 битов, черно-белое;
# ♦ P — 8 битов, цветное (256 цветов);
# ♦ RGB — 24 бита, цветное;
# ♦ RGBA — 32 бита, цветное с альфа-каналом ;
# ♦ CMYC — 32 бита, цветное;
# ♦ YCbCr — 24 бита, цветное, видеоформат;
# ♦ LAB — 24 бита, цветное, используется цветное пространство Lab;
# ♦ HSV — 24 бита, ц ветное, используется цветное пространство HSV ;
# ♦ I — 32 бита, цветное, цвета кодируются целыми числами;
# ♦ F — 32 бита, цветное, цвета кодируются вещественными числами;

size = (100, 100)
color_grey = (100, 100, 100)

img_2 = Image.new("RGB", size, color_grey)

# ♦ width и height — соответственно, ширина и высота изображения в пикселах;
# ♦ size — размеры изображения в пикселах в виде кортежа из двух элементов (width, height);
# ♦ format — формат изображения в виде строки (например: 'gif', 'jpeg' и т.д.);
# ♦ mode — режим в виде строки (например: 'P', 'RGB', 'CMYK' и т.д.);
# ♦ filename — путь к файлу с изображением;
# ♦ info — дополнительная информация об изображении в виде словаря;

mode_img = img.size, img.format, img.mode
print(mode_img)

img_3 = img.copy()

# ♦ thumbnail (<Размер>[,<Фильтр>]) — создает уменьшенную версию изображения указанного размера
# В параметре <Фильтр> могут быть указаны фильтры (NEAREST, BILINEAR, BICUBIC или LANCZOS). 
# Если параметр не указан, используется значение BICUBIC

img_3.thumbnail((400, 300), Image.LANCZOS)

# ♦ resize (<Размер>[, <Фильтр>]) — изменяет размер изображения. 
# В отличие от метода thumbnail о возвращает новое изображение, а не изменяет исходное

img_4 = img.resize((200, 300), Image.LANCZOS)

# ♦ rotate() - поворачивает изображение на указанный угол, отмеряемый в градусах против часовой стрелки

img_4 = img.rotate(180)

# ♦ crop([<X1>, <Y1 >, <X2>, <Y2>]) — вырезает прямоугольный фрагмент из исходного изображения

img_5 = img.crop( [0, 0, 450, 500] )

# ♦ paste(<Цвет>, <Область>[, mask=None]) — закрашивает прямоугольную область определенным цветом

# ♦ filter (<Фильтр>) — применяет к изображению указанный фильтр
# фильтры BLUR , CONTOUR , DETAIL , EDGE_ENHANCE, EDGE_ENHANCE_MORE, 
# EMBOSS, FIND_EDGES, SHARPEN, SMOOTH И SMOOTH_MORE

img2 = Image.open("tmp.jpg")
img3 = img2.filter(ImageFilter. EMBOSS)

img = Image.new ("RGB", (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img)
for n in range (5, 31):
    draw.point((n, 150), fill=(0, 0, 0))


# ♦ line() — проводит линию между двумя точками:

draw.line((100, 200, 100, 300), fill=(0, 0, 0))
# ♦ rectangle () — рисует прямоугольник.

draw.rectangle((10, 10, 30, 30), fill=(0, 0, 0), outline=(0, 0, 0))

# ♦ polygon() — рисует многоугольник.

draw.polygon ((50, 150, 50, 0, 150, 150), outline=(100,100,100), fill=(200, 200, 200))

# ♦ ellipse() — рисует эллипс

draw.ellipse((100, 100, 200, 200), outline=(0,0,0), fill=(155, 155, 155))

# ♦ arc() — рисует дугу

draw.arc((10, 10, 290, 290), 180, 0, fill=(255, 0, 0))

# ♦ chord() — рисует дугу и замыкает ее крайние точки прямой линией

draw.chord((10, 10, 290, 290), -90, 0, fill=(255, 255, 0))

#  pieslice() — рисует дугу и замыкает ее с центром окружности, создавая замкнутый сектор.

draw.pieslice( (10, 10, 290, 290), -90, 0, fill="red")


img.show()