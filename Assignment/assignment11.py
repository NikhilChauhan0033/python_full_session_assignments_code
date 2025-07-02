# python mini project from classroom

numStudent = int(input("Enter a Number Of Student : "))

def recurssion(n, students=[]):
    if n == 0:
        return students
    
    sName = input("Enter Student Name : ")
    pMarks = int(input("Enter Physics Marks : "))
    mathMarks = int(input("Enter Maths Marks : "))
    cMarks = int(input("Enter Chemistry Marks : "))

    sData = {
        'phy' : pMarks,
        'math' : mathMarks,
        'chem': cMarks
    }

    students.append({sName:sData})
    return recurssion(n-1,students)

students_list = recurssion(numStudent)
print("\nStudent Data:", students_list)
    
