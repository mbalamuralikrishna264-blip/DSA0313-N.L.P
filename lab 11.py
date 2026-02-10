i = 0

def S(s):
    global i
    if i < len(s) and s[i] == 'a':
        i += 1
        S(s)
        if i < len(s) and s[i] == 'b':
            i += 1
        else:
            return False
    return True

# Input
s = "aabb"
i = 0

if S(s) and i == len(s):
    print("Accepted")
else:
    print("Rejected")
