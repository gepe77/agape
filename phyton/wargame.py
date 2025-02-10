import time

# Fungsi untuk memberikan jeda waktu
def pause(seconds):
    time.sleep(seconds)

# Fungsi untuk memulai permainan
def intro():
    print("Selamat datang di Game Petualangan Perang Dunia II!")
    pause(2)
    print("\nKamu adalah seorang tentara Uni Soviet yang berada di tengah pertempuran penting selama Perang Dunia II.")
    pause(2)
    print("Kamu akan menghadapi banyak pilihan yang bisa mempengaruhi nasibmu dan jalannya sejarah.")
    pause(2)
    print("Saat ini, kamu berada di Stalingrad, kota yang sedang dibombardir oleh pasukan Nazi Jerman.")
    pause(2)

# Pilihan pertama: Pindah ke lokasi yang aman atau bertarung di medan perang
def first_choice():
    print("\nKamu baru saja menerima perintah untuk memeriksa garis depan. Apa yang akan kamu lakukan?")
    pause(1)
    print("1. Pergi ke garis depan untuk memimpin serangan terhadap pasukan Jerman.")
    print("2. Mencari perlindungan sementara di markas yang lebih aman dan menunggu instruksi lebih lanjut.")
    
    choice = input("Masukkan pilihanmu (1 atau 2): ")
    if choice == '1':
        front_line_battle()
    elif choice == '2':
        safe_house()
    else:
        print("Pilihan tidak valid. Cobalah lagi.")
        first_choice()

# Pilihan jika memilih bertempur di garis depan
def front_line_battle():
    print("\nKamu memutuskan untuk pergi ke garis depan dan bergabung dengan pasukan yang sedang bertempur melawan tentara Jerman.")
    pause(2)
    print("Kamu tiba di sebuah posisi yang sangat kritis, pasukan Jerman hampir menguasai seluruh daerah ini.")
    pause(2)
    print("Apa yang akan kamu lakukan?")
    print("1. Bertarung dengan senjata api dan mengarahkan serangan langsung.")
    print("2. Menggunakan taktik gerilya, menyerang dari sisi yang tidak terduga.")
    
    choice = input("Masukkan pilihanmu (1 atau 2): ")
    if choice == '1':
        direct_assault()
    elif choice == '2':
        guerrilla_warfare()
    else:
        print("Pilihan tidak valid. Cobalah lagi.")
        front_line_battle()

# Pilihan jika memilih bertarung langsung
def direct_assault():
    print("\nKamu memimpin pasukanmu untuk melakukan serangan langsung terhadap pasukan Jerman.")
    pause(2)
    print("Seranganmu cukup berhasil, namun kamu harus menghadapi serangan balasan yang sangat kuat.")
    pause(2)
    print("Kamu terluka parah dalam pertempuran ini, tetapi pasukan Soviet berhasil memukul mundur pasukan Jerman.")
    pause(2)
    print("Namun, kamu harus dibawa ke rumah sakit militer untuk perawatan.")
    hospital_scene()

# Pilihan jika memilih taktik gerilya
def guerrilla_warfare():
    print("\nKamu memutuskan untuk menggunakan taktik gerilya, menyerang pasukan Jerman dengan cara yang tidak terduga.")
    pause(2)
    print("Seranganmu efektif, pasukan Jerman terkejut dan mulai mundur.")
    pause(2)
    print("Namun, pasukanmu juga menderita banyak kerugian dan beberapa tentara tewas dalam aksi ini.")
    pause(2)
    print("Walaupun ada kerugian, keberhasilanmu membantu mematahkan semangat pasukan Jerman.")
    pause(2)
    hospital_scene()

# Pilihan jika memilih berlindung di markas yang lebih aman
def safe_house():
    print("\nKamu memilih untuk berlindung sementara di markas yang aman. Tapi, kamu tahu ini tidak akan bertahan lama.")
    pause(2)
    print("Di dalam markas, kamu menerima perintah untuk bertindak dalam waktu singkat dan menuju ke garis depan.")
    pause(2)
    print("Namun, serangan udara Jerman datang lebih cepat dari yang diperkirakan!")
    pause(2)
    print("Kamu harus segera bertindak!")
    air_strike()

# Pilihan jika terkena serangan udara
def air_strike():
    print("\nPasukan Jerman melancarkan serangan udara yang hebat. Beberapa bangunan hancur dan banyak tentara terluka.")
    pause(2)
    print("Kamu harus memilih tempat perlindungan yang aman.")
    print("1. Menyelamatkan tentara yang terluka.")
    print("2. Menyembunyikan diri dan bertahan di tempat yang aman.")
    
    choice = input("Masukkan pilihanmu (1 atau 2): ")
    if choice == '1':
        rescue_mission()
    elif choice == '2':
        survival()
    else:
        print("Pilihan tidak valid. Cobalah lagi.")
        air_strike()

# Pilihan jika menyelamatkan tentara yang terluka
def rescue_mission():
    print("\nKamu memutuskan untuk menyelamatkan tentara yang terluka. Meskipun ini sangat berisiko, kamu merasa ini adalah hal yang benar.")
    pause(2)
    print("Kamu berhasil membawa beberapa tentara yang terluka ke tempat yang lebih aman.")
    pause(2)
    print("Sayangnya, serangan udara Jerman sangat berat, dan banyak yang harus mengorbankan diri.")
    pause(2)
    hospital_scene()

