# Reversed Word
# def reverse(word):
#     wordlist = []
#     a = 1
#     b = 0
#     for i in range(len(word)):
#         wordlist.append(word[b:a])
#         a += 1
#         b += 1
#     print(wordlist)
#     c = len(word) - 1
#     word2 = ""
#     for i in range(len(word)):
#         word2 += wordlist[c]
#         c -= 1
#     print(word2)
# reverse("Hello")

# Check Palidrome
# def palindrome(word):
#     wordlist = []
#     a = 1
#     b = 0
#     for i in range(len(word)):
#         wordlist.append(word[b:a])
#         a += 1
#         b += 1
#     print(wordlist)
#     c = len(word) - 1
#     word2 = ""
#     for i in range(len(word)):
#         word2 += wordlist[c]
#         c -= 1
#     print(word2)
#     if word == word2:
#         print("Yes")
#     else:
#         print("No")
# palindrome("racecar")

# Penultimate
# def penultimate(sentence):
#     words = sentence.split(" ")
#     indcount = len(words)
#     indcount -= 2
#     print(words[indcount])
# penultimate("Hi My Name Is Ethan")

# Number Extract
# def num_extractor(sentence):
#     numbers = ""
#     for i in sentence:
#         if i.isdigit():
#             numbers = numbers + i
#     print(numbers)
# num_extractor("I am 16 years old and will be 17 in 2022")

# Start With Counter
# def startswith_count(sentence, letter):
#     sentence = sentence.split(" ")
#     print(sentence)
#     count = 0
#     ind = 0
#     for i in range(len(sentence)):
#         word = sentence[ind]
#         if word[0] == letter:
#             count += 1
#             ind += 1
#         else:
#             ind += 1
#     print(count)
# startswith_count("Hello My Name Is Ethan", "H")

#letter_space_rat
# def letter_space_rat(sentence):
#     spacecount = 0
#     spacecount = sentence.count(" ")
#     lettercount = 0
#     lettercount = len(sentence)
#     lettercount -= spacecount
#     print("There are", spacecount, "spaces to", lettercount, "letters" )
# letter_space_rat("Hello My Name Is Ethan")

# def findall(sentence, letter):
#     sentence = sentence.lower()
#     count = sentence.count(letter)
#     print(count)
# findall("Hello My Name Is Ethan", "m")

def fix_cap(paragraph):
    paragraph = paragraph.replace(" i ", " I ")
    paragraph = paragraph[0].upper() + paragraph[1:]
    sentences = paragraph.split(".")
    newpar = ""
    for sentence in sentences:
        sentence = sentence[0].upper() +sentence[1:]
        newpar +=sentence+"."
    return newpar
print(fix_cap("hello, i want some stuff. i need some pizza"))