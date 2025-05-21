import random
import math

lower = int(input("Lower limit: "))
upper = int(input("Upper limit: "))

x = random.randint(lower, upper)

total_chances = math.ceil(math.log(upper - lower + 1,2))
print(f"\n\tYou have only {total_chances} chances left.")

count = 0
flag = False
while count < total_chances:
    count+= 1

    guess = int(input("Guess: "))

    if x == guess:
        print(f"You guessed the number in {count} tries")

        flag = True
        break

    elif x > guess:
        print("Thats too small, try a higher number")
    elif x < guess:
        print("Thats too high, try a smaller number")

if not flag:
    print("\nThe number is %d" % x)