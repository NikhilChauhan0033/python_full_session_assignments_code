# 1 Write a Python program which iterates the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for a in range(1,101):
    if(a % 3 == 0 and a % 5 == 0):
        print("FizzBuzz")
    elif(a % 3 == 0):
        print("Fizz")
    elif(a % 5 == 0):
        print("Buzz")   

# 2 Write a Python program to sum the multiples of 3 and 5 under 1000.

sum = 0

for b in range(1,1001):
    if(b % 3 == 0 or b % 5 == 0):
        sum = sum + b
print(sum)

