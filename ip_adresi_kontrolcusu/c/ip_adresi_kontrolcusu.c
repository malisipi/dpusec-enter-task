#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Windows ve UTF8
#ifdef _WIN32
    #include <locale.h>
    #include <windows.h>
#endif


int main(){
    #ifdef _WIN32
        SetConsoleOutputCP(CP_UTF8);
        SetConsoleCP(CP_UTF8);
        setlocale(LC_CTYPE, "C");
    #endif
    int ip_kisim_1, ip_kisim_2, ip_kisim_3, ip_kisim_4;
    printf("%s: ", "Kontrol etmek istediğiniz IPv4 adresini girin");
    scanf("%d.%d.%d.%d", &ip_kisim_1, &ip_kisim_2, &ip_kisim_3, &ip_kisim_4);
    if( // IP adresinin tanımlı olup olmadığını kontrol et
        (ip_kisim_1 < 0 || ip_kisim_1 > 255) ||
        (ip_kisim_2 < 0 || ip_kisim_2 > 255) ||
        (ip_kisim_3 < 0 || ip_kisim_3 > 255) ||
        (ip_kisim_4 < 0 || ip_kisim_4 > 255)
    ){
        printf("%s", "Girilen IPv4 adresi tanıma uygun değil. IPv4 adresleri 0.0.0.0 ila 255.255.255.255 arasında olmak zorunda");
        exit(1);
    };
    bool herkese_acik = true;
    if(
        (ip_kisim_1 == 10) // 10.*.*.* aralığı
        || (ip_kisim_1 == 172 && (ip_kisim_2 >= 16 && ip_kisim_2 <= 31)) // 172.16.0.0 - 172.31.255.255 aralığı
        || (ip_kisim_1 == 192 && ip_kisim_2 == 168) // 192.168.*.* aralığı
    ){
        herkese_acik = false;
    };
    char* sonuc = "IPv4 adresi kişiseldir.";
    if(herkese_acik){
        sonuc = "IPv4 adresi herkese açıktır.";
    };
    printf("%d.%d.%d.%d %s", ip_kisim_1, ip_kisim_2, ip_kisim_3, ip_kisim_4, sonuc);
    return 0;
}
