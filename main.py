import random

choice = {"s": 1, "w": -1, "g": 0}
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"}
computer = random.choice([-1, 0, 1])

youStr = input("Enter your choice (s, w, g): ")
if youStr not in choice:
    print("Invalid choice! Please enter s, w, or g.")
    exit()

you = choice[youStr]

print(f"You chose: {reversedDict[you]}\nComputer chose: {reversedDict[computer]}")

if computer == you:
    print("It's a Tie!")
else:
    if (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print(f"You Win! {reversedDict[you]} beats {reversedDict[computer]}")
    else:
        print(f"Computer Wins! {reversedDict[computer]} beats {reversedDict[you]}")


# Short Method

# if((computer - you) == -1 or (computer - you) == 2):
#     print(f"Computer Wins! {reversedDict[computer]} beats {reversedDict[you]}")
# else:
#     print(f"You Win! {reversedDict[you]} beats {reversedDict[computer]}")