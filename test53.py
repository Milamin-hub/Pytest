import test46, os
import requests

def createfile():
    try:
        opath_1 = os.path.abspath("test1.html")
        open(opath_1)
    except:
        html = requests.get("https://animevost.org/")
        file = open('test1.html', "ab")
        file.write(html.content)
        file.close()

def removefile():
    try:
        os.remove("test1.html")
    except:
        print("Файл не создан")