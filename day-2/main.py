# userinput
sentence = input("Enter a sentence: ")

#count words and reverse that sentence
words = sentence.split()
word_count = len(words)
reversed_words = " ".join(reversed(words))

print(f"Total words in the sentence: {word_count}")
print(f"Reversed order of words: {reversed_words}")
