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

#Check Palidrome
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

#Penultimate
def penultimate(sentence):
    words = sentence.split(" ")
    indcount = len(words)
    indcount -= 2
    print(words[indcount])
penultimate("Hi My Name Is Ethan")