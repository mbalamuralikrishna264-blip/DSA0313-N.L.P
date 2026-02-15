# Simple PCFG parser

grammar = {
    ("Ram", "runs"): 0.9,
    ("boy", "runs"): 0.7,
    ("Ram", "eats"): 0.6
}

sentence = input("Enter sentence: ")

words = tuple(sentence.split())

if words in grammar:
    print("Sentence Accepted")
    print("Probability:", grammar[words])
else:
    print("Sentence Rejected")
