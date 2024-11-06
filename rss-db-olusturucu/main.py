import sql;
import rss;

if(__name__ == "__main__"):
    sql.bağlan("rss_beslemeleri.db");
    sql.sağlayıcı_tablo_oluştur();
    print("RSS Besleme Aracı");
    print("=================");
    while(True):
        print("\n\t(1) Veritabanlarını güncelle");
        print("\t(2) Yeni sağlayıcı ekle");
        print("\t(3) Bir sağlayıcıyı kaldır");
        print("\t(4) Mevcut sağlayıcıları listele")
        print("\t(9) Çıkış")
        girdi:str = input("\n\tİşleminiz: ");
        if(girdi == "1"):
            sql.her_sağlayıcı_için(rss.işle);
        elif(girdi == "2"):
            rss_adresi:str = input("\tYeni sağlayıcının RSS adresi: ");
            rss_adresi = rss_adresi.split("\n")[0];
            if(len(rss_adresi) < 12): continue; # 12 Haneden daha küçük bir rss url'i olduğunu sanmıyorum. (http://) bile tek başına 7 karakter alıyor
            sql.yeni_sağlayıcı(rss_adresi);
        elif(girdi == "3"):
            sql.her_sağlayıcı_için(lambda adres, a, b, c: print("\t* " + adres));
            rss_adresi:str = input("\tSilmek istediğiniz sağlayıcının RSS adresi: ");
            rss_adresi = rss_adresi.split("\n")[0];
            if(len(rss_adresi) < 12): continue; # 12 Haneden daha küçük bir rss url'i olduğunu sanmıyorum. (http://) bile tek başına 7 karakter alıyor
            sql.sağlayıcıyı_sil(rss_adresi);
        elif(girdi == "4"):
            print("");
            sql.her_sağlayıcı_için(lambda adres, a, b, c: print("\t* " + adres));
        elif(girdi == "9"):
            exit(0);
