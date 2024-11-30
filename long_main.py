import random

# 1 for Snake, -1 for Water, 0 for Gun
choice = {"s": 1, "w": -1, "g": 0} 
reversedDict = {1: "Snake",-1: "Water", 0: "Gun"} 
computer = random.choice([-1, 0, 1])

youStr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
you = choice[youStr]  

print(f"You choose: {reversedDict[you]}\nComputer choose: {reversedDict[computer]}")

# Comparison logic
if computer == you:
    print("It's a Tie!")
else:
    if computer == -1 and you == 1: 
        print("Snake drinks water, You Win!")  # Water vs Snake = Snake drinks water (Snake wins)
    elif computer == -1 and you == 0:
        print("Water Destroy Gun, Computer Win!")  # Water vs Gun = Gun destroys water (Gun wins)
    elif computer == 1 and you == -1:
        print("Snake drinks water ,Computer Win!")  # Snake vs Water = Snake drinks water (Snake wins)
    elif computer == 1 and you == 0:
        print("Gun shoots snake, You Win!")  # Snake vs Gun = Gun shoots snake (Gun wins)
    elif computer == 0 and you == -1:
        print("Water damages gun, Computer Win!")  # Gun vs Water = Water damages gun (Water wins)
    elif computer == 0 and you == 1:
        print("Gun shoots snake, Computer Win!")  # Gun vs Snake = Gun shoots snake (Gun wins)

