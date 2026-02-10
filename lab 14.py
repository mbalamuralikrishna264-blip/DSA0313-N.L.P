def check(sentence):
    words = sentence.lower().split()

    if words[1].endswith('s') and not words[2].endswith('s'):
        print("Agreement Correct")
    elif not words[1].endswith('s') and words[2].endswith('s'):
        print("Agreement Correct")
    else:
        print("Agreement Incorrect")

# Examples
check("The boy runs")
check("The boys runs")
