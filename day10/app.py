print("-------Anagram checker!-------")

word1=input("Enter your first word:")
word2=input("Enter your second word:")


def is_anagram (word1, word2):
    word1 = word1.replace(" ","").lower()
    word2 = word2.replace(" ","").lower()

    if sorted(word1)== sorted(word2):
        return("Yes, it's an angram!")
    else:
        return("No, it's not an anagram!")

print(is_anagram(word1, word2))    