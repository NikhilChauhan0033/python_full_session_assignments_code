# Q1) delete 3rd key value
people = {
1: {'name': 'John', 'age': '27', 'gender': 'Male'},
2: {'name': 'Marie', 'age': '22', 'gender': 'Female'},
3: {'name': 'Luna', 'age': '24', 'gender': 'Female'},
4: {'name': 'Peter', 'age': '29', 'gender': 'Male'}
}

# expected output:
# {1: {'name': 'John', 'age': '27', 'gender': 'Male'},
# 2: {'name': 'Marie', 'age': '22', 'gender': 'Female'},
# 4: {'name': 'Peter', 'age': '29', 'gender': 'Male'}}


people.pop(3)
print(people)


# Q2) print the following values
data = {'a': 1,'c': {'m': 2,'n': {'x': 5,'y' : [7, 8, 9]}},'d': [1, 2, 3]}
# expected output :
# 5
# 2
# 8


print(data["c"]["n"]["x"])
print(data["c"]["m"])
print(data["c"]["n"]["y"][1])