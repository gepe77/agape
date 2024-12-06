def umur(y, m, d):
    import datetime
    saatini = datetime.datetime.now().date() #mememanggil waktu sekarang dengan datetime
    tanggallahir = datetime.date(y, m, d)
    hehey = hehey((saatini - tanggallahir).days / 365)
    print(hehey)
umur(2012, 1, 21)