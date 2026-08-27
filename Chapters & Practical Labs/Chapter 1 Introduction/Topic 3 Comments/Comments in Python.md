# Comments in Python

## Definition
A comment is a line of text in your code that Python completely ignores during execution. It exists only to help humans understand what the code is doing — it has no effect on the logic or output of the program.

## Important Points
- Comments start with the **hash symbol** `#`.
- Python skips everything after `#` on that line — it does not affect execution.
- Comments make code **understandable, readable, professional, and easy to maintain** — especially useful when you (or your team) revisit the code later.
- **Types of comments:**
  - **Single-line comment:** One line starting with `#`.
  - **Multi-line comment:** Multiple consecutive lines, each starting with `#`, used to explain complex logic step-by-step.
- **Placement styles:**
  - **Above the code:** Used for longer, detailed explanations.
  - **Inline (end of code line):** Used for short, quick explanations or labels.
- Only the text after `#` is ignored — if code exists before it on the same line, that code still runs normally.

## Syntax
```
# This is a single-line comment

# This is a
# multi-line comment
# explaining multiple steps
```

**Comment above code (detailed style):**
```python
# store the final exam score
x = 10
```

**Inline comment (short style):**
```python
x = 9  # final exam score
```

## Example
**Without comments (hard to understand):**
```python
data = load_data()
filtered = [d for d in data if d.month == 5 and d.region == "US"]
revenue = sum(d.amount for d in filtered)
total = revenue * 1.1
print(total)
```

**With comments (clear and professional):**
```python
# Load the data
data = load_data()

# Filter data based on month and region
filtered = [d for d in data if d.month == 5 and d.region == "US"]

# Compute the revenue
revenue = sum(d.amount for d in filtered)

# Find the total revenue and display it
total = revenue * 1.1
print(total)
```