# While Loops in Python

## What are While Loops?

- `while` loops execute a block of code repeatedly as long as a condition is `True`.
- They're useful when the number of iterations isn't known in advance (unlike `for` loops, which iterate over a fixed sequence).

## Syntax

```python
while condition:
    # Code to execute while condition is True
```

- `condition` is checked before each iteration.
- As soon as `condition` evaluates to `False`, the loop stops.

## Basic Example

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

**Output:**
```
0
1
2
3
4
```

> **Note:** It's important to update the variable used in the condition (`count += 1` here) — otherwise the condition never becomes `False` and the loop runs forever.

## Infinite Loops

- Be careful to avoid infinite loops by ensuring the condition eventually becomes `False`.
- Example of an infinite loop:

```python
while True:
    print("This will run forever!")
```

- Infinite loops aren't always a mistake — they're often used intentionally with a `break` statement to exit under a specific condition (e.g., a game loop, a server listening for requests).

## `break` and `continue`

- `break` exits the loop immediately, regardless of the condition.
- `continue` skips the rest of the current iteration and re-checks the condition.

```python
count = 0

while True:
    if count == 5:
        break
    print(count)
    count += 1
```

**Output:**
```
0
1
2
3
4
```

```python
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
```

**Output:**
```
1
2
4
5
```

## `else` Clause on a While Loop

Like `for` loops, `while` loops support an optional `else` block that runs only if the loop finishes **without** hitting a `break`:

```python
count = 0

while count < 3:
    print(count)
    count += 1
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

## Common Use Case: Input Validation

`while` loops are often used to repeatedly prompt for input until it's valid:

```python
user_input = ""

while user_input != "quit":
    user_input = input("Type 'quit' to exit: ")

print("Goodbye!")
```

## `while` vs `for`

| | `for` loop | `while` loop |
|---|---|---|
| Best for | Iterating over a known sequence | Repeating until a condition changes |
| Iterations known ahead of time? | Usually yes | Usually no |
| Risk of infinite loop | Low | Higher (must manage condition manually) |

## Key Points to Remember

| Feature | Description |
|---|---|
| Runs while | Condition is `True` |
| Condition checked | Before each iteration |
| Must update | Something that affects the condition, to avoid an infinite loop |
| `break` | Exits the loop early |
| `continue` | Skips to the next condition check |
| `else` | Runs if the loop completes without `break` |