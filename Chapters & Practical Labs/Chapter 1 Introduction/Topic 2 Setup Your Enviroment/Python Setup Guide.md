# Python Setup Guide (From Video Transcript)

## 1. Installing Python

**Definition:**
Before writing any Python code, you need to install the Python engine (interpreter, standard libraries, built-in modules) on your PC by downloading it from the official website.

**Important Points:**
- Go to **python.org** → Downloads section → click the big yellow **Download Python** button.
- During installation, **check "Add python.exe to PATH"** — this is critical for smooth usage later.
- Click **Install Now** to complete setup.
- Verify installation by opening the terminal and typing:
  ```bash
  python --version
  ```
  If a version number is returned, Python is installed correctly.

---

## 2. Choosing a Code Editor vs IDE

**Definition:**
To write Python code, you need either a **Code Editor** (lightweight) or an **IDE** (Integrated Development Environment, heavier and more advanced).

**Important Points:**
- **Code Editor:** A "smart notepad" with syntax highlighting, autocomplete, file navigation, and extensions.
  - Examples: **Visual Studio Code**, Atom
- **IDE:** Includes debugger, compiler, version control, and more advanced tools.
  - Examples: **PyCharm**, Visual Studio *(not the same as VS Code)*
- **Recommended Choice:** Visual Studio Code — free, lightweight, and used by both beginners and professionals in real projects.

---

## 3. Installing Visual Studio Code

**Important Points:**
- Go to **code.visualstudio.com**
- Windows → click **Download for Windows**
- Mac → go to **Docs → Setup** section for the Mac installer
- Linux → available in the same Setup section
- Install it on your PC after downloading.

---

## 4. Setting Up VS Code for Python

**Important Points:**
- Open **Extensions** panel (left sidebar icon).
- Search for **Python** and install the official **Python extension by Microsoft**.
  - Provides smart suggestions, error highlighting, and easier code execution.
- Go to **File → Open Folder** and create a new folder (e.g., `Python_Learning`) to store all your Python files.

---

## 5. Writing & Running Your First Python Code

**Example:**
1. Create a new file and name it `hello.py` (the `.py` extension tells the system it's a Python file).
2. Write the following code:
   ```python
   print("Hi this is my first Python code")
   ```
3. Click the **Play (▶)** icon to run it.
4. Output appears in the terminal, confirming successful execution.

**Important Points:**
- `print()` is a function used to display output.
- The `.py` extension is mandatory for Python files.
- Successful output in the terminal = your PC understood and executed your instruction (this is what "programming" means).

---

## 6. Creating a Keyboard Shortcut to Run Code

**Definition:**
Instead of clicking the Play button every time, you can set up a custom shortcut to run Python files faster.

**Important Points:**
- Open Command Palette:
  - Windows: `Shift + Ctrl + P`
  - Mac: `Shift + Cmd + P`
- Search **"Preferences: Open Keyboard Shortcuts"**
- Search **"Run Python File"**
- Double-click on it and assign a shortcut (e.g., `Ctrl + R`)
- Now you can run code instantly using that shortcut instead of the Play button.

---

## 7. Bonus: Customizing VS Code (Themes & Icons)

**Definition:**
Optional visual upgrades to make VS Code look more professional and personalized — not required for coding.

**Important Points:**
- **Popular Themes** (installed via Extensions):
  - One Dark Pro
  - Iceberg (IO)
  - Monokai Pro *(paid)*
  - **Dracula** *(presenter's favorite, free)*
- **Material Icon Theme:** Adds colorful file/folder icons in the Explorer panel.

---

## 8. Auto-Formatting with PEP8

**Definition:**
PEP8 is the standard style guide for writing clean, readable, and professional Python code. The **autopep8** extension automatically formats your code to follow these rules.

**Important Points:**
- Install extension: **autopep8** (by Microsoft)
- To format a file manually:
  - Open Command Palette (`Shift + Ctrl + P`)
  - Search **"Format Document"**
  - Extra spaces and bad styling are automatically cleaned up.
- You can also set up a shortcut for formatting, similar to running code.

---

## 9. Bonus: Notion Roadmap Template

**Definition:**
A free Notion template (linked in the video description) to track and plan your Python learning progress.

**Important Points:**
- Organized into phases: **Beginner → Intermediate → Advanced**
- Includes a **course index** with chapters and lessons.
- Features a **Kanban-style board** (To Do / In Progress / Done).
- Includes a **timeline/calendar view** and **progress charts**.
- Helps visualize achievement and stay motivated while learning.