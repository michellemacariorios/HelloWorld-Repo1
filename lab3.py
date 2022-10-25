# warm up
import random

for i in range(5):
    print('Hello, my name is Michelle.')

# i)
for i in range(3):
    num = eval(input('Enter a number: '))

print('The square of your number is ', num ** 2)
print('The loop is now done.')

# ii)
for i in range(5, 0, -1):
    print(i, end='')
print(' Blast, off!')

# part 2
for i in range(4):
    print('*'*(i+1))

# part 3

r = random.randint(1, 10)
count = 0
while True:
    count += 1
    num = int(input("Enter guess: "))
    if num == r:
        print("You got it!")
    else:
        print("Nice try, maybe next time. Btw, the random number was " + str(r) + ".")
        break
