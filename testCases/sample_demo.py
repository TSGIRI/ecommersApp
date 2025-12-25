'''
import random
import string


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Example 1: simple random string
print("Random string:", random_generator())

# Example 2: random string of length 12
print("12-char string:", random_generator(12))

# Example 3: use in Selenium test (generate email)
email = random_generator(10) + "@test.com"
print("Generated Email:", email)

def add_sum(a, b):
    return a+b

x = add_sum(3,5)
print(x)

'''
import copy
import uuid

'''
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")
    print(str(self.year) +" " + self.model + " " +self.brand )

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

'''
'''
def greet(name):
    return "Hello, " + name

def welcome(name):
    message = greet(name)
    print(message + "! Welcome to our website.")
welcome("seshagiri")
'''
'''
#--------------- exception handling  - (try - except - finally)-----------------
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return f"The result is: {result}"
    finally:
        print("Execution completed.")

print(divide_numbers(10, 2))  # Valid division
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, 'a'))  # Invalid input type

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    print("Finished attempting to read the file.")


try:
    x = 10 / 0
except Exception as e:
    print("unexpected error occurred: ", e)  # division by zero
finally:
    print("Execution of the try-except block is complete.")

'''
a = 10
a = 20
print(a)  #20

l1 = [1,2,3]
l2 = copy.copy(l1)
print("l1 : ", l1, id(l1))
print("l2 : ", l2, id(l2))
l2[1] = 200
print("After modification:")
print("l1 : ", l1)  #[1, 2, 3]
print("l2 : ", l2)  #[1, 200, 3]




d = {'a':1, 'b':2}
d2 = copy.copy(d)
print(d2)
d['c'] = 3
print(d)  #{'a': 1, 'b': 2, 'c': 3}
print(d2)  #{'a': 1, 'b': 2}

endpoint = "users"
print(endpoint+"/1")  #users/123
print(f"{endpoint}/1", "data")  #users/123

for i in range(3):
    x = uuid.uuid4().hex[:6]
    Email = f"{x}@gmail.com"
    print(Email)

