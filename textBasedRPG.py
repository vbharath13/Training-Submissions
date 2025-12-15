import random

# Weapon (Used via composition)

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


# Inventory (Composition)

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f" {item} added to inventory")

    def show_items(self):
        if not self.items:
            print(" Inventory is empty")
        else:
            print(" Inventory:", ", ".join(self.items))



# Character

class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.__health = 100        # PRIVATE (data hiding)
        self.inventory = Inventory()

        # Assign weapon based on class
        if char_class == "warrior":
            self.weapon = Weapon("Sword", 15)
        elif char_class == "mage":
            self.weapon = Weapon("Staff", 12)
        else:
            self.weapon = Weapon("Dagger", 10)

    # Encapsulated getter
    def get_health(self):
        return self.__health

    # Encapsulated modifier
    def __take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def attack(self, enemy):
        damage = self.weapon.damage + random.randint(0, 5)
        print(f" {self.name} attacks {enemy.name} with {self.weapon.name}")
        enemy.__take_damage(damage)
        print(f" {enemy.name} takes {damage} damage")

    def heal(self):
        if "potion" in self.inventory.items:
            self.__health += 20
            self.inventory.items.remove("potion")
            print(" Healed 20 health")
        else:
            print(" No potion available")

    def show_status(self):
        print(f"{self.name} ({self.char_class}) - Health: {self.__health}")



# Enemy

class Enemy:
    def __init__(self, name):
        self.name = name
        self.__health = 80

    def __take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def attack(self, player):
        damage = random.randint(8, 14)
        print(f" {self.name} attacks!")
        player._Character__take_damage(damage)
        print(f" {player.name} takes {damage} damage")

    def is_alive(self):
        return self.__health > 0

    def show_status(self):
        print(f"{self.name} - Health: {self.__health}")



# Game Loop

player = Character("Hero", "warrior")
enemy = Enemy("Goblin")

player.inventory.add_item("potion")

while enemy.is_alive() and player.get_health() > 0:
    print("\n--- Battle Menu ---")
    print("1. Attack")
    print("2. Heal")
    print("3. Inventory")

    choice = input("Choose action: ")

    if choice == "1":
        player.attack(enemy)
        if enemy.is_alive():
            enemy.attack(player)
    elif choice == "2":
        player.heal()
    elif choice == "3":
        player.inventory.show_items()
    else:
        print("Invalid choice")

    player.show_status()
    enemy.show_status()

# Result
if player.get_health() > 0:
    print("\n You defeated the enemy!")
else:
    print("\n You were defeated.")
