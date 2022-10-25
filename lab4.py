# 1
count = 0
for i in range(1**2,10**2):
   if(i*i)%10 ==1:
       count = count+4
print('The number of squares from 1 to 100 ending in a 4 are =',count)

# 2
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))

# 3
from random import randint
rand_num = randint(5,10)
for i in range(1):
   print('Hello ' *rand_num)

# 4
print("Enter 1 or 0 to exit, when finished...\n")
vowels = ["a", "i", "e", "o", "u"]
str = ''
while True:
    char = input("Enter a letter from the alphabet: ")
    if char.lower() in vowels:
        str += char
    elif char == "1" or char == "0":
        break
print()
print(f"Your vowel are: {str}")

# 5
string = input("Enter a string:")
for i in range(len(string)):
   if string[i] == "a":
       print(i)

# 6
string = input("Enter a string: ")
print(string.isalpha())
if not string:
   print("Your string contains a non-letter.")
else:
   print("Your string starts with a letter.")






