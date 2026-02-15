import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = input("Enter text: ")

words = word_tokenize(text)
tags = pos_tag(words)

last_noun = None

print("Reference Resolution:")

for word, tag in tags:
    if tag in ['NN', 'NNP']:
        last_noun = word

    elif tag == 'PRP':
        print(word, "refers to", last_noun)
