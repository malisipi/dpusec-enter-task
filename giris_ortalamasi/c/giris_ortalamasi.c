#include <stdio.h>
#include <stdlib.h>

// Windows ve UTF8
#ifdef _WIN32
    #include <locale.h>
    #include <windows.h>
#endif


void kullanicidan_sayi_al(const char* istek, double* sayi){
    printf("%s: ", istek);
    char tampon[11]; // 10 + (NUL)
    scanf("%10s", tampon);
    char karakter = 0;
    int ondalik_kisim = -1;
    for(int indeks=0; (karakter = tampon[indeks])!='\0'; indeks++){ // Tamponun sonuna kadar
        int rakam = karakter - '0'; // ASCII tablosuna göre char'lar arası çıkartma
        if(rakam >= 0 && rakam <= 9){ // Gerçekten de bir rakam mı?
            if(ondalik_kisim >- 1) ondalik_kisim++;
            *sayi *= 10;
            *sayi += rakam;
        } else if(ondalik_kisim==-1 && (karakter == ',' || karakter == '.')){
            ondalik_kisim = 0;
        } else if(karakter == '_' || karakter == ' '){ // Sayıyı/Basamakları ayırmak için kullanılmış olabilir
            continue;
        } else {
            printf("%s", "Geçersiz giriş");
            exit(1);
        };
    };
    while(ondalik_kisim>0){
        *sayi /= 10;
        ondalik_kisim--;
    };
}

int main(){
    #ifdef _WIN32
        SetConsoleOutputCP(CP_UTF8);
        SetConsoleCP(CP_UTF8);
        setlocale(LC_CTYPE, "C");
    #endif
    double sayi1 = 0;
    double sayi2 = 0;
    kullanicidan_sayi_al("İlk sayı", &sayi1);
    kullanicidan_sayi_al("İkinci sayı", &sayi2);
    printf("%s %.2f", "Ortalaması", (sayi1+sayi2)/2);
    return 0;
}