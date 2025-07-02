# starting user defined module
# user defined module is known as create over own module

# here create my all module and use it at session12.py 

def hello_msg(name):
    print(f"Hello {name}")

def square(a,b):
    for i in a:
        b.append(i ** 2)
    return b
    
def reverse(c,d):
    for j in c:
        d.insert(0,j)
    return d

def sum1(e):
    total = 0
    for k in e:
        total += k
    return total

def myReplace(text,oldText,newText):
    return text.replace(oldText,newText)