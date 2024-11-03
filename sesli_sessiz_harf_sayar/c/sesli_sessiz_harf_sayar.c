#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Windows ve UTF8
#ifdef _WIN32
    #include <locale.h>
    #include <windows.h>
#endif

const int kucuk_varyant_maks = 'z'-'a';
const int buyuk_varyant_maks = 'Z'-'A';

void sesli_sessiz_harf_say(const char* yazi, uint16_t* sesli_sayisi, uint16_t* sessiz_sayisi){
    char tampon[1024]; // 1023 + (NUL)
    sprintf(tampon, "%1023s", yazi);
    unsigned char karakter = 0;
    // Sıfırla
    *sesli_sayisi = 0;
    *sessiz_sayisi = 0;
    for(int indeks=0; (karakter = tampon[indeks])!='\0'; indeks++){ // Tamponun sonuna kadar
        if((karakter & 0x80) == 0x80){ // Eğer ASCII uyumluluğu dışında kalan UTF-8 karakterse
            if((karakter & 0x40) == 0x40){ // İki byte'lık UTF-8 karakterse
                if((karakter & 0x20) == 0x20){
                    /* 3 veya 4 karakterde depolanan UTF-8 Türkçe karakter yok
                    * Atlanacak, kalan karakterler devam karakteri olarak aşağıda atlanacak */
                    continue;
                } else {
                    unsigned char ikincil_karakter = tampon[++indeks];
                    if(ikincil_karakter == '\0') return; // Eğer bitiş karakteriyse sonlandır
                    // ğĞüÜşŞıİöÖçÇ
                    if(
                        (karakter == 0xC4 && ikincil_karakter == 0x9F) // (ğ)
                        || (karakter == 0xC5 && ikincil_karakter == 0x9F) // (ş)
                        || (karakter == 0xC3 && ikincil_karakter == 0xA7) // (ç)
                        || (karakter == 0xC4 && ikincil_karakter == 0x9E) // (Ğ)
                        || (karakter == 0xC5 && ikincil_karakter == 0x9E) // (Ş)
                        || (karakter == 0xC3 && ikincil_karakter == 0x87) // (Ç)
                    ){
                        (*sessiz_sayisi)++;
                    } else if(
                        (karakter == 0xC3 && ikincil_karakter == 0xBC) // (ü)
                        || (karakter == 0xC4 && ikincil_karakter == 0xB1) // (ı)
                        || (karakter == 0xC3 && ikincil_karakter == 0xB6) // (ö)
                        || (karakter == 0xC3 && ikincil_karakter == 0x9C) // (Ü)
                        || (karakter == 0xC4 && ikincil_karakter == 0xB0) // (İ)
                        || (karakter == 0xC3 && ikincil_karakter == 0x96) // (Ö)
                    ){
                        (*sesli_sayisi)++;
                    } else {
                        continue;
                    }
                };
            } else { // UTF-8 Devam karakteri, atlanabilir
                continue;
            };
        } else {
            int kucuk_varyant = karakter - 'a';
            int buyuk_varyant = karakter - 'A';
            // ASCII'de tanımlı olmayan türkçe karakterler, UTF-8 olarak ayrıştırılacaktır
            if(kucuk_varyant>=0 && kucuk_varyant <= kucuk_varyant_maks){
                if(karakter == 'a' || karakter == 'e' || karakter == 'i' || karakter == 'o' || karakter == 'u'){ 
                    (*sesli_sayisi)++;
                } else if(karakter == 'q' || karakter == 'w' || karakter == 'x') { // Türkçe olmayan karakterler
                    continue;
                } else {
                    (*sessiz_sayisi)++;
                };
            } else if(buyuk_varyant>=0 && buyuk_varyant <= buyuk_varyant_maks){
                if(karakter == 'A' || karakter == 'E' || karakter == 'I' || karakter == 'O' || karakter == 'U'){ 
                    (*sesli_sayisi)++;
                } else if(karakter == 'Q' || karakter == 'W' || karakter == 'X') { // Türkçe olmayan karakterler
                    continue;
                } else {
                    (*sessiz_sayisi)++;
                };
            } else {
                continue;
            }
        };
    };
}

int main(){
    #ifdef _WIN32
        SetConsoleOutputCP(CP_UTF8);
        SetConsoleCP(CP_UTF8);
        setlocale(LC_CTYPE, "C");
    #endif
    char tampon[1024];
    uint16_t sesli_sayisi;
    uint16_t sessiz_sayisi;
    printf("%s: ", "Yazı girişi yapın");
    fgets(tampon, 1024, stdin);
    sesli_sessiz_harf_say(tampon, &sesli_sayisi, &sessiz_sayisi);
    printf("%s;\n\t%s: %u\n\t%s: %u\n", "Yazı İstatistiği", "Sesli Harf", sesli_sayisi, "Sessiz Harf", sessiz_sayisi);
    return 0;
}