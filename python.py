# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

x = [[5, 2, 3], [15, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Bryant'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Andres', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 30}]


def Dictionary(TheList: list):
    for item in TheList:
        if item:
            keys = sorted(list(item.keys()))
            match = [key - item[key] for key in keys]
            a = ", ".join(match)
            print(a)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def Dictionary2(name, TheList):
    for item in TheList:
        print(item.get(name))


def printInfo(dictionary):
    for key, value in dictionary.items():
        print((len(value),key.upper()))
        for item in value:
            print(item)
        print()


printInfo(dojo)