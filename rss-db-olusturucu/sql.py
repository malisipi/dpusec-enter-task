import sqlite3;
import re;
import hasher;
import domain;

__bağlantı = None;
__imleç = None;

def girişi_temizle(kullanıcı_girişi:str) -> str:
    temizlenmiş_çıktı:str = re.sub(r"[^A-Za-z0-9_]", "_", kullanıcı_girişi);
    return temizlenmiş_çıktı;

def bağlan(veritabanı:str) -> None:
    global __bağlantı;
    global __imleç;
    __bağlantı = sqlite3.connect("rss_beslemeleri.db");
    __imleç = __bağlantı.cursor();

def sağlayıcı_tablo_oluştur() -> None:
    try:
        __imleç.execute("CREATE TABLE saglayicilar (baslik TEXT, link TEXT, aciklama TEXT, rss_link TEXT)");
    except Exception as reason:
        if(not "already exist" in str(reason)): # Eğer tablo mevcutsa atla
            print(reason);
            exit(1);

def yeni_sağlayıcı(rss_linki:str) -> None:
    aynı_rss_linkine_sahip_kayıtlar = __imleç.execute("SELECT rss_link FROM saglayicilar WHERE rss_link = ?", (rss_linki, )).fetchall();
    if(len(aynı_rss_linkine_sahip_kayıtlar) > 0): return; # Aynı rss_linkine sahiplerse eklenmelerine gerek yok

    __imleç.execute("INSERT INTO saglayicilar VALUES (?, ?, ?, ?)", (rss_linki, rss_linki, "", rss_linki));

def sağlayıcıyı_sil(rss_linki:str) -> None:
    try:
        link:str = (__imleç.execute("SELECT link FROM saglayicilar WHERE rss_link = ?", (rss_linki, )).fetchall())[0][0];
    except:
        print("\tİstenilen sağlayıcı kayıtlarda bulunamadı..");
        return;
    __imleç.execute("DELETE FROM saglayicilar WHERE rss_link = ?", (rss_linki, ));
    __imleç.execute("DROP TABLE {}".format(girişi_temizle(domain.domaini_ayrıştır(link))));
    __bağlantı.commit();

def sağlayıcıyı_güncelle(rss_linki:str, başlık:str, link:str, açıklama:str) -> None:
    __imleç.execute("UPDATE saglayicilar SET baslik = ?, link = ?, aciklama = ? WHERE rss_link = ?", (başlık, link, açıklama, rss_linki, ));
    __bağlantı.commit();

def yeni_besleme_tablosu_oluştur(tablo_adı:str) -> None:
    try:
        __imleç.execute("CREATE TABLE {} (baslik TEXT, link TEXT, aciklama TEXT, zaman TEXT, kategori TEXT, hash TEXT)".format(girişi_temizle(tablo_adı)));
    except Exception as reason:
        if(not "already exist" in str(reason)): # Eğer tablo mevcutsa atla
            print(reason);
            exit(1);

def yeni_besleme(tablo_adı:str, başlık:str, link:str, açıklama:str, zaman:str, kategori:str) -> None:
    # HASH otomatik olarak oluşturulup karşılaştırılacaktır.
    # HASH algoritması olarak MD5 kullanılacaktır.
    # HASH burada "sadece" içeriğin daha önce kaydedilip kaydedilmediğini depolamak için mevcuttur.
    # Bu HASH değerini başka bir amaçla kullanılması amaçlanmamaktadır.
    veri_hash:str = hasher.md5_hash_oluştur([başlık, link, açıklama]);
    aynı_hasha_sahip_kayıtlar = __imleç.execute("SELECT hash FROM {} WHERE hash = ?".format(girişi_temizle(tablo_adı)), (veri_hash, )).fetchall();
    if(len(aynı_hasha_sahip_kayıtlar) > 0): return; # Aynı hash'a sahiplerse eklenmelerine gerek yok

    __imleç.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?)".format(girişi_temizle(tablo_adı)), (başlık, link, açıklama, zaman, kategori, veri_hash));

def her_sağlayıcı_için(işleyici:callable) -> None:
    sql_sonucu = __imleç.execute("SELECT rss_link FROM saglayicilar").fetchall();
    sağlayıcı_listesi = list(map(lambda sağlayıcı: sağlayıcı[0], sql_sonucu));
    for sağlayıcı in sağlayıcı_listesi:
        işleyici(sağlayıcı, sağlayıcıyı_güncelle, yeni_besleme_tablosu_oluştur, yeni_besleme);
