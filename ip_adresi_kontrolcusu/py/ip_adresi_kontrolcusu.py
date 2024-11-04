if(__name__ == "__main__"):
    ip_adresi:str = input("Kontrol etmek istediğiniz IPv4 adresini girin: ");
    bölünmüş_adres:list[str] = ip_adresi.split(".");
    sayısal_ip:list[int] = [0,0,0,0];

    try:
        if(len(bölünmüş_adres) != 4):
            raise Exception("");
        for indeks in range(4):
            sayısal_ip[indeks] = int(bölünmüş_adres[indeks]);
            if(sayısal_ip[indeks] < 0 or sayısal_ip[indeks] > 255):
                raise Exception("");
    except:
        print("Girilen IPv4 adresi tanıma uygun değil. IPv4 adresleri 0.0.0.0 ila 255.255.255.255 arasında olmak zorunda");
        exit(1);

    if (sayısal_ip[0] == 10) or (sayısal_ip[0] == 172 and (sayısal_ip[1] >= 16 and sayısal_ip[1] <= 31)) or (sayısal_ip[0] == 192 and sayısal_ip[1] == 168):
            print(ip_adresi + " IPv4 adresi kişiseldir.");
    else:
            print(ip_adresi + " IPv4 adresi herkese açıktır.");

    exit(0);
