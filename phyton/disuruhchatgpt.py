#NNNNNNNNN inputer
video_url = "https://www.youtube.com/watch?v=2qBlE2-WL60"

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
import webbrowser

def permainan_hangman():
    kata = ["singa", "kasur", "bunga"]
    kata_terpilih = random.choice(kata)
    huruf_yang_ditebak = []
    kata_tertebak = ['_' for _ in kata_terpilih]
    nyawa = 6

    print("Selamat datang di permainan Hangman!")
    print("Petunjuk: Jumlah huruf pada kata adalah", len(kata_terpilih))

    while nyawa > 0 and '_' in kata_tertebak:
        print("\nKata: ", ' '.join(kata_tertebak))
        print("Nyawa tersisa:", nyawa)
        tebakan = input("Masukkan huruf: ").lower()

        if len(tebakan) != 1 or not tebakan.isalpha():
            print("Masukkan satu huruf saja!")
            continue

        if tebakan in huruf_yang_ditebak:
            print("Kamu sudah menebak huruf ini. Coba huruf lain.")
            continue

        huruf_yang_ditebak.append(tebakan)

        if tebakan in kata_terpilih:
            print("Tebakan benar!")
            for idx, huruf in enumerate(kata_terpilih):
                if huruf == tebakan:
                    kata_tertebak[idx] = tebakan
        else:
            nyawa -= 1
            print("Tebakan salah! Nyawa berkurang 1.")

    if '_' not in kata_tertebak:
        print("\nSelamat! Kamu berhasil menebak kata:", kata_terpilih)
        print("selamat ini hadiahnya")
        webbrowser.open(video_url)

    else:
        print("\nKamu kalah! Kata yang benar adalah:", kata_terpilih)

permainan_hangman()


