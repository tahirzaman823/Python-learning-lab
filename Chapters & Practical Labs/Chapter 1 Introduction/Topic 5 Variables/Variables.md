# Variables in Python

## Definition
A **variable** is a name you create to store a value in memory so it can be reused later in your program. Think of it like a labeled box — you give it a name and put something inside (a number, string, calculation, etc.), and you can open it, change its contents, or use it anywhere in your code.

## Important Points
- Variables are the **foundation for making code dynamic**.
- The `=` operator is used for **assignment** (assigning a value to a variable name).
- Python stores variable values in **memory** for quick access whenever needed.
- Once created, a variable can be **reused anywhere** in the code.
- A variable's value can be **updated** at any time using the same assignment syntax.
- **Python executes code line by line** — a variable only holds the value it was assigned *up to that point* in execution, not future updates.
- Variables prevent repetition — instead of manually changing a value everywhere, you change it **once** in the variable, and it updates everywhere it's used.
- To combine static text and variables in `print()`, separate them using a **comma** — Python automatically adds a space after each comma.

## Syntax
```python
variable_name = value        # creating & assigning a variable
variable_name = new_value    # updating a variable's value

print("static text", variable_name)   # mixing static text + variable
```

## Example
**Creating and using a variable:**
```python
x = 1
print(x)        # Output: 1

x = 2            # updating the value
print(x)        # Output: 2

y = x + 3         # using a variable in a calculation
print(y)         # Output: 5
```

**Without variables (repetitive & hard to maintain):**
```python
print("My name is Bar")
print("Bar is learning Python")
print("Bar wants to become Python expert")
```

**With variables (dynamic & easy to update):**
```python
name = "Bar"
language = "Python"

print("My name is", name)
print(name, "is learning", language)
print(name, "wants to become", language, "expert")
```

**Changing values updates everywhere automatically:**
```python
name = "Maria"
language = "JavaScript"
# Output automatically becomes:
# My name is Maria
# Maria is learning JavaScript
# Maria wants to become JavaScript expert
```