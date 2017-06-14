"""prgm"""
def add(att1, att2):
    """prgm"""
    ans = int(att1) + int(att2)
    if ans == 0:
        return ans
    elif att1.isdigit and att2.isdigit:
        return ans
    else:
        return False

# take input from the user
print "Addition of two numbers"

#A = raw_input("Enter first number: ")
#B = raw_input("Enter second number: ")
A = '45'
B = '56'
print A, "+", B, "=", add(A, B)
