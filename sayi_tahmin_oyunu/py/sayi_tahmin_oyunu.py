import random

def kullanıcıdan_sayı_al(istem:str) -> int:
    sayı_str:str = input(istem + ": ");
    return int(sayı_str);

if(__name__ == "__main__"):
    rastgele_sayı:int = random.randint(0, 100); # 0 ila 100 arasında
    tahmin:int = 0;
    while (rastgele_sayı != tahmin):
        tahmin = kullanıcıdan_sayı_al("Tahmininiz");
        if tahmin > rastgele_sayı:
            print("İstenen sayı tahmininizden ("+ str(tahmin) +") daha düşük.\n");
        elif tahmin < rastgele_sayı:
            print("İstenen sayı tahmininizden ("+ str(tahmin) +") daha yüksek.\n");

    print("\nİstediğim sayıyı doğru tahmin ettin.\n\tSayı: " + str(tahmin));
