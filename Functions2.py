# Reversed Word
def reverse(word):
    wordlist = []
    a = 1
    b = 0
    for i in range(len(word)):
        wordlist.append(word[b:a])
        a += 1
        b += 1
    print(wordlist)
    c = len(word) - 1
    word2 = ""
    for i in range(len(word)):
        word2 += wordlist[c]
        c -= 1
    print(word2)
reverse("Hello")