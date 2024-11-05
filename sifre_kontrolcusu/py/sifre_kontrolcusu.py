def şifre_sızdırılmış_mı(dosya_konumu:str, şifre:str) -> bool:
    dosya:_io.TextIOWrapper = open(dosya_konumu, "r");
    yeni_satır:str = dosya.readline();
    while yeni_satır != "":
        yeni_satır = yeni_satır.split("\n")[0]; # Yeni satır karakterinden kurtulma vakti
        if(yeni_satır == şifre):
            return True;
        yeni_satır = dosya.readline();
    return False;

if(__name__ == "__main__"):
    dosya_konumu:str = input("Dosya Konumu: ");
    şifre:str = input("Kontrol Edilmesi İstenen Şifre: ");
    if(şifre_sızdırılmış_mı(dosya_konumu, şifre)):
        print("Şifre Sızdırılmış");
    else:
        print("Güvendesiniz, Henüz :)");
