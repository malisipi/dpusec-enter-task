if(__name__ == "__main__"):
    url:str = input("Yazı girişi yapın: "); # protokol://kullanici_adi:şifre@alt.domain.com:8000/yol/adi/index.html?arama#hash
    adres:str = url.split("://")[1]; # 0 -> (protokol) [://] 1-> (kullanici_adi:şifre@alt.domain.com:8000/yol/adi/index.html?arama#hash)
    adres = adres.split("/")[0]; # 0 -> (kullanici_adi:şifre@alt.domain.com:8000)[/] 1-> (yol)[/] 2-> (adi)[/] 3-> (index.html?arama#hash)
    adres = adres.split("@")[-1]; # 0-> (kullanici_adi:şifre)[@] -1 -> (alt.domain.com:8000)
    subdomain:str = adres.split(":")[0]; # 0 -> (alt.domain.com)[:] 1-> (8000)
    print("Ayrıştırılan subdomain: " + subdomain); # (alt)[.](domain)[.](com)
    domain:str = ".".join(subdomain.split(".")[-2:]); # {#-2}[.](domain)[.](com){#}
    print("Ayrıştırılan domain: " + domain);
