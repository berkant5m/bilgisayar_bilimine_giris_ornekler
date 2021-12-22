# Maraton idman asistanı.
import math 
def toplam_saniye(dk, sn):
    return dk * 60 + sn
def hiz(time):
    return 3600 / time
sure_dk = int(input("1 mil için gerekli dakika? "))
sure_sn = int(input("1 mil için gerekli saniye? "))
mesafe = int(input("Toplam mesafe?"))
mph = hiz(toplam_saniye(sure_dk, sure_sn))
print("Hiiziniz")
print(mph)
total = mesafe * toplam_saniye(sure_dk, sure_sn)
gecen_dakika = toplam // 60
gecen_saniye = toplam % 60
print("Toplam gecen sure")
print(gecen_dakika)
print(gecen_saniye)
