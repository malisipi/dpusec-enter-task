import xml.dom.minidom;
import requests;
import domain;

def içeriği_temizle(yazı:str) -> str:
    return yazı.replace("<![CDATA[", "").replace("]]>", "").strip();

def düğümün_içeriğini_al(düğüm, tag:str) -> str:
    try:
        return içeriği_temizle(düğüm.getElementsByTagName(tag)[0].firstChild.toxml());
    except:
        return "";

def içeriği_ayrıştır(düğüm) -> list[str]:
    içerik_başlığı:str = düğümün_içeriğini_al(düğüm, "title");
    içerik_linki:str = düğümün_içeriğini_al(düğüm, "link");
    içerik_açıklaması:str = düğümün_içeriğini_al(düğüm, "description");
    içerik_zamanı:str = düğümün_içeriğini_al(düğüm, "pubDate");
    içerik_kategorisi:str = düğümün_içeriğini_al(düğüm, "category");
    return [içerik_başlığı, içerik_linki, içerik_açıklaması, içerik_zamanı, içerik_kategorisi];

def işle(url:str, sağlayıcıyı_güncelle:callable, yeni_besleme_tablosu_oluştur:callable, yeni_besleme:callable) -> None:
    print("\tGüncelleniyor.. " + url);
    istek = requests.get(url);
    data:str = istek.content.decode("utf-8");
    ağaç = xml.dom.minidom.parseString(data);
    kök = ağaç.firstChild; # rss düğümü
    kanal = kök.getElementsByTagName("channel")[0]; # kanal düğümü
    kanal_başlığı:str = düğümün_içeriğini_al(kanal, "title");
    kanal_linki:str = düğümün_içeriğini_al(kanal, "link");
    kanal_açıklaması:str = düğümün_içeriğini_al(kanal, "description");
    sağlayıcıyı_güncelle(url, kanal_başlığı, kanal_linki, kanal_açıklaması);

    içerik_düğümü_listesi:list = kanal.getElementsByTagName("item");
    içerik_listesi:list[list[str]] = list(map(içeriği_ayrıştır, içerik_düğümü_listesi));

    rss_domain_adresi = domain.domaini_ayrıştır(kanal_linki);
    yeni_besleme_tablosu_oluştur(rss_domain_adresi);

    for içerik in içerik_listesi:
        yeni_besleme(rss_domain_adresi, içerik[0], içerik[1], içerik[2], içerik[3], içerik[4]);
