from math import factorial
import random
import itertools

standard_dice = sorted(list(range(1, 7)))
sums_standard_dice = sorted(list(a + b for a in standard_dice for b in standard_dice))
used_combinations = list()
max_value = 10

max_iterations = 10 ** 10

for i in range(max_iterations):
    new_dice1 = [1]
    new_dice2 = [1]
    while len(new_dice1) < 6 and len(new_dice2) < 6:
        new_dice1.append(random.randint(2, max_value))
        new_dice2.append(random.randint(2, max_value))

    new_dice1.sort()
    new_dice2.sort()

    if new_dice1 == standard_dice or new_dice2 == standard_dice or max(new_dice1) + max(new_dice2) > 12:
        continue

    if [new_dice1, new_dice2] in used_combinations or [new_dice2, new_dice1] in used_combinations:
        continue

    sums_new_dice = sorted(list(a + b for a in new_dice1 for b in new_dice2))

    if sums_standard_dice == sums_new_dice:
        print("Found an example of Sichemarn dices! They are:\n" + new_dice1.__str__() + "\n" + new_dice2.__str__())
        break

    used_combinations.append([new_dice1, new_dice2])

    if i == max_iterations - 1:
        print("No Sicherman dices found!")
