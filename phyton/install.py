import pygame

# Inisialisasi pygame
pygame.init()

# Memuat file suara
pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\HP\\Downloads\\Medieval Music Vox Vulgaris - Rokatanc.wav")

# Memainkan suara
pygame.mixer.music.play()

# Agar program tidak langsung berhenti
input("Press Enter to stop the sound...")
pygame.mixer.music.stop()