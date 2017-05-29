# define functions
"""its fun """
def add(x, y):
    if int(x) and int(y):
        return x + y
    else:
        return False

# take input from the user
print "Addition of two numbers"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print num1, "+", num2, "=", add(num1, num2)
