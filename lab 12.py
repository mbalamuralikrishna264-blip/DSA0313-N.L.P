grammar = {
    'S': ['A'],
    'A': ['a']
}

def earley_parse(word):
    chart = [set() for _ in range(len(word) + 1)]
    chart[0].add(('S', 0))

    for i in range(len(word) + 1):
        for state in list(chart[i]):
            lhs, dot = state
            rule = grammar[lhs]

            # Scan
            if dot < len(rule) and i < len(word) and rule[dot] == word[i]:
                chart[i + 1].add((lhs, dot + 1))

    return ('S', 1) in chart[len(word)]

# Test
print("Accepted" if earley_parse("a") else "Rejected")
