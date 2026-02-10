def print_tree(node, level=0):
    print("  " * level + node)

# Printing parse tree directly
print_tree("S")
print_tree("NP", 1)
print_tree("Det -> the", 2)
print_tree("N -> dog", 2)
print_tree("VP", 1)
print_tree("V -> runs", 2)
