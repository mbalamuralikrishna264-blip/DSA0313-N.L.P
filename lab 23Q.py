text = input("Enter text: ")

sentences = text.split(".")

score = 0

for i in range(len(sentences)-1):

    words1 = set(sentences[i].split())
    words2 = set(sentences[i+1].split())

    common = words1.intersection(words2)

    score += len(common)

print("Coherence Score:", score)
