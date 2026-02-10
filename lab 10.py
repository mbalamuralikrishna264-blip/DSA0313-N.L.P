def tag(sentence):
    words = sentence.lower().split()

    # Step 1: initial tagging (all NN)
    tags = ['NN'] * len(words)

    # Step 2: apply simple transformation rules
    for i in range(len(words)):
        if words[i] in ['a', 'an', 'the']:
            tags[i] = 'DT'
        elif words[i].endswith('ing'):
            tags[i] = 'VBG'
        elif words[i].endswith('ly'):
            tags[i] = 'RB'
        elif words[i].endswith('s'):
            tags[i] = 'NNS'

    # Step 3: print result
    for i in range(len(words)):
        print(words[i], '->', tags[i])

# Example
tag("The dogs are running quickly")
