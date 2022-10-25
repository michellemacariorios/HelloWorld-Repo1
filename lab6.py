# a)
import random
L = []
for i in range(51):
    L.append(random.randint(1,11))
print(L)

# b)

for i in range(len(L)):
    L[i] = L[i] ** 2
print(L)

# c)
k = 50
count = len([i for i in L if i > k])
print("The numbers greater than 50: " + str(count))

# d)
QUESTIONS = [
    ("What is the capital of France?", "Paris"),
    ("What is the longest river in the United States?", "Mississippi"),
    ("Which state has only one neighbor?", "Maine")
]

for questions, correct_answer in QUESTIONS:
    answer = input(f"{questions}")
    if answer == correct_answer:
        print("Correct")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")


# e) 

import string

Sentence = input("Enter a sentence: ")


for i in Sentence:
    if i in string.punctuation:
        print(i)



# f)

import random

names = ['Saida', 'Sonia', 'Ella', 'Vanessa']
blanks=''

chosen =random.choice(names)
print(chosen)

for i in range(len(chosen)):
  blanks+= '_'

print(blanks)


# g)

from random import sample

print(sample(names, 2))

# h)

import random
string1 = input("Enter a string: ")
print(random.choice(string1))

# i)
import random

random.shuffle(names)
print("\nRandom order: ")
print(names)

# j)

middle_index=2
first_part=names[:middle_index]
sec_part=names[middle_index:]


print('The original list is: ',names)
print("First half of list is ",first_part)

print("Second half of list is ",sec_part)

