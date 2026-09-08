# Match-Case Statements in Python

## What is Match-Case?

- `match-case` is a feature introduced in **Python 3.10** for structural pattern matching.
- It simplifies complex conditional logic that would otherwise require long chains of `if`/`elif`/`else` statements.
- It's Python's version of the "switch" statement found in languages like C, Java, and JavaScript — but more powerful, since it can match on structure (types, sequences, objects), not just simple values.

## Syntax

```python
match value:
    case pattern1:
        # Code to execute if value matches pattern1
    case pattern2:
        # Code to execute if value matches pattern2
    case _:
        # Default case (if no patterns match)
```

- `value` is the expression being matched.
- Each `case` block defines a pattern to check against.
- `_` is the **wildcard pattern** — it matches anything and is typically used as a default/fallback case (like `else`).

## Basic Example

```python
status = 404

match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")
```

**Output:**
```
Not Found
```

## Matching Multiple Values

You can combine multiple patterns in a single `case` using `|` (the "or" pattern):

```python
day = "Sat"

match day:
    case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":
        print("Weekday")
    case "Sat" | "Sun":
        print("Weekend")
    case _:
        print("Invalid day")
```

**Output:**
```
Weekend
```

## Matching with Conditions (Guards)

You can add an `if` condition to a pattern using a **guard**:

```python
point = (5, 5)

match point:
    case (x, y) if x == y:
        print("Point is on the diagonal")
    case (x, y):
        print(f"Point at ({x}, {y})")
```

**Output:**
```
Point is on the diagonal
```

## Matching Data Structures

`match-case` can destructure sequences, tuples, and dictionaries directly.

```python
command = ["move", 10, 20]

match command:
    case ["move", x, y]:
        print(f"Moving to ({x}, {y})")
    case ["stop"]:
        print("Stopping")
    case _:
        print("Unknown command")
```

**Output:**
```
Moving to (10, 20)
```

## Matching Objects (Classes)

`match-case` also works with class instances, using their attributes:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(0, 0)

match point:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=0, y=y):
        print(f"On the Y axis at {y}")
    case Point(x=x, y=0):
        print(f"On the X axis at {x}")
    case Point():
        print("Somewhere else")
    case _:
        print("Not a point")
```

**Output:**
```
Origin
```

## Key Points to Remember

| Feature | Description |
|---|---|
| Introduced in | Python 3.10 |
| Wildcard | `_` matches anything (default case) |
| Multiple patterns | Use `\|` to combine values |
| Guards | Add `if condition` after a pattern |
| Destructuring | Works with lists, tuples, dicts, and objects |
| Order matters | Patterns are checked top to bottom; first match wins |

## When to Use It

- When you have many possible values/conditions to check against a single variable.
- When you need to destructure structured data (tuples, lists, objects) while checking conditions.
- When it would improve readability over a long `if`/`elif` chain.