print("===== Program Latihan Menghitung Diagonal Bidang dan Diagonal Ruang Kubus =====")
import random
rusukkubus = [6, 4.17 , 21.6, 33.133 , 43.96 , 47, 57.9 , 81]
print("Telah disediakan bermacam-macam angka acak sebagai panjang rusuk kubus"
      "\nKetik ALVINGANTENG untuk memulai proses pengacakan angka")
ALVINGANTENG = input(">>")
if ALVINGANTENG == 'ALVINGANTENG' :
    angka_acak = random.choice(rusukkubus)
    print("Panjang rusuk kubus :", angka_acak)
    print("Hitunglah Diagonal Ruang dan Diagonal Bidang dengan Panjang Rusuk", angka_acak, "m" )
    print("====================================================================")
    import math
    bidangkubus = angka_acak * math.sqrt(2)
    print("Diagonal Bidang dari kubus dengan panjang rusuk", angka_acak, "m adalah", bidangkubus, "m ~", math.ceil(bidangkubus), "m.")
    ruangkubus = angka_acak * math.sqrt(3)
    print("Diagonal Ruang dari kubus dengan panjang rusuk", angka_acak, "m adalah", ruangkubus, "m ~", math.ceil(ruangkubus), "m.")
else:
    print("Ulang program dan ketik 'ALVINGANTENG' untuk mendapatkan sebuah angka.")