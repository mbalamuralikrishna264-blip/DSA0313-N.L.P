expression = input("Enter expression (Example: Loves(Ram,Sita)): ")

predicate = expression.split("(")[0]

arguments = expression.split("(")[1].replace(")", "").split(",")

print("Predicate:", predicate)

print("Arguments:", arguments)
