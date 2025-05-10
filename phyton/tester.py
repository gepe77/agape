import sys
import time

player_stats = {
    "strength": 0,
    "health": 0,
    "stamina": 0,
    "intelligence": 0
}
role = "nigga"




def type_writer(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()



def choose_role():


    type_writer("raider: 'Choose your path, young soldier. Your destiny awaits.'")
    type_writer("1. Knight - Balanced Strength and Defense")
    type_writer("2. Cavalry - High Speed and Charge Attack")
    type_writer("3. Mage - Powerful Magic, Low Defense")
    type_writer("4. Berserker - High Strength, Low Defense")
    choice = input("Enter the number of your chosen role (1/2/3/4): ")

    if choice == "1":
        player_stats['strength'] += 15
        player_stats['health'] += 20
        player_stats['stamina'] += 10
        type_writer("You chose the Knight. A balanced warrior with strong defense.")
        return "Knight", player_stats

    elif choice == "2":
        player_stats['strength'] += 20
        player_stats['stamina'] += 15
        player_stats['intelligence'] += 5
        type_writer("You chose the Cavalry. A swift and powerful mounted warrior.")
        return "Cavalry", player_stats

    elif choice == "3":
        player_stats['intelligence'] += 25
        player_stats['health'] += 10
        player_stats['stamina'] += 5
        type_writer("You chose the Mage. Master of destructive magic.")
        return "Mage", player_stats

    elif choice == "4":
        player_stats['strength'] += 30
        player_stats['health'] += 5
        player_stats['stamina'] += 5
        type_writer("You chose the Berserker. A raging powerhouse with little defense.")
        return "Berserker", player_stats

    else:
        type_writer("Invalid choice. Choose again.")
        return choose_role()

# Panggil fungsi dan dapatkan hasilnya
role, player_stats = choose_role()
print(f"Your role is: {role}")
print(f"Your stats: {player_stats}")
