# How Python Works?

## Definition
Python converts human-readable source code (`.py`) into intermediate byte code (`.pyc`), which is then executed by the Python Virtual Machine (PVM) into machine code (1s and 0s) that your computer hardware understands.

## Important Points
- **Compiler Phase:** Automatically compiles `.py` source code into intermediate bytecode (`.pyc`).
- **Linking Libraries:** Integrates pre-written code modules (like file handlers or math functions) with the bytecode.
- **Python Virtual Machine (PVM):** The software engine that reads bytecode and runs it on the actual CPU.
- **The Interpreter:** The overarching "toolbox" combining the compiler, linker, and PVM behind the scenes.

## Syntax (Conceptual Workflow)
$$\text{Source Code (.py)} \longrightarrow \text{Compiler} \longrightarrow \text{Byte Code (.pyc)} \longrightarrow \text{PVM + Libraries} \longrightarrow \text{Machine Code (0s/1s)}$$

## Example
```python
# Save this in a file named `app.py`
import math

print(math.sqrt(16))  # Compiled to bytecode, linked with `math`, executed by PVM
```

---