import pygame 
import time
pygame.init()

W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("work simulator")

putih = (255,255,255)
hitam = (0,0,0)
abu = (200,200,200)
abutua = (100,100,100)

font = pygame.font.SysFont(None, 32)

energi = 100
uang = 100
hari = 1
maks_hari = 10

kerja = pygame.Rect(400, 50, 150, 40)
istirahat = pygame.Rect(400,110,150,40)
belanja = pygame.Rect(400,170,150,40)

run = True

while run:
    screen.fill(putih)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    teks_energi = font.render(f"Energi: {energi}", True,hitam)
    teks_uang = font.render(f"uang: Rp{uang}", True,hitam)
    teks_hari = font.render(f"hari: {hari}", True,hitam)

    screen.blit(teks_energi,(20,20))
    screen.blit(teks_uang,(20,60))
    screen.blit(teks_hari,(20,100))

    pygame.draw.rect(screen, abu, kerja)
    pygame.draw.rect(screen, abu, istirahat)
    pygame.draw.rect(screen, abu, belanja)

    screen.blit(font.render("kerja",True,hitam), (kerja.x + 40, kerja.y + 8))
    screen.blit(font.render("istirahat",True,hitam), (istirahat.x + 20, istirahat.y + 8))
    screen.blit(font.render("Belanja",True,hitam), (belanja.x + 30, belanja.y + 8))

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()

        if kerja.collidepoint(mouse_pos):
            if energi >= 20:
                uang += 50
                energi -= 20
                hari += 1

        if istirahat.collidepoint(mouse_pos):
            energi = min(energi + 30,100)
            hari += 1


        if belanja.collidepoint(mouse_pos):
            if uang >= 50:
                uang -= 50
                hari += 1

    def gameover(uang):
        screen.fill((0,0,0))

        judul = font.render("GAME OVER", True, (255,0,0))
        skor = font.render(f"uang y7ang kamu kumpulkan: Rp{uang}", True, (255,255,255))
        info = font.render("tekan tombol x untuk keluar", True, (255,255,255))

        screen.blit(judul,(W//2 - judul.get.W() //2 , 120))
        screen.blit(skor,(W//2 - judul.get.W() //2 , 170))
        screen.blit(info,(W//2 - judul.get.W() //2 , 220))

        if hari > maks_hari:
            gameover(uang)
            run = False


    pygame.display.flip()
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False

pygame.quit()