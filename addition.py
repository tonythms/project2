# define functions
"""its fun """
def add(x, y):
    if int(x) and int(y):
        return x + y
    else:
        return False

# take input from the user
print "Addition of two numbers"

n1 = raw_input("Enter first number: ")
n2 = raw_input("Enter second number: ")

print n1, "+", n2, "=", add(n1, n2)
