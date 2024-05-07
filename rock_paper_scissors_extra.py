import random

print("#######################")
print("  Rock Paper Scissors  ")
print("#######################")

choices = {1: "Rock ✊", 2: "Paper ✋", 3: "Scissors ✌️", 4: "Spock 🖖", 5: "Lizard 🦎"}

for i in range(1, 6):
    print(f"{i}) {choices[i]}")

Answer = int(input("Pick a number: "))

CPU = random.randint(1, 5)

print(f"\nYou chose: {choices[Answer]}")
print(f"CPU chose: {choices[CPU]}")

if Answer == CPU:
    print("It was a tie!")
elif (Answer == 1 and CPU == 2) or (Answer == 2 and CPU == 3) or (Answer == 3 and CPU == 1) or (Answer == 1 and CPU == 5) or (Answer == 5 and CPU == 4) or (Answer == 4 and CPU == 3) or (Answer == 3 and CPU == 5) or (Answer == 5 and CPU == 2) or (Answer == 2 and CPU == 4) or (Answer == 4 and CPU == 3):
    print("Computer won!")
else:
    print("The player won!")

input("\nPress Enter to close...")