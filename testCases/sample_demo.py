
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

