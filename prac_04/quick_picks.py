import random

columns = 6
max = 45
min = 1

def main():
    pick_amount = int(input("How many picks?"))
    while pick_amount < 0:
        print("Incorrect Amount of Picks")
        pick_amount = input("How many picks?")
    numberPick(pick_amount)


def numberPick(quickPickAmount):
    for i in range(quickPickAmount):
        pick_list = []
        for a in range(columns):
            pick_range = random.randint(min, max)
            while pick_range in pick_list:
                pick_range = random.randint(min, max)
            pick_list.append(pick_range)
        pick_list.sort()
        print(pick_list)


main()
