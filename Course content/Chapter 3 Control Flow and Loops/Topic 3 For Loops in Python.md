# For Loops in Python

## What are For Loops?

- `for` loops are used to iterate over a sequence (e.g., list, tuple, string, dictionary, range).
- They execute a block of code once for each item in the sequence.

## Syntax

```python
for item in sequence:
    # Code to execute for each item
```

- `item` is a variable that takes on the value of each element in `sequence`, one at a time.
- `sequence` is any iterable (list, string, range, tuple, dict, set, etc.).

## Basic Example

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

## Using `range()`

- The `range()` function generates a sequence of numbers, commonly used to repeat an action a set number of times.
- `range(stop)` — starts at 0, goes up to (but not including) `stop`.
- `range(start, stop)` — starts at `start`, goes up to (but not including) `stop`.
- `range(start, stop, step)` — increments by `step` each time.

```python
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
```

```python
for i in range(2, 10, 2):
    print(i)  # Output: 2, 4, 6, 8
```

## Looping Over a String

Strings are iterable too — looping over one yields each character:

```python
for letter in "cat":
    print(letter)
```

**Output:**
```
c
a
t
```

## Looping with Index using `enumerate()`

Use `enumerate()` when you need both the index and the value:

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

**Output:**
```
0 apple
1 banana
2 cherry
```

## Looping Over a Dictionary

By default, looping over a dict gives you its keys. Use `.items()` to get key-value pairs:

```python
person = {"name": "Alex", "age": 30}

for key, value in person.items():
    print(key, ":", value)
```

**Output:**
```
name : Alex
age : 30
```

## `break` and `continue`

- `break` exits the loop entirely.
- `continue` skips to the next iteration.

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0, 1, 2, 3, 4
```

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0, 1, 3, 4
```

## `else` Clause on a For Loop

Python `for` loops support an optional `else` block, which runs only if the loop completes **without** hitting a `break`:

```python
for i in range(3):
    print(i)
else:
    print("Loop finished without break")
```

**Output:**
```
0
1
2
Loop finished without break
```

## Nested For Loops

Loops can be nested inside one another — useful for grids, matrices, or combinations:

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

**Output:**
```
0 0
0 1
0 2
1 0
1 1
1 2
```

## Key Points to Remember

| Feature | Description |
|---|---|
| Iterates over | Lists, strings, tuples, dicts, sets, ranges |
| `range()` | Generates a number sequence to loop over |
| `enumerate()` | Gives index + value together |
| `.items()` | Loops over dict key-value pairs |
| `break` | Exits the loop early |
| `continue` | Skips to the next iteration |
| `else` | Runs if the loop completes without `break` |