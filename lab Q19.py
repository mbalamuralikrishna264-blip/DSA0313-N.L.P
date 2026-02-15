import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

sentence = input("Enter sentence: ")
word = input("Enter ambiguous word: ")

sense = lesk(word_tokenize(sentence), word)

print("Meaning:", sense.definition())
