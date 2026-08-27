# The print() Function in Python

## Definition
`print` is a **built-in Python function** that displays text or a result on the output screen, used to communicate messages, results, or progress to the user.

## Important Points
- `print` is one of the most frequently used functions in Python — used from beginner to advanced levels.
- A **function** takes an input, processes it internally, and returns an output (like a mini machine — e.g., a coffee machine takes beans + water and gives coffee).
- **Three sources of functions:**
  - **Built-in functions:** Come with Python by default (e.g., `print`, `input`, `len`, `max`).
  - **Third-party functions:** From external libraries (e.g., pandas, numpy, plotly) — must be installed separately.
  - **User-defined functions:** Functions created by the programmer.
- Real-world use cases of `print`:
  - Displaying messages/results to users.
  - **Debugging/testing** — printing intermediate values (like subtotals) to verify calculations are correct.

## Syntax
```python
print("message")
```

## Example
```python
print("Hi Python")
```

---

# Quotes in print()

## Definition
Python allows using either **single quotes** or **double quotes** for strings, as long as the same type is used at the start and end.

## Important Points
- `"text"` and `'text'` both work.
- Mixing quote types (e.g., start with `"` and end with `'`) causes a **syntax error**.

## Example
```python
print("Hi Python")   # valid
print('Hi Python')   # valid
print("Hi Python')   # invalid - SyntaxError
```

---

# Escape Sequences (Backslash `\`)

## Definition
Escape sequences are special character combinations starting with a **backslash (`\`)** that tell Python to perform a special action instead of treating the character as normal text.

## Important Points
- `\"` → Insert a double quote inside a double-quoted string.
- `\'` → Insert a single quote inside a single-quoted string.
- `\\` → Insert a real backslash.
- `\n` → Create a new line.
- `\t` → Insert a horizontal tab (space).
- Escape characters allow full control over formatting inside a **single** `print()` statement.

## Syntax
```
\"   → escaped double quote
\'   → escaped single quote
\\   → escaped backslash
\n   → new line
\t   → tab space
```

## Example
```python
# Double quotes inside a double-quoted string
print("Hi \"Python\"")     # Output: Hi "Python"

# Single quotes inside a single-quoted string
print('Hi \'Python\'')     # Output: Hi 'Python'

# Real backslash in output (path example)
print("C:\\Users\\bar")    # Output: C:\Users\bar

# New line
print("Message 1\nMessage 2")
# Output:
# Message 1
# Message 2

# Tab space
print("Message 1\tMessage 2")
# Output: Message 1    Message 2
```

---

# Multi-line Output with Triple Quotes

## Definition
Triple quotes (`"""` or `'''`) let you write a **multi-line string** directly in your code across several lines, without needing `\n` for every line break — all within a **single** `print()` call.

## Important Points
- Start and end the string with `"""`.
- Pressing Enter inside triple quotes automatically creates a new line in the output.
- Removes the need to manually add `\n` for each line.

## Syntax
```python
print("""
line 1
line 2
line 3
""")
```

## Example
```python
print("""Your learning path:
    - Python basics
    - Data engineering
    - AI""")
```

**Output:**
```
Your learning path:
    - Python basics
    - Data engineering
    - AI
```