# Basic arithmetic

num1 = 10
num2 = 5
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)   

#String Manipulation

text = "Hello, World!"
length = len(text)
upper_case = text.upper()
lower_case = text.lower()
print("Length:", length)
print("Upper case:", upper_case)
print("Lower case:", lower_case)

#conditional Statements

age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


#Loops

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

#tuples

# Creating a tuple
my_tuple = (1, 2, "hello", True)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Trying to modify a tuple (will raise an error)
# my_tuple[0] = 3  # This line will cause an error

# Tuple functions
print(len(my_tuple))  # Output: 4
print(my_tuple.index("hello"))  # Output: 2
print(my_tuple.count(2))  # Output: 1

#Dictionaries
# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing values
print(my_dict["name"])  # Output: Alice

# Adding a key-value pair
my_dict["occupation"] = "Engineer"

# Modifying a value
my_dict["age"] = 31

# Deleting a key-value pair
del my_dict["city"]

# Dictionary functions
print(len(my_dict))  # Output: 3
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'occupation'])
print(my_dict.values())  # Output: dict_values(['Alice', 31, 'Engineer'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('occupation', 'Engineer')])


#List

# Creating a list
my_list = [10, "apple", True, [1, 2, 3]]

# Accessing elements
print(my_list[1])  # Output: apple

# Modifying elements
my_list[0] = 20

# Adding elements
my_list.append("banana")
my_list.insert(2, "orange")

# Removing elements
my_list.remove("apple")
del my_list[0]

# List functions
print(len(my_list))  # Output: 4
print(my_list.index("orange"))  # Output: 2
print(my_list.count(True))  # Output: 1
my_list.sort()  # Sorts the list in ascending order
my_list.reverse()  # Reverses the order of elements



