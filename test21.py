""" Шифрование строк """
import hashlib

h = hashlib.md5(b"pPass")
p = h.hexdigest()
print(p)

h2 = hashlib.md5(b"pPass")
if p == h2.hexdigest(): print("Пароль правильный")
else: print("Пароль неверный")