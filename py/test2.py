import encodings.aliases

arr = encodings.aliases.aliases

keys = list(arr.keys())

keys.sort()

for key in keys :
    print("%s => %s" % (key, arr[key]))

"""
/r (перевод каретки) (Windows)
/n (перевод строки) (системы Unix и Windows)

"""
