
import hashlib as hasher

sifreleyici = hasher.md5()
metin=str(input("Sifrelemek istediğiniz seyi giriniz="))
sifreleyici.update(metin.encode("utf-8"))
hash = sifreleyici.hexdigest()
print(hash)