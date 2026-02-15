import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = input("Enter sentence: ")

words = word_tokenize(sentence)

tags = pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN>}"

parser = RegexpParser(grammar)

tree = parser.parse(tags)

print("Noun Phrases:")

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        print(subtree)
