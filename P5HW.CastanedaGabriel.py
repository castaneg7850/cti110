# Gabriel Castaneda
# 4/29/2025
# P5HW
# Create a game

import random

# Function to create a character with 4 attributes
def create_character():
    name = input("Enter your character's name: ")
    character_class = input("Enter your character's class (e.g., Warrior, Mage, Archer): ")
    health = int(input("Enter your character's starting health (number): "))
    strength = int(input("Enter your character's strength level (number): "))

    character = {
        "Name": name,
        "Class": character_class,
        "Health": health,
        "Strength": strength
    }
    return character

# Function to display character details
def display_character(character):
    print("\nCharacter Information:")
    print(f"Name: {character['Name']}")
    print(f"Class: {character['Class']}")
    print(f"Health: {character['Health']}")
    print(f"Strength: {character['Strength']}")

# Function to simulate an attack
def attack_enemy(character):
    enemy_health = random.randint(20, 50)
    print(f"\nAn enemy appears with {enemy_health} health!")

    while enemy_health > 0 and character['Health'] > 0:
        action = input("Do you want to 'attack' or 'run'? ").lower()
        
        if action == 'attack':
            damage = random.randint(5, character['Strength'])
            enemy_health -= damage
            print(f"You attacked and dealt {damage} damage! Enemy's health is now {enemy_health}.")

            if enemy_health > 0:
                enemy_attack = random.randint(5, 15)
                character['Health'] -= enemy_attack
                print(f"The enemy strikes back and deals {enemy_attack} damage! Your health is now {character['Health']}.")
        
        elif action == 'run':
            print("You ran away safely!")
            break
        else:
            print("Invalid action. Try 'attack' or 'run'.")
    
    if enemy_health <= 0:
        print("You defeated the enemy!")
    if character['Health'] <= 0:
        print("You were defeated... Game Over.")

# Function to simulate finding an item
def find_item(character):
    items = ["Health Potion", "Strength Elixir"]
    found_item = random.choice(items)
    print(f"\nYou found a {found_item}!")

    if found_item == "Health Potion":
        character['Health'] += 20
        print("Your health increased by 20!")
    elif found_item == "Strength Elixir":
        character['Strength'] += 5
        print("Your strength increased by 5!")

# Main game logic
def main():
    print("Welcome to the Character Adventure Game!")
    my_character = create_character()
    display_character(my_character)

    while my_character['Health'] > 0:
        print("\nWhat would you like to do next?")
        choice = input("Type 'attack' to fight, 'search' to find items, or 'end' to quit the game: ").lower()

        if choice == 'attack':
            attack_enemy(my_character)
        elif choice == 'search':
            find_item(my_character)
        elif choice == 'end':
            print("\nYou ended the game. Thanks for playing!")
            break
        else:
            print("Invalid choice. Please type 'attack', 'search', or 'end'.")

    if my_character['Health'] <= 0:
        print("\nGame Over. Thanks for playing!")

# Run the game
main()
