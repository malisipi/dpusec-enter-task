def csv_aç(dosya_konumu:str) -> list[list[str]]:
    dosya:_io.TextIOWrapper = open(dosya_konumu, "r");
    csv:list[list[str]] = [];

    yeni_satır:str = dosya.readline();
    tanımlı_sütun_sayısı:int = len(yeni_satır.split(","));
    while yeni_satır != "":
        yeni_satır = yeni_satır.split("\n")[0]; # Yeni satır karakterinden kurtulma vakti
        if tanımlı_sütun_sayısı == len(yeni_satır.split(",")): # Eğer sütun sayıları eşleşiyorsa ekle
            csv.append(yeni_satır.split(",")); # ,'den böl ve listeye ekle
        else:
            print("Hatalı formatlanmış satır atlanıyor...");
            print("\tSatır: " + yeni_satır);
        yeni_satır = dosya.readline();
    dosya.close();
    return csv;

def csv_yazdır(csv:list[list[str]]) -> None:
    satır_sayısı:int = len(csv);
    sütun_sayısı:int = len(csv[0]);
    print("\n");
    for satır_indeks in range(0, satır_sayısı): # İlk satır isimleri tuttuğu için atlanır
        satır_formatı:str = "{}|" + (" {:<15} |" *sütun_sayısı);
        if(satır_indeks == 1): print("-" * (1+18*sütun_sayısı));
        print(satır_formatı.format("", *csv[satır_indeks]));

def csv_hesapla(csv:list[list[str]]) -> list[list[str]]:
    satır_sayısı:int = len(csv);
    sütun_sayısı:int = len(csv[0]);
    hesaplanmış_csv:list[list[str]] = [[csv[0][0], "Ortalamalar"]];
    for satır_indeks in range(1, satır_sayısı): # İlk satır isimleri tuttuğu için atlanır
        toplam:int = 0;
        for sütun_indeks in range(1, sütun_sayısı):
            toplam += int(csv[satır_indeks][sütun_indeks]);
        hesaplanmış_csv.append([csv[satır_indeks][0], str(toplam/(sütun_sayısı-1))]);
    return hesaplanmış_csv;

def csv_kaydet(dosya_konumu:str, csv:list[list[str]]) -> None:
    dosya:_io.TextIOWrapper = open(dosya_konumu, "w");
    for satır in csv:
        dosya.write(",".join(satır) + "\n");
    dosya.close();

if(__name__ == "__main__"):
    dosya_konumu:str = input("Dosya Konumu: ");
    csv:list[list[str]] = csv_aç(dosya_konumu);
    csv_yazdır(csv);
    hesaplanmış_csv:list[list[str]] = csv_hesapla(csv);
    csv_yazdır(hesaplanmış_csv);
    csv_kaydet("hesaplanmış_" + dosya_konumu, hesaplanmış_csv);
    exit(0);
