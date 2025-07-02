def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Number of terms
terms = int(input("Enter the number of terms: "))

# Printing Fibonacci series
print("Fibonacci Series:")
for i in range(1, terms + 1):
    print(fibonacci(i), end=" ")