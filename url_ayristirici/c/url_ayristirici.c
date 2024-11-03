#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Windows ve UTF8
#ifdef _WIN32
    #include <locale.h>
    #include <windows.h>
#endif

typedef struct URL {
    char hash[4096];
    char host[4096];
    char host_adi[4096];
    char adres[4096];
    char sifre[4096];
    char yol_adi[4096];
    char port_str[4096];
    int port;
    char protokol[4096];
    char arama[4096];
    char kullanici_adi[4096];
} URL;

void stringi_bol(const char* yazi, const char* ayristirma, char* ilk, char* ikinci){
    int ayristirma_indeks = 0;
    char karakter;
    for(int indeks=0; (karakter=yazi[indeks])!='\0'; indeks++){
        if(ayristirma[ayristirma_indeks] == yazi[indeks]){
            while(ayristirma[ayristirma_indeks] == yazi[indeks + ayristirma_indeks]){
                ayristirma_indeks++;
            };
            if(ayristirma[ayristirma_indeks]=='\0'){
                strncpy(ilk, yazi, indeks);
                ilk[indeks] = '\0';
                indeks += ayristirma_indeks;
                strcpy(ikinci, yazi+indeks);
                return;
            };
            ayristirma_indeks = 0;
        };
    };
};

// ***********------------------------**********-----------------------------------
// protokol://kullanici_adi:şifre@alt.domain.com:8000/yol/adi/index.html?arama#hash
// *: Minimum gerekli alan
// -: Gerekli değil

void urli_ayristir(URL* url, const char* yazi){
    char tampon[4096]; // 4095 + (NUL)
    sprintf(tampon, "%.4095s", yazi);
    sprintf(url->adres, "%s", tampon);
    char domain[4096];
    char yol_adi[4096];
    char kimlik[4096];
    stringi_bol(tampon, "://", url->protokol, domain); // (protokol)[://](kullanici_adi:şifre@alt.domain.com:800/yol/adi/index.html?arama#hash)
    if(strchr(domain, '/') != NULL){ // kullanici_adi:şifre@alt.domain.com:8000 [/] yol/adi/index.html?arama#hash
        stringi_bol(domain, "/", domain, yol_adi); // (kullanici_adi:şifre@alt.domain.com:800)[/](yol/adi/index.html?arama#hash)
        if(strchr(yol_adi, '#')){ // yol/adi/index.html?arama[#]hash
            char hash[4096];
            stringi_bol(yol_adi, "#", yol_adi, hash); // (yol/adi/index.html?arama)[#](hash)
            sprintf(url->hash, "#%s", hash);
        };
        if(strchr(yol_adi, '?')){ // yol_adi/yolu/index.html[?]arama
            char arama[4096];
            stringi_bol(yol_adi, "?", yol_adi, arama); // (yol/adi/index.html)[?](arama)
            sprintf(url->arama, "?%s", arama);
        };
        sprintf(url->yol_adi, "/%s", yol_adi); // (yol/adi/index.html)
    };
    if(strchr(domain, '@') != NULL){ // kullanici_adi:şifre[@]alt.domain.com:8000
        stringi_bol(domain, "@", kimlik, domain); // (kullanici_adi:şifre)[@](alt.domain.com:8000)
        if(strchr(kimlik, ':')){ // kullanici_adi[:]şifre
            stringi_bol(kimlik, ":", url->kullanici_adi, url->sifre); // (kullanici_adi)[:](şifre)
        };
    };
    sprintf(url->host, "%s", domain);
    if(strchr(domain, ':') != NULL){ // alt.domain.com:8000
        stringi_bol(domain, ":", domain, url->port_str); // (alt.domain.com)[:](8000)
        url->port = atoi(url->port_str);
    };
    sprintf(url->host_adi, "%s", domain);
};

void urli_yazdir(URL* url){
    printf("URL: (İşaretçi konumu => %p)\n", url);
    printf("\t%s: %s\n", "Hash", url->hash);
    printf("\t%s: %s\n", "Host", url->host);
    printf("\t%s: %s\n", "Host Adı", url->host_adi);
    printf("\t%s: %s\n", "Adres", url->adres);
    printf("\t%s: %s\n", "Şifre", url->sifre);
    printf("\t%s: %s\n", "Yol Adı", url->yol_adi);
    printf("\t%s: %i\n", "Port", url->port);
    printf("\t%s: %s\n", "Protokol", url->protokol);
    printf("\t%s: %s\n", "Arama", url->arama);
    printf("\t%s: %s\n", "Kullanıcı Adı", url->kullanici_adi);
};

int main(){
    #ifdef _WIN32
        SetConsoleOutputCP(CP_UTF8);
        SetConsoleCP(CP_UTF8);
        setlocale(LC_CTYPE, "C");
    #endif
    char tampon[4096];
    printf("%s: ", "Yazı girişi yapın");
    fgets(tampon, 4096, stdin);
    tampon[strlen(tampon)-1] = '\0'; // Yeni satır karakterini sil
    URL* url = (URL*)malloc(sizeof(URL)); // Yeni URL Objesi
    urli_ayristir(url, tampon);
    urli_yazdir(url);
    free(url); // Belleği boşaltma vakti
    return 0;
}