import random
while True:
    anton = int(input("masukan angka 1 untuk mulai dan angka 2 untuk keluar"))
    if anton == 1:
        hendra = random.randint(1, 6)
        print(hendra)
    elif anton == 2:
        break
    else:
        print("tidak saatnya untuk itu bung")