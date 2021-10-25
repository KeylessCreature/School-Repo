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

<<<<<<< HEAD
#Penultimate
=======
# Penultimate
>>>>>>> 7a34286be2dbe35eb7d94e38957b7d88f01506c6
# def penultimate(sentence):
#     words = sentence.split(" ")
#     indcount = len(words)
#     indcount -= 2
#     print(words[indcount])
# penultimate("Hi My Name Is Ethan")

<<<<<<< HEAD
# def printNames(*names):
#     for name in names:
#         print(name)
# printNames("Ethan", "Read")

# def printNames2(first,*names):
#     for name in names:
#         print(first,names)
# printNames2("Ethan", "Read", "Hello")

# def order(ordernum,*items):
#     total = 0
#     for item in items:
#         total += item
#     print(ordernum,total)
# order(1,20,40,50,100)

# def addup(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     print(total)
# addup(10,20,30)

# def smallest(*nums):
#     smallest = nums[0]
#     for num in nums:
#         if smallest > num:
#             smallest = num
#     print(smallest)
# smallest(10,20,30,5)

# def avgPos(*nums):
#     total = 0
#     div = 0
#     for num in nums:
#         if num < 0:
#             num = num * 0
#         else:
#             total += num
#             div += 1
#     if div == 0:
#         print("BAD")
#     else:
#         print(total/div)
# avgPos(10,50,-2,20,-2)

# def power(a,b=2):
#     print(a**b)
# power(2, 4)
# power(5)

# def payed(hours, moneyper=7.25):
#     money = hours * moneyper
#     print("$",money)
# payed(8)
# payed(8, 15)
=======
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

#Fix_Cap
# def fix_cap(paragraph):
#     paragraph = paragraph.replace(" i ", " I ")
#     paragraph = paragraph[0].upper() + paragraph[1:]
#     sentences = paragraph.split(".")
#     newpar = ""
#     for sentence in sentences:
#         sentence = sentence[0].upper() +sentence[1:]
#         newpar +=sentence+"."
#     return newpar
# print(fix_cap("hello, i want some stuff. i need some pizza"))
>>>>>>> 7a34286be2dbe35eb7d94e38957b7d88f01506c6
