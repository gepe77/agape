##################################### mencetak semua huruf pada kata agape

#for huruf in "agape":
#    print(huruf.upper())

##################################### mencetak angka dari 3 sampai 5

#for x in range(3,6):
#    print(x)

##################################### ganjil genap

#for i in range(10):
#    if i % 2 != 0:  # != itu mirip dengan else bedanya lebih simple dan flexible daripada line 18
#        print(i)  


#for i in range(10):
#    if i % 2 == 0:
#        continue
#   else:
#        print(1)

##################################### print huruf vokal pada suatu kata

#kata = "gamma"
#vokal = ["a", "i", "u", "e", "o"]
#def hapus_konsonan(teks):
#    hasil = []
#    for huruf in teks:
#        if huruf in vokal:
#            hasil.append(huruf)
#    return hasil

# Cetak hasilnya dengan koma sebagai pemisah
#print(", ".join(hapus_konsonan(kata)))  # Output: a, a

##################################### print kelipatan 3

#for i in range(1,21):
#    if i % 3 == 0:
#        print(i)
#    else:
#        print(i, "<- ini bukan kelipatan 3")

##################################### nama

#teman = ["Budi", "Ani", "Tono"]
#
#for nama in teman:
#    print(f"hai, {nama}!")

##################################### Enumerate

#pelajaran = ["Matematika", "IPA", "Bahasa"]

#for urut, item in enumerate(pelajaran):
#    print(urut + 1, item)

##################################### GRID
#for i in range(1,5):
#    for j in range(0):     
#        print("#", end="")
#        
#     
#    print("#" * i)                