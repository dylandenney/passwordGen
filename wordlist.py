import nltk
nltk.download('words')  # Download the word list corpus

from nltk.corpus import words
word_list = words.words()  # Access the word list

print(word_list[:10])  # Print the first 10 words as a sample

