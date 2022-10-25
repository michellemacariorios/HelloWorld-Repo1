# 1

with open('readfile.txt', 'w') as f:
    f.write('Hello!\nMy name is Mary Summers.\nThis is my resume.')

# 2
text_file = open("readfile.txt")

# 3
file1 = open("temps.txt", "r")
lines = file1.readlines()
file2 = open("temps.txt", 'w')
for i in range(len(lines)):
   c = lines[i].strip()
   f = round((float(c) * 1.8) + 32, 2)
   file2.write(str(f) + "\n")
file2.close()

# 4
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

sentences = text.count('.') + text.count('?') + \
    text.count(':') + text.count(';') + \
    text.count('!')

words = len(text.split())
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59))


print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")


