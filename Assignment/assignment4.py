# Q1) Accept the percentage from the user
# and display the grade according to the
# following criteria:
# Below 25 —- D
# 25 to 45 —- C
# 45 to 50 —- B
# 50 to 60 –– B+
# 60 to 80 — A
# Above 80 –- A+

# inp1 = int(input("Enter Your Percentage : "))

# if(inp1>=80):
#     print("Your Grade is A+")
# elif(inp1<=80 and inp1>=60):
#     print("Your Grade is A")
# elif(inp1<=60 and inp1>=50):
#     print("Your Grade is B+")
# elif(inp1<=50 and inp1>=45):
#     print("Your Grade is B")
# elif(inp1<=45 and inp1>=25):
#     print("Your Grade is C")
# else:
#     print("Your Grade is D")

# Q2) Accept three sides of a triangle and check
# whether it is an equilateral, isosceles or
# scalene triangle.

# Equilateral Triangle → All three sides are equal.
# Isosceles Triangle → Any two sides are equal.
# Scalene Triangle → All three sides are different.

# side1 = int(input("Enter Side 1 : "))
# side2 = int(input("Enter Side 2 : "))
# side3 = int(input("Enter Side 3 : "))

# if(side1 == side2 == side3):
#     print("The triangle is Equilateral.")
# elif(side1==side2 or side2==side3 or side1==side3):
#     print("The triangle is Isosceles.")
# else:
#     print("The triangle is Scalene.")


# Q3) Write a program to check
# whether the last digit of a number(
# entered by user ) is divisible by 3 or
# not.
# (hint : any number % 10 will return the last
# digit)

# num = int(input("Enter A Number : "))

# lastDigit = num % 10 #(find the last number by % 10)

# if lastDigit % 3 == 0:
#     print("The last digit", lastDigit, "is divisible by 3.")
# else:
#     print("The last digit", lastDigit, "is not divisible by 3.")



# Q4) Convert month name to a number of
# days(if else)
# "january", "march", "may", "july", "august", "october", "december" has 31 days
# "april", "june", "september", "november" has 30 days
# february has 28 29 days (leap year dependent)

# Month = input("Enter Month Name : ")
# Month = Month.lower()

# if(Month == "january" or Month == "march" or Month == "may" or Month == "july" or Month == "march" or Month == "october" or Month == "december"):
#     print(f"{Month.capitalize()} has 31 Days")
# elif(Month == "april" or Month == "june" or Month == "september" or Month == "november"):
#     print(f"{Month.capitalize()} has 30 Days")
# elif(Month == "february"):
#     print(f"{Month.capitalize()} has 28 or 29 Days (leap year dependent)")
# else:
#     print("Invalid month name. Please enter a valid month.")

# Q5) Take input from the user and find the
# median of three values

# n7 = int(input("Enter Your 1st Number"))
# n8 = int(input("Enter Your 2nd Number"))
# n9 = int(input("Enter Your 3rd Number"))

# if((n8>n7 and n7>n9) or (n9>n7 and n7>n8)):
#     print(n7)
# elif((n7>n8 and n8>n9) or (n9>n8 and n8>n7)):
#     print(n8)
# else:
#     print(n9)

# another way to write Q5)
# if(n8>n7>n9 or n9>n7>n8):
#     print(n7)
# elif(n7>n8>n9 or n9>n8>n7):
#     print(n8)
# else:
#     print(n9)


# Q6) Python program to enter week number
# and print day of week

# weekNumber = int(input("Enter a Week Number : "))

# if(weekNumber == 1):
#     print("Monday")
# elif(weekNumber == 2):
#     print("Tuesday")
# elif(weekNumber == 3):
#     print("Wednesday")
# elif(weekNumber == 4):
#     print("Thursday")
# elif(weekNumber == 5):
#     print("Friday")
# elif(weekNumber == 6):
#     print("Saturday ")
# else:
#     print("Sunday")


# Q7) Python program to check vowel.

# vowel = input("Enter A Vowel : ")

# if(vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u" or vowel == "A" or vowel == "E" or vowel == "I" or vowel == "O" or vowel == "U"):
#     print(f"{vowel} is vowel")
# else:
#     print(f"{vowel} is not vowel")

# Q8) Python program to find maximum
# between three numbers

# inp1 = int(input("Enter 1st Number : "))
# inp2 = int(input("Enter 2nd Number : "))
# inp3 = int(input("Enter 3rd Number : "))

# if(inp1>inp2 and inp1>inp3):
#     print(f"{inp1} is Maximum")
# elif(inp2>inp1 and inp2>inp3):
#     print(f"{inp2} is Maximum")
# else:
#     print(f"{inp3} is Maximum")
