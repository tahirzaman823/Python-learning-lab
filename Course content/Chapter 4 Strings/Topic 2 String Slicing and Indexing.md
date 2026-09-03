# String Slicing and Indexing

## Introduction

In Python, strings are sequences of characters, and each character has an index. You can access individual characters using indexing and extract substrings using slicing.

---

## String Indexing

Each character in a string has a unique index, starting from 0 for the first character and -1 for the last character.

```python
text = "Python"
print(text[0])   # Output: P
print(text[1])   # Output: y
print(text[-1])  # Output: n (last character)
print(text[-2])  # Output: o
```

---

## String Slicing

Slicing allows you to extract a portion of a string using the syntax `string[start:stop:step]`.

```python
text = "Hello, Python!"
print(text[0:5])    # Output: Hello
print(text[:5])      # Output: Hello (same as text[0:5])
print(text[7:])      # Output: Python! (from index 7 to end)
print(text[::2])     # Output: Hlo Pto!
print(text[-6:-1])   # Output: ython (negative indexing)
```

---

## Step Parameter

The `step` parameter defines the interval of slicing.

```python
text = "Python Programming"
print(text[::2])    # Output: Pto rgamn
print(text[::-1])   # Output: gnimmargorP nohtyP (reverses string)
```

---

## Practical Uses of Slicing

String slicing is useful in many scenarios:

- Extracting substrings
- Reversing strings
- Removing characters
- Manipulating text efficiently

```python
text = "Welcome to Python!"
print(text[:7])     # Output: Welcome
print(text[-7:])    # Output: Python!
print(text[3:-3])   # Output: come to Pyt
```

---

## Summary

- Indexing allows accessing individual characters.
- Positive indexing starts from 0, negative indexing starts from -1.
- Slicing helps extract portions of a string.
- The step parameter defines the interval for selection.
- Using `[::-1]` reverses a string. 