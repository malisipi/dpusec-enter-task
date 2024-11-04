#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <inttypes.h>

// Windows ve UTF8
#ifdef _WIN32
    #include <locale.h>
    #include <windows.h>
#endif


void kullanicidan_sayi_al(const char* istek, uint64_t* sayi){
    printf("%s: ", istek);
    char tampon[11]; // 10 + (NUL)
    fgets(tampon, 11, stdin);
    char karakter = 0;
    *sayi = 0; // Önceki değeri temizle
    for(int indeks=0; (karakter = tampon[indeks])!='\0'; indeks++){ // Tamponun sonuna kadar
        int rakam = karakter - '0'; // ASCII tablosuna göre char'lar arası çıkartma
        if(rakam >= 0 && rakam <= 9){ // Gerçekten de bir rakam mı?
            *sayi *= 10;
            *sayi += rakam;
        } else if(karakter == '_' || karakter == ' '){ // Sayıyı/Basamakları ayırmak için kullanılmış olabilir
            continue;
        } else if(karakter == '\n') { // Yeni satır karakterini atla
            continue;
        } else {
            printf("%s (%d)", "Geçersiz giriş, tanınmayan karakter:", karakter);
            exit(1);
        };
    };
}

int main(){
    #ifdef _WIN32
        SetConsoleOutputCP(CP_UTF8);
        SetConsoleCP(CP_UTF8);
        setlocale(LC_CTYPE, "C");
    #endif
    srand(time(NULL)); // Tohumu değiştir
    uint64_t rastgele_sayi = rand()%101; // 0 ila 100 arasında
    uint64_t tahmin = 0;
    while (rastgele_sayi != tahmin) {
        kullanicidan_sayi_al("Tahmininiz", &tahmin);
        if(tahmin > rastgele_sayi) {
            printf("%s (%" PRIu64 ") %s.\n", "İstenen sayı tahmininizden", tahmin, "daha düşük");
        } else if(tahmin < rastgele_sayi) {
            printf("%s (%" PRIu64 ") %s.\n", "İstenen sayı tahmininizden", tahmin, "daha yüksek");
        };
    };
    printf("\n%s.\n\t%s: %" PRIu64 "\n", "İstediğim sayıyı doğru tahmin ettin", "Sayı", rastgele_sayi);
    return 0;
}
