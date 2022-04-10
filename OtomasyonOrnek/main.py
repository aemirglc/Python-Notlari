import time
import alisveris as al
import account


while True:
    kullanici_adi = input("Kullanıcı Adı: ")
    sifre = input("Şifre: ")

    if kullanici_adi == account.kullanici_adi and sifre == account.sifre:
        print("""
-------------------------------------------------
Giriş Başarılı. Ana sayfaya yönlendiriliyorsunuz.
-------------------------------------------------
                """)
        time.sleep(1)
        al.main()

    else:
        print("""
-----------------------------------------
Giriş başarısız, şifre veya parola hatalı.
------------------------------------------
    """)
        time.sleep(1)