# Pilihan untuk bertahan hidup setelah serangan udara
def survival():
    print("\nKamu memilih untuk berlindung sementara dan bertahan hidup.")
    pause(2)
    print("Meskipun banyak temanmu yang terluka atau gugur, kamu bertahan hidup.")
    pause(2)
    print("Setelah beberapa jam, serangan udara mereda dan kamu bisa kembali ke garis depan.")
    pause(2)
    print("Namun, kamu merasa kehilangan banyak sahabat dalam pertempuran ini.")
    pause(2)
    hospital_scene()

# Pilihan jika harus dirawat di rumah sakit militer
def hospital_scene():
    print("\nSetelah pertempuran, kamu dibawa ke rumah sakit militer untuk mendapatkan perawatan medis.")
    pause(2)
    print("Kamu terbaring di ranjang rumah sakit, terluka, namun masih hidup.")
    pause(2)
    print("Di sini kamu memiliki waktu untuk merenung, tetapi keputusan masa depan akan segera menantimu.")
    pause(2)
    print("Apa yang akan kamu lakukan setelah pulih?")
    print("1. Kembali ke garis depan untuk melanjutkan perjuangan.")
    print("2. Mengambil peran yang lebih strategis dan membantu perencanaan di markas.")
    
    choice = input("Masukkan pilihanmu (1 atau 2): ")
    if choice == '1':
        return_to_front_line()
    elif choice == '2':
        strategic_role()
    else:
        print("Pilihan tidak valid. Cobalah lagi.")
        hospital_scene()

# Pilihan jika kembali ke garis depan
def return_to_front_line():
    print("\nKamu kembali ke garis depan dan melanjutkan pertempuran.")
    pause(2)
    print("Dengan perjuangan keras, pasukan Soviet akhirnya berhasil mengalahkan pasukan Nazi di Stalingrad.")
    victory()

# Pilihan jika memilih peran strategis
def strategic_role():
    print("\nKamu memilih untuk bekerja di markas, membantu merencanakan strategi untuk melawan pasukan Jerman.")
    pause(2)
    print("Keputusan strategis yang kamu buat berhasil memperkuat posisi Soviet di banyak front.")
    pause(2)
    print("Dengan bantuanmu, pasukan Soviet berhasil melancarkan serangan balasan yang besar.")
    victory()

# Kemenangan dan Plot Twist
def victory():
    print("\nDengan keberhasilanmu, pasukan Soviet akhirnya mengalahkan pasukan Jerman di Stalingrad.")
    pause(2)
    print("Namun, saat kamu merayakan kemenangan, kamu menerima informasi bahwa komandan tertinggi Uni Soviet, Joseph Stalin, mencurigai ada pengkhianat di dalam tubuh pasukan.")
    pause(2)
    print("Apa yang akan kamu lakukan?")
    print("1. Menyelidiki apakah ada pengkhianat di antara tentara.")
    print("2. Terus berjuang tanpa memikirkan pengkhianatan.")
    
    choice = input("Masukkan pilihanmu (1 atau 2): ")
    if choice == '1':
        betrayal_investigation()
    elif choice == '2':
        ultimate_betrayal()
    else:
        print("Pilihan tidak valid. Cobalah lagi.")
        victory()

# Investigasi pengkhianatan
def betrayal_investigation():
    print("\nKamu mulai menyelidiki dan menemukan bahwa salah satu sahabatmu ternyata adalah mata-mata Jerman!")
    pause(2)
    print("Kamu harus memilih apakah akan melaporkannya atau menyembunyikan kebenaran untuk melindungi temanmu.")
    print("1. Melaporkan pengkhianatan tersebut.")
    print("2. Menyembunyikan kebenaran dan melindungi temanmu.")
    
    choice = input("Masukkan pilihanmu (1 atau 2): ")
    if choice == '1':
        betrayal_reported()
    elif choice == '2':
        secret_ally()
    else:
        print("Pilihan tidak valid. Cobalah lagi.")
        betrayal_investigation()

# Melaporkan pengkhianatan
def betrayal_reported():
    print("\nKamu melaporkan pengkhianatan tersebut kepada komandan.")
    pause(2)
    print("Komandan memuji keberanianmu, tetapi kamu dihukum karena telah melaporkan temanmu.")
    game_over()

# Melindungi teman yang berkhianat
def secret_ally():
    print("\nKamu memilih untuk menyembunyikan kebenaran dan melindungi temanmu.")
    pause(2)
    print("Namun, pengkhianatan ini akhirnya terungkap dan kamu dituduh sebagai pengkhianat juga.")
    game_over()

# Ending jika memilih untuk terus berjuang tanpa peduli pengkhianatan
def ultimate_betrayal():
    print("\nKamu memilih untuk terus berjuang tanpa memikirkan pengkhianatan.")
    pause(2)
    print("Namun, akhirnya pasukan Jerman mengungkapkan bahwa mereka telah membayar beberapa pejabat Soviet untuk memberikan informasi.")
    pause(2)
    print("Sebuah pengkhianatan besar terjadi dan kamu pun jatuh dalam perang ini.")
    game_over()

# Game Over
def game_over():
    print("\nKamu gagal dalam misi ini. Game over.")
    pause(2)
    print("Terima kasih telah bermain! Coba lagi untuk melihat ending yang berbeda.")

# Memulai permainan
intro()
first_choice()
