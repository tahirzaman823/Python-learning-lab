# Q1: Basic String Operations

name = "Tahir Zaman"
print(name[0])     # Output: T
print(name[-1])    # Output: n
print(len(name))   # Output: 11

# Q2: String Slicing and Indexing
text = "Python Programming"
print(text[0:6])   # Output: Python
print(text[-6:])    # Output: amming
print(text[::2])    # Output: Pto rgamn

# Q3: String Methods and Functions
messy = "  i love python programming  "

stripped = messy.strip()          # Remove extra spaces from both ends
title_case = stripped.title()     # Convert to title case
o_count = stripped.count("o")     # Count occurrences of "o"

print(stripped)      # Output: i love python programming
print(title_case)    # Output: I Love Python Programming
print(o_count)        # Output: 3

# Check if "123abc" is alphanumeric
check_str = "123abc"
print(check_str.isalnum())   # Output: True

# Q4: String Formatting and f-Strings
Name = "John"
Age = 25
print("My name is {} and i am {} year old.".format(Name, Age))
# Output: My name is John and i am 25 year old.

# Q5: String Manipulation Challenges
sentence = "Coding in Python is fun"

# 5.1 Replace "fun" with "awesome"
new_sentence = sentence.replace("fun", "awesome")
print(new_sentence)   # Output: Coding in Python is awesome

# 5.2 Find the index of "Python"
python_index = sentence.find("Python")
print(python_index)   # Output: 10

# 5.3 Convert to uppercase
upper_sentence = sentence.upper()
print(upper_sentence)   # Output: CODING IN PYTHON IS FUN


# Q6: Bonus Questions
# 6.1 Count vowels in a given string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

test_string = "Coding in Python is fun"
print(count_vowels(test_string))   # Output: 6


# 6.2 Palindrome checker using user input
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")   # ignore case and spaces
    return cleaned == cleaned[::-1]

user_string = input("Enter a string to check if it's a palindrome: ")
print(is_palindrome(user_string))