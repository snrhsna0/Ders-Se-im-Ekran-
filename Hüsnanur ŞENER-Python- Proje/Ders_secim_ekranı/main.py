from ogrenci_yonetimi import Ogrenci
from ders_yonetimi import Ders
import donem_kaydi_yonetimi as dky




def secenekleri_sun():
    print("""\n1-liste almak için (1)
             \n2-ders kaydı için (2)
             \n3-çıkış için (3)  """)

def uygulama_baslat():
    while True:
        secenekleri_sun()
        secenek = input(":")

        if secenek == "1":
            dky.ders_kayitlarini_getir()
        elif secenek == "2":
            ogrenci = Ogrenci()
            ogrenci.ogrenci_no=input("ogrenci no giriniz")
            ogrenci.ogrenci_adi=input("ogrenci adı giriniz")
      
            ders = Ders()
            ders.ders_kodu=input("ders kodu giriniz: ")
            ders.ders_adi=input("ders adi giriniz: ")
            
            

            sonuc = dky.donem_kaydet(ders=ders,ogrenci=ogrenci,donem_yili= 2022,donem=2)
            if sonuc:
                print("işlem başarılı")
            else:
                print("sorun yaşanıyor")
            

        elif secenek == "3":
            print("İyi Günler...")
            break
        else:
            print("lütfen doğru seçeneği giriniz")



if __name__ == "__main__":
    print("uyugulamamıza hosgeldiniz. v1.23")
    uygulama_baslat()
else:
    print("Bu uygulama module olarak kullanılamaz.")