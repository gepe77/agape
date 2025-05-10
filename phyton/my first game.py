import time
import sys
import random
import webbrowser

# Stats karakter
role = "peasant"
result = None
player_stats = {     # ini disebut dictionary (menyimpan data yang banyak dan bisa berbagai jenis)
    'health': 100,   # Kesehatan pemain
    'strength': 15,  # Kekuatan pemain
    'intelligence': 8,  # Kecerdasan pemain
    'stamina': 15,  # Daya tahan pemain
    'charisma': 7,  # Karisma atau kemampuan berinteraksi
    'inventory': [],  # Barang-barang yang dimiliki pemain
    'level': 1,  # Level karakter
}

# Fungsi untuk menampilkan stats pemain
def show_stats():
    print("\n--- Player Stats ---")
    print(f"Health: {player_stats['health']}")
    print(f"Strength: {player_stats['strength']}")
    print(f"Intelligence: {player_stats['intelligence']}")
    print(f"Stamina: {player_stats['stamina']}")
    print(f"Charisma: {player_stats['charisma']}")
    print(f"Level: {player_stats['level']}")
    print(f"Inventory: {', '.join(player_stats['inventory']) if player_stats['inventory'] else 'Empty'}")
    print("---------------------\n")

# Fungsi untuk mengetikkan teks secara perlahan
def type_writer(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Permainan dimulai
print("Welcome to my game")
video_url = "https://www.youtube.com/watch?v=2qBlE2-WL60"
developer = "developer: Agape"
if developer != "developer: Agape":
    type_writer("this game is hacked the real developer is Agape")
    webbrowser.open(video_url)
    exit()
print(developer)
type_writer("This is a dark fantasy genre game.")
type_writer("are you ready to go to battle field and fight all the enemy?.")
ask = input("Type 'yes' to start: ")
name = input("Input your name: ")

if ask.lower() == "yes":
    def game():
        type_writer("It's a long day since the King of Warmoth attacked the country...")
        time.sleep(1)
        type_writer("People are suffering and the world is full of darkness.")
        time.sleep(1)
        type_writer("You are here to save the world.")
        time.sleep(1)
        type_writer("Story starts in a house of Sterling Village.")
        time.sleep(1)
        type_writer("You just came from the woods to play with your friends.")
        time.sleep(1)
        type_writer("Your grandma is sick right now.")
        time.sleep(1)
        type_writer("Grandma: 'Son, where have you been?'")
        time.sleep(2)

        choices()

    def choices():
        type_writer("Do you want to say:")
        time.sleep(1)
        type_writer("1. Tell her you were playing in the woods with your friends.")
        type_writer("2. Lie and say you were out looking for herbs to help her.")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            tell_truth()
        elif choice == "2":
            lie_to_grandma()
        else:
            type_writer("Invalid choice. Try again!")
            choices()

    def tell_truth():
        type_writer(f"{name}: I just came from the woods playing with my friends.")
        time.sleep(2)
        type_writer("Grandma was disappointed but also grateful for having an honest child.")
        time.sleep(2)
        player_stats['charisma'] += 2
        type_writer(f"Your charisma increased by 2! Current charisma: {player_stats['charisma']}")
        time.sleep(2)
        type_writer(f"{name}:ma i want to go outside see you")
        time.sleep(2)
        continue_story()

    def lie_to_grandma():
        type_writer(f"{name}: I just came from hunting in the woods.")
        time.sleep(2)
        type_writer("Grandma: 'Thank you, my good boy.'")
        time.sleep(2)
        type_writer("Grandma: 'Where is the food?'")
        time.sleep(2)
        type_writer(f"{name}: Uhh... uhh?")
        time.sleep(1)
        type_writer("Grandma: 'Are you lying to me again?'")
        time.sleep(2)
        type_writer(f"{name}:im sorry grandma")
        time.sleep(2)
        type_writer("grandma:getout of here!")
        continue_story()

    def continue_story():
        type_writer("You are outside the house right now.")
        time.sleep(2)
        type_writer("A soldier comes up to you.")
        time.sleep(2)
        type_writer("Soldier: 'Hey young man, you are 12 years old. You are old enough to be a man. Come with us to be a soldier!'")
        time.sleep(2)
        choices2()

    def choices2():
        type_writer("Do you want to:")
        time.sleep(1)
        type_writer("1. Try to escape from them.")
        type_writer("2. Cooperate with them.")
        choice2 = input("Enter the number of your choice: ")

        if choice2 == "1":
            arrested()
        elif choice2 == "2":
            cooperate()
        else:
            type_writer("Invalid choice! Try again.")
            choices2()

    def arrested():
        type_writer("You try to escape, but the soldiers catch you and arrest you.")
        time.sleep(2)
        type_writer("Soldier: 'Gotcha! You can't escape now.'")
        player_stats['charisma'] -= 2
        type_writer(f"Your charisma decreased by 2! Current charisma: {player_stats['charisma']}")
        time.sleep(2)
        barrack()

    def cooperate():
        type_writer("You decide to cooperate with the soldiers. They take you to the barracks.")
        time.sleep(2)
        barrack()

    def barrack():
        type_writer(f"{name}: 'Where am I?'")
        time.sleep(2)
        type_writer("Raider: 'Welcome to the barracks. You will learn how to fight against mages, witches, dragons, soldiers, kings, etc.'")
        time.sleep(2)
        type_writer(f"{name}: 'Wow, I will learn how to fight like a real man?'")
        time.sleep(1)
        type_writer("Raider: 'Say it politely!'")
        time.sleep(1)
        type_writer("Raider: 'In the barracks, the proper response is \"Yes, sir!\" and \"No, sir!\"'")
        time.sleep(2)
        type_writer(f"{name}: 'Sir, yes sir!'")
        time.sleep(2)
        type_writer("Raider: 'Let's start the practice.'")
        training()

    def training():
        type_writer("A training dummy appears in front of you. Let's practice!")
        time.sleep(1)

        # Status musuh (dummy)
        dummy = {'name': 'Training Dummy', 'health': 30, 'attack': 5}

        # Multiplier untuk strength
        strength_multiplier = 0.5

        # Mulai mini-game bertarung
        while dummy['health'] > 0 and player_stats['health'] > 0:
            type_writer(f"{dummy['name']} health: {dummy['health']}")
            type_writer(f"Your health: {player_stats['health']}")
            type_writer(f"Your strength: {player_stats['strength']}")
            type_writer("What will you do?")
            type_writer("1. Attack")
            type_writer("2. Defend")
            choice = input("Choose an action (1/2): ")

            if choice == "1":
                # Hitung damage berdasarkan strength
                base_damage = random.randint(5, 10)
                damage = base_damage + int(player_stats['strength'] * strength_multiplier)
                dummy['health'] -= damage
                type_writer(f"You dealt {damage} damage to {dummy['name']}!")
            
            elif choice == "2":
             # Pertahanan
                defense = random.randint(2, 5)
                reduced_damage = max(dummy['attack'] - defense, 0)
                player_stats['health'] -= reduced_damage
                type_writer(f"You blocked the attack, reducing damage by {defense}.")
            else:
                type_writer("Invalid choice! Try again.")

            # Dummy menyerang
            if dummy['health'] > 0:
                player_stats['health'] -= dummy['attack']
                type_writer(f"{dummy['name']} attacks! You lost {dummy['attack']} health.")

            # Cek jika pemain kalah
            if player_stats['health'] <= 0:
                type_writer("You have been defeated! Training failed.")
                break

        # Jika dummy kalah
        if dummy['health'] <= 0:
            type_writer(f"You defeated the {dummy['name']}! Well done, soldier!")
            player_stats['level'] += 1
            type_writer(f"Your level increased to {player_stats['level']}!")
            question()

    
    def question():
        type_writer("Raider:'are you ready to fight the enemy?'")
        time.sleep(1)
        type_writer("1.'sir,yes sir'")
        type_writer("2. 'no sir'")
        choice3 = input("Enter the number of your choice: ")        

        
        if choice3 == "1":
            war()
        elif choice3 == "2":
            war2()
        else:
            type_writer("Invalid choice! Try again.")
            choices2()

    
    def add_to_inventory(item):
        player_stats['inventory'].append(item)
        print(f"{item} has been added to your inventory.")

    def increase_strength(amount):
        player_stats['strength'] += amount
        print(f"Strength increased by {amount}. Current strength: {player_stats['strength']}")


    def increase_Intelligence(amount):
        player_stats['Intelligence'] += amount
        print(f"Intelligence increased by {amount}. Current Intelligence: {player_stats['Intelligence']}")

    def war():
        type_writer("raider:'Take this sword!'")
        sword = "Mighty Sword"
        add_to_inventory(sword)
        increase_strength(20)  # Menambahkan 20 strength
        choose_role()


    def war2():
        type_writer("raider:'I'm sorry son, life is too hard for you.'")
        type_writer("The war is too intense... You decide to give up.")
        type_writer("Game Over.")
        sys.exit()  # Menghentikan program sepenuhnya




    def change_role(new_role):
        global role
        role = new_role
        type_writer(f"Your role has been changed to {role}.")




    def choose_role():
        type_writer("raider: 'Choose your path, young soldier. Your destiny awaits.'")
        time.sleep(1)
        type_writer("1. Knight - Balanced Strength and Defense")
        type_writer("2. Cavalry - High Speed and Charge Attack")
        type_writer("3. Mage - Powerful Magic, Low Defense")
        type_writer("4. Berserker - High Strength, Low Defense")
        role = input("Enter the number of your chosen role (1/2/3/4): ")

        if role == "1":
            player_stats['strength'] += 15
            player_stats['health'] += 20
            player_stats['stamina'] += 10
            type_writer("You chose the Knight. A balanced warrior with strong defense.")
            type_writer(f"Strength: {player_stats['strength']}, Health: {player_stats['health']}, Stamina: {player_stats['stamina']}")
            return "Knight", player_stats
            gowar()


        elif role == "2":
            player_stats['strength'] += 20
            player_stats['stamina'] += 15
            player_stats['intelligence'] += 5
            type_writer("You chose the Cavalry. A swift and powerful mounted warrior.")
            type_writer(f"Strength: {player_stats['strength']}, Stamina: {player_stats['stamina']}, Intelligence: {player_stats['intelligence']}")
            change_role("Cavalry")
            cavalry_training() 

        elif role == "3":
            player_stats['intelligence'] += 25
            player_stats['health'] += 10
            player_stats['stamina'] += 5
            type_writer("You chose the Mage. Master of destructive magic.")
            type_writer(f"Intelligence: {player_stats['intelligence']}, Health: {player_stats['health']}, Stamina: {player_stats['stamina']}")
            return "Mage", player_stats
            mage()

        elif role == "4":
            player_stats['strength'] += 30
            player_stats['health'] += 5
            player_stats['stamina'] += 5
            type_writer("You chose the Berserker. A raging powerhouse with little defense.")
            type_writer(f"Strength: {player_stats['strength']}, Health: {player_stats['health']}, Stamina: {player_stats['stamina']}")
            return "Berserker", player_stats
            gowar()

        else:
            type_writer("Invalid choice. Choose again.")
            return choose_role()


    def mage():
        type_writer("Mage:welcome to our society")
        time.sleep(2)
        type_writer("Mage:today you will learn how to be great mage")
        time.sleep(2)
        type_writer("Mage:take this wand")
        wand = "magical staff"
        add_to_inventory(wand)
        increase_Intelligence(100) 
        study() 
    
    def study():
        type_writer("Mage: 'Now that you have the magical staff, let's practice your spells.'")
        time.sleep(2)
        type_writer("Mage: 'I will give you a simple spell to cast. Focus and unleash your power!'")
        time.sleep(2)

        # Mini game untuk Mage
        spells = ["Fireball", "Ice Blast", "Thunder Strike"]
        chosen_spell = random.choice(spells)

        type_writer(f"Mage: 'Try to cast the spell {chosen_spell} correctly.'")
        time.sleep(1)
        user_spell = input("Enter the spell: ").strip()

        if user_spell.lower() == chosen_spell.lower():
            type_writer(f"You successfully cast {chosen_spell}! Your intelligence increases.")
            increase_Intelligence(50)
        else:
            type_writer(f"You failed to cast {chosen_spell}. Your stamina decreases.")
            player_stats['stamina'] -= 10
            type_writer(f"Stamina: {player_stats['stamina']}")

        # Kembali ke latihan
        type_writer("Mage: 'Good job. youre ready enough to go to frontline.'")
        time.sleep(2)
        gowar()

    def cavalry_training():
        global role, result
        type_writer("Cavalry Trainer: 'Welcome to the cavalry training ground!'")
        time.sleep(2)
        type_writer("Cavalry Trainer: 'Today, you'll learn how to charge effectively and strike with precision.'")
        time.sleep(2)
        type_writer("Cavalry Trainer: 'Take this spear and mount your horse!'")
    
        # Menambahkan spear ke inventory dan meningkatkan strength
        spear = "Cavalry Spear"
        add_to_inventory(spear)
        increase_strength(65)

        time.sleep(2)
        type_writer("You are now on your horse, facing a line of training dummies.")
        time.sleep(2)
        type_writer("Cavalry Trainer: 'Prepare to charge! Aim for the dummies and strike at the right moment!'")
        time.sleep(2)

        # Mini game
        targets = ["Left", "Center", "Right"]
        hit_count = 0

        for i in range(3):
            target = random.choice(targets)
            type_writer(f"The target appears on the {target}!")
            time.sleep(1)
            user_choice = input("Choose your strike direction (Left/Center/Right): ").strip().capitalize()

            if user_choice == target:
                type_writer("You hit the target! Your strength increases!")
                increase_strength(20)
                hit_count += 1
            else:
                type_writer("You missed the target. Stay focused!")

    # Menentukan hasil latihan
        if hit_count >= 2:
            type_writer(f"You successfully hit {hit_count} targets! Your cavalry skills are improving.")
            player_stats['level'] += 1
            type_writer(f"Your level increased to {player_stats['level']}!")
        else:
            type_writer(f"You only hit {hit_count} targets. You need more practice.")

        type_writer("Cavalry Trainer: 'Good job! Keep practicing to become a true cavalry warrior!'")
        gowar()
        


    def gowar():
        #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
        #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
        #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
        role ,player_stats = choose_role()  #not testen yet
        #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
        #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
        #NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
        type_writer("You step into the battlefield. The air is thick with the scent of blood and steel.")
        time.sleep(2)
        enemy = {"name": "Enemy Soldier", "health": 100, "attack": 15}





                
        type_writer(f"You are fighting as a {role}!")

        while enemy["health"] > 0 and player_stats["health"] > 0:
            type_writer(f"Enemy health: {enemy['health']}")
            type_writer(f"Your health: {player_stats['health']}")
            type_writer("1. Attack")
            type_writer("2. Special Ability")
            action = input("Choose your action (1/2): ").strip()

        # Sistem serangan dan kemampuan khusus berdasarkan role
            if action == "1":
                if role == "Knight":
                    damage == player_stats['strength'] + random.randint(10, 20)
                elif role == "Cavalry":
                    damage = player_stats['strength'] + random.randint(20, 30)
                elif role == "Mage":
                    damage = player_stats['intelligence'] + random.randint(30, 40)
                elif role == "Berserker":
                    damage = player_stats['strength'] + random.randint(30, 50)

                enemy["health"] -= damage
                type_writer(f"You dealt {damage} damage to the {enemy['name']}!")

            elif action == "2":
                if role == "Knight":
                    type_writer("You raise your shield, blocking the next attack completely!")
                    player_stats["stamina"] -= 5
                    enemy["attack"] = 0

                elif role == "Cavalry":
                    type_writer("You charge with your spear, delivering a devastating blow!")
                    damage = player_stats['strength'] * 2
                    enemy["health"] -= damage
                    player_stats["stamina"] -= 10
                    type_writer(f"You dealt {damage} damage but lost 10 stamina!")

                elif role == "Mage":
                    type_writer("You cast a powerful spell, burning the enemy!")
                    damage = player_stats['intelligence'] * 1.5
                    enemy["health"] -= damage
                    player_stats["stamina"] -= 5
                    type_writer(f"You dealt {damage} magic damage but lost 5 stamina!")

                elif role == "Berserker":
                    type_writer("You enter a frenzied state, striking wildly!")
                    damage = player_stats['strength'] * 1.8
                    enemy["health"] -= damage
                    player_stats["health"] -= 10
                    type_writer(f"You dealt {damage} damage but also hurt yourself!")

            else:
                type_writer("Invalid choice. Try again.")
                continue

            # Musuh menyerang
            if enemy["health"] > 0:
                player_stats["health"] -= enemy["attack"]
                type_writer(f"The {enemy['name']} attacks! You lost {enemy['attack']} health.")

    # Hasil pertempuran
        if player_stats["health"] > 0:
            type_writer(f"Victory! You defeated the {enemy['name']}!")
            player_stats["level"] += 3
            type_writer(f"Your level increased to {player_stats['level']}!")
        else:
            type_writer("You have been defeated... The battlefield grows silent.")


game()



        

        

        




 



    
    










