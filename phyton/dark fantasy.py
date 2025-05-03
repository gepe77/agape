import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print('\n')

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 15
        self.defense = 5
        self.inventory = []
    
    def is_alive(self):
        return self.hp > 0

def fight(player, enemy):
    print_slow(f"\n{enemy['name']} muncul!")
    while player.is_alive() and enemy['hp'] > 0:
        print_slow(f"HP kamu: {player.hp} | HP {enemy['name']}: {enemy['hp']}")
        action = input("\nApa yang ingin kamu lakukan? Serang (S), Bicara (B), atau Bertahan (D)? ").lower()
        
        if action == 's':
            damage = max(0, player.attack - enemy['defense'])
            enemy['hp'] -= damage
            print_slow(f"Kamu menyerang {enemy['name']} dan memberikan {damage} damage!")
        elif action == 'b':
            if 'talk' in enemy:
                print_slow(enemy['talk'])
                if 'pacify' in enemy:
                    print_slow(f"{enemy['name']} merasa damai dan pergi...")
                    return
            else:
                print_slow(f"{enemy['name']} tidak mengerti kata-katamu...")
        elif action == 'd':
            block = random.randint(5, 10)
            player.defense += block
            print_slow(f"Kamu bertahan dan meningkatkan pertahanan sebesar {block}!")
        
        if enemy['hp'] > 0:
            enemy_damage = max(0, enemy['attack'] - player.defense)
            player.hp -= enemy_damage
            print_slow(f"{enemy['name']} menyerang dan memberikan {enemy_damage} damage!")
            player.defense -= block  # Reset pertahanan setelah serangan musuh
        
    if player.is_alive():
        print_slow(f"\nKamu telah mengalahkan {enemy['name']}!")
        if 'drop' in enemy:
            print_slow(f"{enemy['name']} menjatuhkan {enemy['drop']}!")
            player.inventory.append(enemy['drop'])
    else:
        print_slow("\nKegelapan telah menelanmu...")
        exit()

def explore_ruins(player):
    print_slow("\nKamu menjelajahi reruntuhan kastil dan menemukan sebuah pintu tersembunyi...")
    choice = input("Buka pintu (B) atau Lewati (L)? ").lower()
    if choice == 'b':
        print_slow("Pintu terbuka, dan di dalamnya terdapat harta karun serta makhluk yang menjaganya!")
        fight(player, {"name": "Penjaga Harta", "hp": 60, "attack": 14, "defense": 8, "drop": "Pedang Legendaris", "talk": "Kau tak akan mengambil harta ini begitu saja!", "pacify": False})
    else:
        print_slow("Kamu memutuskan untuk meninggalkan pintu dan melanjutkan perjalanan.")

def start_adventure():
    print_slow("Selamat datang di dunia kegelapan...")
    name = input("Masukkan nama karaktermu: ")
    player = Player(name)
    
    print_slow("\nKamu tiba di gerbang kota Shadowmere yang sunyi dan dipenuhi kabut hitam...")
    choice = input("Masuk ke kota (M) atau Pergi ke hutan gelap (H)? ").lower()
    
    if choice == 'm':
        print_slow("\nDi dalam kota, kamu bertemu dengan seorang pengemis misterius...")
        choice2 = input("Berikan koin (B) atau Abaikan (A)? ").lower()
        if choice2 == 'b':
            print_slow("Pengemis memberimu jimat perlindungan!")
            player.defense += 5
            player.inventory.append("Jimat Perlindungan")
        else:
            print_slow("Pengemis berubah menjadi iblis dan menyerang!")
            fight(player, {"name": "Iblis Pengemis", "hp": 40, "attack": 10, "defense": 3, "drop": "Pedang Terkutuk", "talk": "Iblis hanya tertawa kejam...", "pacify": False})
    else:
        print_slow("\nKamu memasuki hutan gelap dan dikejutkan oleh serigala bayangan!")
        fight(player, {"name": "Serigala Bayangan", "hp": 30, "attack": 8, "defense": 2, "drop": "Cakar Serigala", "talk": "Serigala hanya menggeram...", "pacify": False})
    
    print_slow("\nPetualanganmu baru saja dimulai...")
    print_slow(f"\nInventori: {player.inventory}")
    
    print_slow("Kamu melanjutkan perjalanan dan melihat dua jalur: menuju reruntuhan kastil (K) atau lembah kabut (L)...")
    choice3 = input("Kemana kamu akan pergi? ").lower()
    
    if choice3 == 'k':
        print_slow("\nKamu tiba di reruntuhan kastil yang penuh aura jahat...")
        fight(player, {"name": "Ksatria Terkutuk", "hp": 50, "attack": 12, "defense": 6, "drop": "Armor Kuno", "talk": "Ksatria tampak ragu...", "pacify": True})
        explore_ruins(player)
    else:
        print_slow("\nLembah kabut menyembunyikan banyak bahaya, tiba-tiba makhluk bayangan muncul!")
        fight(player, {"name": "Penjaga Bayangan", "hp": 45, "attack": 11, "defense": 5, "drop": "Jubah Kegelapan", "talk": "Makhluk itu berbisik tentang masa lalu...", "pacify": True})
    
    print_slow("\nPetualangan masih panjang, dan kegelapan semakin mendekat...")
    
    print_slow("\nKamu menemukan sebuah kuil kuno, di dalamnya terdapat pilihan: Ambil relik suci (R) atau tinggalkan (T)...")
    choice4 = input("Apa yang akan kamu lakukan? ").lower()
    if choice4 == 'r':
        print_slow("\nKamu mengambil relik suci, tetapi dewa kegelapan bangkit dan menyerang!")
        fight(player, {"name": "Dewa Kegelapan", "hp": 80, "attack": 20, "defense": 10, "drop": "Cahaya Harapan", "talk": "Manusia bodoh, kau menantang takdir!", "pacify": False})
    else:
        print_slow("\nKamu meninggalkan kuil dengan selamat, perasaan aneh menyelimuti hatimu...")
    
    print_slow("\nAkhir dari petualangan masih jauh, tetapi nasib duniamu kini di tanganmu...")

start_adventure()
