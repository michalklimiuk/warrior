import random

distance = range(-6, 6)
action_type = [0, 1, 2 , 3]

class Warrior:
    def __init__(self, name: str, health: int, armor: int):
        self.x = 0
        self.y = 0    
        self.name = name
        self.health = health
        self.armor = armor

    def move(self):
        self.x += random.choice(distance)
        self.y += random.choice(distance)
        print(f"Your current position is [X: {self.x}, Y: {self.y}]")

    def reduce_armor(self):
        self.armor -= 1

    def reduce_health(self):
        self.health -= 1 * self.armor

warrior1 = Warrior('Warrior', 100, 10)


for move in range(5):
    warrior1.move()
    choice = random.choice(action_type)
    # fight cases
    if choice == 0:
        if ((warrior1.x + warrior1.y)**2) % 2 == 0:
            print("Gear up Warrior - fight with Crab!")

        if ((warrior1.x + warrior1.y)**2) % 2 != 0:
            print("Gear up Warrior - fight with Basilisk!")


    