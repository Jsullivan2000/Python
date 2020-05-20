import random


Num1 = round(random.random() * 10)
Num2 = round(random.random() * 10)
rand_num = int(Num1 * Num2)

num = int(input("Guess a number between 0 and 100"))
tries = 1

if(num == rand_num):
    print("Congradulations! you win!")
while((num != rand_num) and (tries < 3)):
    if (num < rand_num):
        print("Too low, Try again")
    elif (num > rand_num):
        print("Too High, Try again")
    elif(num == rand_num):
        print("Congradulations You Win!")
    num = int(input('Guess again'))
    tries += 1
if (tries >= 3):
    print("Too Bad! Better Luck Next Time")






