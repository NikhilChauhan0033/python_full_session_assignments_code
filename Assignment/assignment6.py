# assignment
# get number from user and print the only even numbers tables

inp1 = int(input("Enter A Number To Print Table : "))

for a in range(1,inp1+1):
    for b in range(1,11):
        if(a % 2 == 0):
            print(f"{a} X {b} = {a*b}")
    print()


