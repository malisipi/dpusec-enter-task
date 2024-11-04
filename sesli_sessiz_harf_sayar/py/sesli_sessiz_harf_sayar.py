if(__name__ == "__main__"):
    yazı:str = input("Yazı girişi yapın: ");
    bölünmüş_yazı:list[str] = list(yazı);

    sesli_karakter:int = 0;
    sessiz_karakter:int = 0;

    for karakter in bölünmüş_yazı:
        if(karakter in "aeıiuoöüAEIİUOÖÜ"):
            sesli_karakter += 1;
        elif(karakter in "rtypğsdfghjklşzcvbnmçRTYPĞSDFGHJKLŞZCVBNMÇ"):
            sessiz_karakter += 1;
        else: continue;

    print("Yazı İstatistiği")
    print("\tSesli Harf: " + str(sesli_karakter));
    print("\tSessiz Harf: " + str(sessiz_karakter));
