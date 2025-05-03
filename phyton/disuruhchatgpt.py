#NNNNNNNNN inputer

#name = input("siapa nama mu? = ")
#Yo   = int(input("berapa umur mu? = "))

#print("Halo,", name, "! Kamu berusia", Yo, "tahun. Selamat bermain!")

#print(f"Halo, {name}! Kamu berusia {Yo} tahun. Selamat bermain!")

#lupa istilah untuk tanda setelah if H line 16
#integer sudah dipakai di line 2 tapi lupa di line 13

#NNNNNNNNN tebak angka

#angka = 10

#h = int(input("masukan angka! "))


#if h == angka:
#    print("angka sudah benar")

#elif h > angka: #operator >= tidak perlu karena sudah di lakukan pada line 16
 #   print("angka terlalu besar")

#elif h < angka: #operator >= tidak perlu karena sudah di lakukan pada line 16
#    print("angka terlalu kecil")

#NNNNNNNN  looping angka tetapi hanya ganjil yang di print

#angka1 = 1

#while angka1 <= 10:
#    if angka1 % 2 != 0:
#        print(angka1)
#    angka1 += 1

#def tambah_lima(angka):
#   return(angka + 5)
#
#hasil = tambah_lima(20)
#print(hasil)


#NNNNNNNN fizzbuzz looping
   
#angka = 1

#while angka <= 50:
#    if angka % 5 == 0 and angka % 3 == 0:
#       print("fizzbuzz")
#    elif angka % 3 == 0:
#      print("fizz")
#    elif angka % 5 == 0:
#       print("buzz")
#    else:
#       print(angka)
#    angka += 1

#script gagal karena awalnya ada peraturan yang bertabrakan contohnya angka 14 tidak memenuhi syarat maka akhirnya angka 15 pun tercetak
#lalu angka += 1 jadi terlewat beberapa angka .
#Angka bertambah terlalu banyak karena pertambahan terjadi ketika if angka % 5 == 0 and angka % 3 == 0: dijalankan akan bertambah 1 tetapi kondisi yang lain juga ikut terjalankan seperti  elif angka % 5 == 0:
#ini bisa terjadi karena angka di naikan di awal loop dan juga di dalam kondisi if dan elif

#NNNNNNNN perkalian tanpa *

#def kali(a, b):
#    hasil = 0
#    for i in range(b):
#        hasil = hasil + a
#    return hasil

#print(kali(1, 3))
    

#teks = input("Masukkan teks: ")
#print("Jumlah huruf:", len(teks))  # menghitung panjang string

#for indeks in range(len(teks)):
#    print(f"Huruf ke-{indeks}: {teks[indeks]}")

#NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN  pendeteksi huruf vokal dan konsonan pada kata NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

#def deteksi_huruf(teks):
#    vokal = "aeiouAEIOU"
#    hasil = []
#
#    for huruf in teks:
#        if huruf.isalpha():  
#            if huruf in vokal:
#                hasil.append((huruf, "vokal"))
#            else:
#                hasil.append((huruf, "konsonan"))
#        else:
#            hasil.append((huruf, "simbol lain, bukan huruf"))
#    
#    return hasil


#input_teks = input("Masukkan sebuah kata atau kalimat: ")
#hasil_deteksi = deteksi_huruf(input_teks)

#for huruf, jenis in hasil_deteksi:
#    print(f"'{huruf}' adalah {jenis}")

#NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN Hangman NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

import random
def deteksi_huruf(kata):
    kata = random.choices["singa","kasur","bunga"]
    nyawa = 3
    jhk = 5

    while nyawa < 0:
        inputkata = input("masukan huruf")
        for huruf in kata:
                if huruf.isalpha:
                    if huruf in kata:
                        True
                        print("kata benar sisa", jhk,"huruf")
                else:
                    nyawa -= 1
                    print("masukan huruf bukan simbol! -1")


print("selamat datang di game tebak kata")
print("clue: jumlah huruf pada kata adalah 5")

input1 = input("masukan huruf ")
game = deteksi_huruf(input1)



      

