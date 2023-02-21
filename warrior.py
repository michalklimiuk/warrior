import random

distance = range(-5, 5)
action_type = [0, 1, 2, 3, 4]
increase_decrease = [1,2,3,4,5]

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
        self.health -= 1

    def increase_armor(self):
        self.armor += 1

    def increase_health(self):
        self.health += 1

    def show_health(self):
        print("Your current health: ", self.health)
    
    def show_armor(self):
        print("Your current armor: ", self.armor)

class Knight(Warrior):
    def __init__(self, name: str, health: int, armor: int):
        super().__init__(name, health, armor)

    def reduce_health_fight(self):
        self.health -= 1 * self.armor
    
class Mage(Warrior):
    def __init__(self, name: str, health: int, armor: int):
        super().__init__(name, health, armor)

    def reduce_health_fight(self):
        self.health -= 2 * self.armor

class Tank(Warrior):
    def __init__(self, name: str, health: int, armor: int):
        super().__init__(name, health, armor)
    
    def reduce_health_fight(self):
        self.health -= 0.5 * self.armor

warrior1 = Knight('Warrior', 100, 10)


print("-----" * 19 + 'WELOCOME IN WARRIOR!' + "-----" * 19)


for move in range(10):
        print("-----" * 20 + 'MOVE' + "-----" * 20)
        warrior1.move()
        choice = random.choice(action_type)
        # fight cases
        if choice == 0:
            if ((warrior1.x + warrior1.y)**2) % 2 == 0 and ((warrior1.x + warrior1.y)**2) < 20:
                print("Gear up Warrior - fight with Crab!")
                fight_random = random.randint(0, 100)
                if fight_random < 50:
                    print("Defeat! You lose your health")
                    for i in range(2):
                        warrior1.reduce_health_fight()
                if fight_random > 50:
                    print("Victory! Continue your journey")
                print('---'*10)
                warrior1.show_armor()
                print('---'*10)
                warrior1.show_health()
                print('---'*10)
                if warrior1.health < 0:
                    print("Game over!")
                    break
                
            
            if ((warrior1.x + warrior1.y)**2) % 2 == 0 and ((warrior1.x + warrior1.y)**2) > 20:
                print("Gear up Warrior - fight with Troll!")
                fight_random = random.randint(0, 100)
                if fight_random < 50:
                    print("Defeat! You lose your health")
                    for i in range(4):
                        warrior1.reduce_health_fight()
                if fight_random > 50:
                    print("Victory! Continue your journey")
                print('---'*10)
                warrior1.show_armor()
                print('---'*10)
                warrior1.show_health()
                print('---'*10)
                if warrior1.health < 0:
                    print("Game over!")
                    break

            if ((warrior1.x + warrior1.y)**2) % 2 != 0 and ((warrior1.x + warrior1.y)**2) < 20:
                print("Gear up Warrior - fight with Basilisk!")
                fight_random = random.randint(0, 100)
                if fight_random < 50:
                    print("Defeat! You lose your health")
                    for i in range(6):
                        warrior1.reduce_health_fight()
                if fight_random > 50:
                    print("Victory! Continue your journey")
                print('---'*10)
                warrior1.show_armor()
                print('---'*10)
                warrior1.show_health()
                print('---'*10)
                if warrior1.health < 0:
                    print("Game over!")
                    break

            if ((warrior1.x + warrior1.y)**2) % 2 != 0 and ((warrior1.x + warrior1.y)**2) > 20:
                print("Gear up Warrior - fight with Basilisk!")
                fight_random = random.randint(0, 100)
                if fight_random < 50:
                    print("Defeat! You lose your health")
                    for i in range(8):
                        warrior1.reduce_health_fight()
                if fight_random > 50:
                    print("Victory! Continue your journey")
                print('---'*10)
                warrior1.show_armor()
                print('---'*10)
                warrior1.show_health()
                print('---'*10)
                if warrior1.health < 0:
                    print("Game over!")
                    break
        
        if choice == 1:
            # health boost
            print("You are lucky today! You've found new item that increases your health")
            multiplier = random.choice(increase_decrease)
            for i in range(multiplier):
                warrior1.increase_health()
            print('---'*10)
            warrior1.show_armor()
            print('---'*10)
            warrior1.show_health()
            print('---'*10)
            
        if choice == 2:
            # health reduction
            print("Bad luck! You've eaten a poisoned fruit that decreases your health")
            multiplier = random.choice(increase_decrease)
            for i in range(multiplier):
                warrior1.reduce_health()
            print('---'*10)
            warrior1.show_armor()
            print('---'*10)
            warrior1.show_health()
            print('---'*10)
            if warrior1.health < 0:
                print("Game over!")
                break
               
        if choice == 3:
            # armor boost
            print("You are lucky today! You've found new item that increases your armor")
            multiplier = random.choice(increase_decrease)
            for i in range(multiplier):
                warrior1.increase_armor()
            print('---'*10)
            warrior1.show_armor()
            print('---'*10)
            warrior1.show_health()
            print('---'*10)
            if warrior1.health < 0:
                print("Game over!")
                break
        
        if choice == 4:
            #armor reduction
            print("Bad luck! You've stepped into a trap that decreases your armor")
            multiplier = random.choice(increase_decrease)
            for i in range(multiplier):
                warrior1.reduce_armor()
            print('---'*10)
            warrior1.show_armor()
            print('---'*10)
            warrior1.show_health()
            print('---'*10)
        print("Congrats! You have finished your journey, Warrior")

    
            



    



    