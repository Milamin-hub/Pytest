from bs4 import BeautifulSoup
import test46, test53

""" Последние обновления на сайте"""

test53.createfile()

with open("test1.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

title = soup.title.text
print("Название сайта: " + "%s" % title + "\n")

page_h2 = soup.find_all("h2")
l_i = []

for item in page_h2:
    l_i.append(item)
    for i in range(len(l_i)):
        print(end="")
    print("%s" % i + ". " + "%s" % item.text.strip())

test53.removefile()
