import pygame
import random
import webbrowser

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Permainan Hangman")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# URL video hadiah
video_url = "https://www.youtube.com/watch?v=2qBlE2-WL60"

# Fungsi untuk menggambar hangman
def gambar_hangman(nyawa):
    if nyawa == 6:
        return None  # Tiang kosong
    elif nyawa == 5:
        pygame.draw.circle(screen, BLACK, (300, 100), 30, 3)  # Kepala
    elif nyawa == 4:
        pygame.draw.line(screen, BLACK, (300, 130), (300, 200), 3)  # Tubuh
    elif nyawa == 3:
        pygame.draw.line(screen, BLACK, (300, 160), (250, 150), 3)  # Tangan kiri
    elif nyawa == 2:
        pygame.draw.line(screen, BLACK, (300, 160), (350, 150), 3)  # Tangan kanan
    elif nyawa == 1:
        pygame.draw.line(screen, BLACK, (300, 200), (250, 250), 3)  # Kaki kiri
    elif nyawa == 0:
        pygame.draw.line(screen, BLACK, (300, 200), (350, 250), 3)  # Kaki kanan

# Fungsi permainan Hangman
def permainan_hangman():
    kata = ["singa", "kasur", "bunga"]
    kata_terpilih = random.choice(kata)
    huruf_yang_ditebak = []
    kata_tertebak = ['_' for _ in kata_terpilih]
    nyawa = 6

    font = pygame.font.SysFont("arial", 30)
    input_font = pygame.font.SysFont("arial", 40)
    
    running = True
    while running and nyawa > 0 and '_' in kata_tertebak:
        screen.fill(WHITE)
        gambar_hangman(nyawa)  # Menampilkan gambar hangman
        
        # Menampilkan kata yang sedang ditebak
        kata_text = ' '.join(kata_tertebak)
        text = font.render(f"Kata: {kata_text}", True, BLACK)
        screen.blit(text, (20, 20))
        
        # Menampilkan nyawa tersisa
        nyawa_text = font.render(f"Nyawa: {nyawa}", True, BLACK)
        screen.blit(nyawa_text, (20, 60))

        # Menampilkan huruf yang telah ditebak
        tebakan_text = font.render(f"Tebakan: {' '.join(huruf_yang_ditebak)}", True, BLACK)
        screen.blit(tebakan_text, (20, 100))

        # Membaca input pemain
        input_text = input_font.render("Masukkan huruf: ", True, BLACK)
        screen.blit(input_text, (20, 160))

        pygame.display.update()
        
        # Menunggu input pemain
        user_input = ""
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_input = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Jika enter ditekan
                        waiting_for_input = False
                    elif event.key == pygame.K_BACKSPACE:  # Jika backspace ditekan
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode
                    input_box = input_font.render(user_input, True, BLACK)
                    screen.fill(WHITE)
                    screen.blit(input_box, (200, 160))
                    pygame.display.update()

        tebakan = user_input.lower()

        if len(tebakan) != 1 or not tebakan.isalpha():
            continue

        if tebakan in huruf_yang_ditebak:
            continue

        huruf_yang_ditebak.append(tebakan)

        if tebakan in kata_terpilih:
            for idx, huruf in enumerate(kata_terpilih):
                if huruf == tebakan:
                    kata_tertebak[idx] = tebakan
        else:
            nyawa -= 1

    # Menampilkan hasil permainan
    screen.fill(WHITE)
    if '_' not in kata_tertebak:
        result_text = font.render(f"Selamat! Kata: {kata_terpilih}", True, RED)
        screen.blit(result_text, (200, 200))
        webbrowser.open(video_url)
    else:
        result_text = font.render(f"Kamu kalah! Kata yang benar adalah: {kata_terpilih}", True, RED)
        screen.blit(result_text, (100, 200))
    
    pygame.display.update()
    pygame.time.delay(3000)  # Tunda selama 3 detik sebelum keluar

# Memulai permainan
permainan_hangman()
pygame.quit()
