# warrior
The given code is a simulation game where a player controls a warrior character who moves in a 2D space and fights different creatures. The game is implemented using Python classes and modules. Here is a brief documentation of the code.

Required Modules
random: The random module is used to generate random numbers for actions such as moving and fighting.
Global Variables
distance: A range of values from -5 to 5, used to randomly determine the distance moved by the warrior character in each direction.
action_type: A list of values 0-4, used to determine the type of action the warrior character performs.
increase_decrease: A list of values 1-5, used to randomly determine the magnitude of the health and armor changes.
Warrior Class
__init__: The constructor of the Warrior class initializes the attributes of the warrior character such as name, health, and armor. It also initializes the position (x, y) of the warrior character to (0, 0).
move: The move method randomly changes the position of the warrior character by adding random values from the distance range to the x and y attributes. The new position is then printed.
reduce_armor: The reduce_armor method reduces the armor attribute of the warrior character by 1.
reduce_health: The reduce_health method reduces the health attribute of the warrior character by 1.
increase_armor: The increase_armor method increases the armor attribute of the warrior character by 1.
increase_health: The increase_health method increases the health attribute of the warrior character by 1.
show_health: The show_health method prints the current health attribute of the warrior character.
show_armor: The show_armor method prints the current armor attribute of the warrior character.
Knight, Mage, and Tank Classes
These classes inherit from the Warrior class and have a specialized reduce_health_fight method that reduces the health attribute of the warrior character based on their armor attribute.
Main Code
A Knight object is created with initial attributes (name='Warrior', health=100, armor=10).
A for loop is used to simulate 10 moves for the warrior character. In each iteration, the move method is called and then a random choice is made from the action_type list.
If the choice is 0, the warrior character fights with one of four creatures based on its current position. If the warrior character defeats the creature, its armor and health attributes are updated based on the reduce_health_fight method of the corresponding specialized class. If the warrior character's health attribute falls below 0, the game is over.
If the choice is 1, the warrior character finds an item that increases its health attribute by a random magnitude from the increase_decrease list. The new health attribute is then printed.
If the choice is anything else, the warrior character finds an item that increases its armor attribute by a random magnitude from the increase_decrease list. The new armor attribute is then printed.

Example:
```
-----------------------------------------------------------------------------------------------WELOCOME IN WARRIOR!-----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------MOVE----------------------------------------------------------------------------------------------------
Your current position is [X: 1, Y: -1]
Bad luck! You've eaten a poisoned fruit that decreases your health
------------------------------
Your current armor:  20
------------------------------
Your current health:  98
------------------------------
----------------------------------------------------------------------------------------------------MOVE----------------------------------------------------------------------------------------------------
Your current position is [X: -4, Y: -2]
Gear up Warrior - fight with Troll!
Defeat! You lose your health
------------------------------
Your current armor:  20
------------------------------
Your current health:  18
------------------------------
----------------------------------------------------------------------------------------------------MOVE----------------------------------------------------------------------------------------------------
Your current position is [X: -4, Y: 2]
You are lucky today! You've found new item that increases your health
------------------------------
Your current armor:  20
------------------------------
Your current health:  21
------------------------------
----------------------------------------------------------------------------------------------------MOVE----------------------------------------------------------------------------------------------------
Your current position is [X: -7, Y: 0]
Gear up Warrior - fight with Basilisk!
Defeat! You lose your health
------------------------------
Your current armor:  20
------------------------------
Your current health:  -139
------------------------------
Game over!
```
