import math

print "Please type in your coefficients: "
a = input("First coefficient: ")
b = input("Second coefficient: ")
c = input("Third coefficient: ")
print "a: %d b: %d c: %d" % (a, b, c)

root = math.sqrt((b**2)-(4*a*c))
x1 = (-b+root)/(2*a)
x2 = (-b-root)/(2*a)

if x1 != x2:
    print "The answers are: (x1, x2) (%.2f , %.2f)" % (x1, x2)
elif x1 == x2:
    print "The answer is: x = %.2f" % x1
else:
    print("Something went wrong. Please try again.\n")
mainLoop = raw_input("Press the Enter key to close this window.")
