# Break, Continue, and Pass Statements

## Break

- The `break` statement is used to exit a loop prematurely — it stops the loop entirely, even if the original condition or sequence hasn't been exhausted.

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0, 1, 2, 3, 4
```

**Output:**
```
0
1
2
3
4
```

- `break` only exits the **innermost** loop it's in. If you have nested loops, an outer loop keeps running.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

**Output:**
```
0 0
1 0
2 0
```

## Continue

- The `continue` statement skips the rest of the code in the current iteration and moves on to the next iteration — it does **not** stop the loop.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0, 1, 3, 4
```

**Output:**
```
0
1
3
4
```

## Pass

- The `pass` statement is a placeholder that does nothing. It's used when Python's syntax requires a statement (e.g., a non-empty block) but no action is actually needed yet.

```python
for i in range(5):
    if i == 3:
        pass  # Do nothing
    print(i)  # Output: 0, 1, 2, 3, 4
```

**Output:**
```
0
1
2
3
4
```

- Common uses for `pass`:
  - Stubbing out a function or class body while still writing/planning it:
    ```python
    def my_function():
        pass  # TODO: implement later
    ```
  - Keeping an empty `if`/`else`, loop, or exception handler syntactically valid.

## `break` vs `continue` vs `pass`

| Statement | Effect |
|---|---|
| `break` | Exits the loop immediately |
| `continue` | Skips the current iteration, moves to the next one |
| `pass` | Does nothing — just a syntactic placeholder |

## Summary

- Use `if`, `elif`, and `else` for decision-making.
- Use `match-case` for pattern matching (Python 3.10+).
- Use `for` loops to iterate over sequences and `while` loops for repeated execution based on a condition.
- Control loop execution with `break`, `continue`, and `pass`.