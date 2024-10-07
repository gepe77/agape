bb = int(input("masukan berat badan (dalam kilo gram) "))
tb = int(input("masukan tinggi badan (dalam centi meter) "))
bmi = bb/(tb / 100)**2
if bmi < 18.5:
    print("anda sangat kurus cepat makan karena bmi mu kurang dari 18.5 Bmi=", bmi)
if bmi > 18.4 and bmi < 25:
    print("kamu normal pasti makanmu teratur karena bmi mu lebih dari 18.4 Bmi=", bmi)
if bmi > 25 and bmi < 29:
    print("kamu cukup gendut jangan makan keseringan atau kebanyakan karena bmi mu lebih dari 25 Bmi=", bmi)
if bmi > 29:
    print("kamu terlalu gendut atur makanmu karena bmi kamu lebih dari 29 Bmi=", bmi)