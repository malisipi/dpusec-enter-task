def log_dosyasını_aç(dosya_konumu:str) -> dict:
    dosya:_io.TextIOWrapper = open(dosya_konumu, "r");
    yeni_satır:str = dosya.readline();
    log:dict = {};
    while yeni_satır != "":
        yeni_satır = yeni_satır.split("\n")[0]; # Yeni satır karakterinden kurtulma vakti
        try:
            istek:list[str] = yeni_satır.split(" ");
            if(len(istek) != 3): raise Exception("");
            if(not istek[0] in log):
                log[istek[0]] = [];
            log[istek[0]].append([istek[1], istek[2]]);
        except:
            print("Hatalı İstek Verisi Atlanıyor\n\tİstek: " + yeni_satır);
        yeni_satır = dosya.readline();
    return log;
"""
{}log_dosyası:
    []ip:str:
        [tip:str, adres:str] # istekler
     
"""

def toplam_istek_analizi(log:dict) -> None:
    for ip in log:
        print("=> {:15} toplamda {:5} kez istekte bulundu.".format(ip, len(log[ip])));

if(__name__ == "__main__"):
    dosya_konumu:str = input("Dosya Konumu: ");
    log:dict = log_dosyasını_aç(dosya_konumu);
    toplam_istek_analizi(log);