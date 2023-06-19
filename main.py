def a(c):
    if len(c) < 1:
        return True
    else:
        if c[0] == c[-1]:
            return a(c[1:-1])
        else:
            return False
b = str(input())
if (a(b) == True):
    print("True")
else:
    print("False")