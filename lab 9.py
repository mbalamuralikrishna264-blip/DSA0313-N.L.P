sentence = "I am playing cricket"
words = sentence.split()

tags = {}

for w in words:
    tags[w] = "NN"

for w in words:
    if w.lower() in ["i", "he", "she"]:
        tags[w] = "PRP"
    elif w.lower() in ["am", "is", "are"]:
        tags[w] = "VBP"
    elif w.endswith("ing"):
        tags[w] = "VBG"

print("Word Tag")
for w in words:
    print(w, tags[w])
