import sys, os.path
arr = sys.argv[:] # Сохраняет в переменную имя файла
print(arr)
for n in arr:
    n_1 = list(n)
    n_2 = list(n)
    n_2 = n[4:6]
    n_2 = str(int(n_2) + 1)
    n_1 = n_1[0:4]
    n_1 = "".join(n_1)
    v_1 = n_1 + n_2 + "." + "py"


try:
    opath_1 = os.path.abspath(v_1)
    open(opath_1)
except:
    with open("{0}".format(v_1), "a", encoding="utf-8") as f:
        f.write("import test46\n") # Записываем строку в конец файл


