from ders_yonetimi import Ders
from ogrenci_yonetimi import Ogrenci

class DonemKaydi():
    ders_kayitlari=[]
    def __init__(self, ders:Ders, ogrenci:Ogrenci, ders_yili:int, ders_donemi:int):
        self.ders=ders
        self.ogrenci = ogrenci
        self.ders_yili = ders_yili
        self.ders_donemi = ders_donemi
        self.ders_kayitlari.append(self)

    @classmethod
    def ders_listesi_getir(cls):
        return cls.ders_kayitlari
    
    def ogrenci_adini_getir(self) -> str:
        return self.ogrenci

    @classmethod
    def ders_kaydi_sil(cls, indeks_numarasi:int):
        cls.ders_kayitlari.pop(indeks_numarasi)



def donem_kaydet(ogrenci:Ogrenci, ders:Ders, donem_yili:int, donem:int) -> bool:
    DonemKaydi(ders,ogrenci,donem_yili,donem)
    print("Ders yılı kaydedildi")
    return True

def ders_kayitlarini_getir():
    template = "Indeks: {}, Ogrenci No: {}, Ders Kodu: {}, OğrenciAd: {}, Yıl: {}, Dönem: {}"
    indeks=1



    for donem_kaydi in DonemKaydi.ders_listesi_getir():
        print(template.format(indeks,donem_kaydi.ogrenci.ogrenci_no, donem_kaydi.ders.ders_kodu,
        donem_kaydi.ogrenci.ogrenci_adi,donem_kaydi.ders_yili,donem_kaydi.ders_donemi ))
        
        indeks = indeks + 1
   
        print("-----------------------------------------------------------------------------------")
