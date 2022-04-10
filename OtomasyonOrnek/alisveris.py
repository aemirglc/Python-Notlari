import time
import price as pr


class main:
    def __init__(self):
        self.sepet = {}
        self.toplam_fiyat = 0
        self.onaylanan_urun = []
        self.onaylanan_urun_fiyat = []
        self.ana_menu()

    def ana_menu(self):
        print("""
----------------------------------
Gitmek istediğiniz ekranı seçiniz.
----------------------------------
1- Siparişlerim
2- Sepetim
3- Alışveriş
----------------------------------
                """)
        secim = input("Seçiminizi yapınız: ")
        if secim == "1":
            self.info()
        elif secim == "2":
            self.sepet_menu()
        elif secim == "3":
            self.kategori_listesi()

        else:
            print("""
----------------------------------
Geçersiz Seçim Yaptınız.
----------------------------------
                    """)
            self.ana_menu()




    def onay_menu(self):
        self.onaylanan_urun.append(self.sepet)
        self.onaylanan_urun_fiyat.append(self.toplam_fiyat)
        self.sepet = {}
        self.toplam_fiyat = 0
        self.ana_menu()





    #1.Ekran



    def info(self):
        counter = 0
        counter_for_price = 0
        for i in self.onaylanan_urun:
            print(f"{counter+1} - {i} ")
            print(f"Toplam fiyat {self.onaylanan_urun_fiyat[counter]}"),
            counter += 1
        secim = input("Devam etmek için entera basınız: ")
        self.ana_menu()


    # 2.Ekran

    def sepet_menu(self):
        sepettekiler = []
        fiyatlar = []
        print("Sepetinizde bulunan ürünler:")
        counter = 1
        for i,j in self.sepet.items():
            print(f"{counter} - {i} - {j} ₺")
            counter += 1
            sepettekiler.append(i)
            fiyatlar.append(j)

        print(f"Toplam fiyat: {self.toplam_fiyat}")

        secim = input("""
-----------------------------------------------------------------------------------
Sepetinizden çıkartmak istediğiniz bir ürün var ise, ürün numarasını yazabilirsiniz.
Sepetinizi onaylamak için 'onayla' yazabilirsiniz.
Üst menüye dönmek için "Enter"a basabilirsiniz.
-----------------------------------------------------------------------------------
                """)


        try:
            if secim == "onayla":
                self.onay_menu()

            elif secim == "":
                time.sleep(1)
                self.ana_menu()

            elif int(secim) <= len(sepettekiler):
                self.sepet.pop(sepettekiler[int(secim)-1])
                self.toplam_fiyat -= fiyatlar[int(secim)-1]
                del fiyatlar[int(secim)-1]
                del sepettekiler[int(secim)-1]
                self.sepet_menu()

            else:
                print("""
-----------------------------------
Geçersiz seçim yaptınız.
-----------------------------------
                """)
                self.sepet_menu()

        except:
            print("""
----------------------------------
Geçersiz Seçim Yaptınız.
----------------------------------
                                """)
            self.sepet_menu()




    # 3.Ekran

    def kategori_listesi(self):
        print("""
----------------
Kategori Listesi
----------------    
1.Elektronik
2.Giyim
3.Gıda
4.Beyaz Eşya
5.Kırtasiye
6.Üst Menü
----------------
     """)
        secim = input("Seçiminizi giriniz: ")
        if secim == "1":
            print("Elektronik kategorisi seçildi.")
            time.sleep(1)
            self.elektronik()
        elif secim == "2":
            print("Giyim kategorisi seçildi.")
            time.sleep(1)
            self.giyim()
        elif secim == "3":
            print("Gıda kategorisi seçildi.")
            time.sleep(1)
            self.gida()
        elif secim == "4":
            print("Beyaz Eşya kategorisi seçildi.")
            time.sleep(1)
            self.beyaz_esya()
        elif secim == "5":
            print("Kırtasiye kategorisi seçildi.")
            time.sleep(1)
            self.kirtasiye()
        elif secim == "6":
            print("Üst Menüye dönülüyor.")
            time.sleep(1)
            self.ana_menu()
        else:
            print("Hatalı seçim yaptınız.")
            time.sleep(1)
            self.kategori_listesi()

    def elektronik(self):
        print(f"""
----------------------------------
Elektronik Ürünleri
----------------------------------
1.Telefon - {pr.telefon} ₺
2.Tablet - {pr.tablet} ₺
3.Bilgisayar - {pr.bilgisayar} ₺
4.Kulaklık - {pr.kulaklik} ₺
5.Televizyon - {pr.televizyon} ₺
6.Üst Menüye dön
----------------------------------
        """)
        secim = input("Seçiminizi giriniz: ")
        if secim == "1":
            print("Telefon seçildi.")
            time.sleep(1)
            self.sepet["Telefon"] = pr.telefon
            self.toplam_fiyat += pr.telefon
            self.elektronik()

        elif secim == "2":
            print("Tablet seçildi.")
            time.sleep(1)
            self.sepet["Tablet"] = pr.tablet
            self.toplam_fiyat += pr.tablet
            self.elektronik()

        elif secim == "3":
            print("Bilgisayar seçildi.")
            time.sleep(1)
            self.sepet["Bilgisayar"] = pr.bilgisayar
            self.toplam_fiyat += pr.bilgisayar
            self.elektronik()

        elif secim == "4":
            print("Kulaklık seçildi.")
            time.sleep(1)
            self.sepet["Kulaklık"] = pr.kulaklik
            self.toplam_fiyat += pr.kulaklik
            self.elektronik()

        elif secim == "5":
            print("Televizyon seçildi.")
            time.sleep(1)
            self.sepet["Televizyon"] = pr.televizyon
            self.toplam_fiyat += pr.televizyon
            self.elektronik()

        elif secim == "6":
            print("Üst menüye dönülüyor.")
            time.sleep(1)
            self.kategori_listesi()

        else:
            print("Hatalı seçim yaptınız.")
            time.sleep(1)
            self.elektronik()

    def giyim(self):
        print(f"""
----------------------------------
Giyim Ürünleri
----------------------------------
1.Tişört - {pr.tisort} ₺
2.Ayakkabı - {pr.ayakkabi} ₺
3.Sweat - {pr.sweat} ₺
4.Pantolon - {pr.pantolon} ₺
5.Mont - {pr.mont} ₺
6.Üst Menüye dön
----------------------------------
        """)
        secim = input("Seçiminizi giriniz: ")
        if secim == "1":
            print("Tişört seçildi.")
            time.sleep(1)
            self.sepet["Tişört"] = pr.tisort
            self.toplam_fiyat += pr.tisort
            self.giyim()

        elif secim == "2":
            print("Ayakkabı seçildi.")
            time.sleep(1)
            self.sepet["Ayakkabı"] = pr.ayakkabi
            self.toplam_fiyat += pr.ayakkabi
            self.giyim()

        elif secim == "3":
            print("Sweat seçildi.")
            time.sleep(1)
            self.sepet["Sweat"] = pr.sweat
            self.toplam_fiyat += pr.sweat
            self.giyim()

        elif secim == "4":
            print("Pantolon seçildi.")
            time.sleep(1)
            self.sepet["Pantolon"] = pr.pantolon
            self.toplam_fiyat += pr.pantolon
            self.giyim()

        elif secim == "5":
            print("Mont seçildi.")
            time.sleep(1)
            self.sepet["Mont"] = pr.mont
            self.toplam_fiyat += pr.mont
            self.giyim()

        elif secim == "6":
            print("Üst menüye dönülüyor.")
            time.sleep(1)
            self.kategori_listesi()

        else:
            print("Hatalı seçim yaptınız.")
            time.sleep(1)
            self.giyim()

    def gida(self):
        print(f"""
----------------------------------
Gıda Ürünleri
----------------------------------
1.Kola - {pr.kola} ₺
2.Peynir - {pr.peynir} ₺
3.Yağ - {pr.yag} ₺
4.Tereyağı - {pr.tereyagi} ₺
5.Yumurta - {pr.yumurta} ₺   
6.Üst Menüye dön
----------------------------------
        """)
        secim = input("Seçiminizi giriniz: ")
        if secim == "1":
            print("Kola seçildi.")
            time.sleep(1)
            self.sepet["Kola"] = pr.kola
            self.toplam_fiyat += pr.kola
            self.gida()

        elif secim == "2":
            print("Peynir seçildi.")
            time.sleep(1)
            self.sepet["Peynir"] = pr.peynir
            self.toplam_fiyat += pr.peynir
            self.gida()

        elif secim == "3":
            print("Yağ seçildi.")
            time.sleep(1)
            self.sepet["Yağ"] = pr.yag
            self.toplam_fiyat += pr.yag
            self.gida()

        elif secim == "4":
            print("Tereyağı seçildi.")
            time.sleep(1)
            self.sepet["Tereyağı"] = pr.tereyagi
            self.toplam_fiyat += pr.tereyagi
            self.gida()

        elif secim == "5":
            print("Yumurta seçildi.")
            time.sleep(1)
            self.sepet["Yumurta"] = pr.yumurta
            self.toplam_fiyat += pr.yumurta
            self.gida()

        elif secim == "6":
            print("Üst menüye dönülüyor.")
            time.sleep(1)
            self.kategori_listesi()

        else:
            print("Hatalı seçim yaptınız.")
            time.sleep(1)
            self.gida()

    def beyaz_esya(self):
        print(f"""
----------------------------------
Beyaz Eşya Ürünleri
----------------------------------
1.Buzdolabı - {pr.buzdolabi} ₺
2.Çamaşır Makinesi - {pr.camasir_makinesi} ₺
3.Bulaşık Makinesi - {pr.bulasik_makinesi} ₺
4.Klima - {pr.klima} ₺
5.Fırın - {pr.firin} ₺
6.Üst Menüye dön
----------------------------------
        """)
        secim = input("Seçiminizi giriniz: ")
        if secim == "1":
            print("Buzdolabı seçildi.")
            time.sleep(1)
            self.sepet["Buzdolabı"] = pr.buzdolabi
            self.toplam_fiyat += pr.buzdolabi
            self.beyaz_esya()

        elif secim == "2":
            print("Çamaşır Makinesi seçildi.")
            time.sleep(1)
            self.sepet["Çamaşır Makinesi"] = pr.camasir_makinesi
            self.toplam_fiyat += pr.camasir_makinesi
            self.beyaz_esya()

        elif secim == "3":
            print("Bulaşık Makinesi seçildi.")
            time.sleep(1)
            self.sepet["Bulaşık Makinesi"] = pr.bulasik_makinesi
            self.toplam_fiyat += pr.bulasik_makinesi
            self.beyaz_esya()

        elif secim == "4":
            print("Klima seçildi.")
            time.sleep(1)
            self.sepet["Klima"] = pr.klima
            self.toplam_fiyat += pr.klima
            self.beyaz_esya()

        elif secim == "5":
            print("Fırın seçildi.")
            time.sleep(1)
            self.sepet["Fırın"] = pr.firin
            self.toplam_fiyat += pr.firin
            self.beyaz_esya()

        elif secim == "6":
            print("Üst menüye dönülüyor.")
            time.sleep(1)
            self.kategori_listesi()

        else:
            print("Hatalı seçim yaptınız.")
            time.sleep(1)
            self.beyaz_esya()

    def kirtasiye(self):
        print(f"""
----------------------------------
Kırtasiye Ürünleri
----------------------------------
1.Kalem - {pr.kalem} ₺
2.Defter - {pr.defter} ₺
3.Kitap - {pr.kitap} ₺
4.Silgi - {pr.silgi} ₺
5.Kalemlik - {pr.kalemlik} ₺
6.Üst Menüye dön
----------------------------------
        """)
        secim = input("Seçiminizi giriniz: ")
        if secim == "1":
            print("Kalem seçildi.")
            time.sleep(1)
            self.sepet["Kalem"] = pr.kalem
            self.toplam_fiyat += pr.kalem
            self.kirtasiye()

        elif secim == "2":
            print("Defter seçildi.")
            time.sleep(1)
            self.sepet["Defter"] = pr.defter
            self.toplam_fiyat += pr.defter
            self.kirtasiye()

        elif secim == "3":
            print("Kitap seçildi.")
            time.sleep(1)
            self.sepet["Kitap"] = pr.kitap
            self.toplam_fiyat += pr.kitap
            self.kirtasiye()

        elif secim == "4":
            print("Silgi seçildi.")
            time.sleep(1)
            self.sepet["Silgi"] = pr.silgi
            self.toplam_fiyat += pr.silgi
            self.kirtasiye()

        elif secim == "5":
            print("Kalemlik seçildi.")
            time.sleep(1)
            self.sepet["Kalemlik"] = pr.kalemlik
            self.toplam_fiyat += pr.kalemlik
            self.kirtasiye()

        elif secim == "6":
            print("Üst menüye dönülüyor.")
            time.sleep(1)
            self.kategori_listesi()

        else:
            print("Hatalı seçim yaptınız.")
            time.sleep(1)
            self.kirtasiye()