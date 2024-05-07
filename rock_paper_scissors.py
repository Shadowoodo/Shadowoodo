# Rock paper scissors

import random

print("#######################")
print("  Rock Paper Scissors  ")
print("#######################")

choices = {1: "Rock ✊", 2: "Paper ✋", 3: "Scissors ✌️"}

for i in range(1, 4):
    print(f"{i}) {choices[i]}")

Answer = int(input("Pick a number: "))

CPU = random.randint(1, 3)

print(f"\nYou chose: {choices[Answer]}")
print(f"CPU chose: {choices[CPU]}")

if Answer == CPU:
    print("It was a tie!")
elif (Answer == 1 and CPU == 2) or (Answer == 2 and CPU == 3) or (Answer == 3 and CPU == 1):
    print("Computer won!")
else:
    print("The player won!")

input("\nPress Enter to close...")