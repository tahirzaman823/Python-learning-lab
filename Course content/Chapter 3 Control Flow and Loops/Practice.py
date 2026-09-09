"""
Python Practice Program
========================
Covers:
1. If-Else Conditional Statements
2. Match-Case Statements
3. For Loops
4. While Loops
5. Break, Continue, and Pass Statements

Each section is organized into its own function so the program
runs in a clean, structured, menu-driven way.
"""


# ------------------------------------------------------------------
# 1. IF-ELSE CONDITIONAL STATEMENTS
# ------------------------------------------------------------------

def check_positive_negative_zero():
    """Ask the user for a number and print whether it is positive, negative, or zero."""
    num = float(input("Enter a number: "))
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print(f"{num} is Zero")


def check_voting_eligibility():
    """Check if a person is eligible to vote (age >= 18)."""
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are NOT eligible to vote.")


def check_even_odd():
    """Take a number from the user and print 'Even' or 'Odd'."""
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


def run_if_else_section():
    print("\n--- 1. If-Else Conditional Statements ---")
    print("\n[1.1] Positive / Negative / Zero Checker")
    check_positive_negative_zero()

    print("\n[1.2] Voting Eligibility Checker")
    check_voting_eligibility()

    print("\n[1.3] Even / Odd Checker")
    check_even_odd()


# ------------------------------------------------------------------
# 2. MATCH-CASE STATEMENTS
# ------------------------------------------------------------------

def day_of_week():
    """Ask for a day number (1-7) and print the corresponding day using match-case."""
    day_num = int(input("Enter a day number (1-7): "))

    match day_num:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid day number. Please enter a number between 1 and 7.")


def simple_calculator():
    """Simulate a simple calculator using match-case."""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    match operation:
        case "+":
            print(f"Result: {num1 + num2}")
        case "-":
            print(f"Result: {num1 - num2}")
        case "*":
            print(f"Result: {num1 * num2}")
        case "/":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please use +, -, *, or /.")


def run_match_case_section():
    print("\n--- 2. Match-Case Statements ---")
    print("\n[2.1] Day of the Week")
    day_of_week()

    print("\n[2.2] Simple Calculator")
    simple_calculator()


# ------------------------------------------------------------------
# 3. FOR LOOPS
# ------------------------------------------------------------------

def print_numbers_1_to_10():
    """Print numbers from 1 to 10 using a for loop."""
    for i in range(1, 11):
        print(i, end=" ")
    print()


def multiplication_table():
    """Print the multiplication table of a number entered by the user."""
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


def sum_1_to_100():
    """Calculate the sum of all numbers from 1 to 100 using a for loop."""
    total = 0
    for i in range(1, 101):
        total += i
    print(f"Sum of numbers from 1 to 100 = {total}")


def print_star_pattern():
    """Print a star pattern using a for loop."""
    rows = 4
    for i in range(1, rows + 1):
        print("*" * i)


def run_for_loop_section():
    print("\n--- 3. For Loops ---")
    print("\n[3.1] Numbers 1 to 10")
    print_numbers_1_to_10()

    print("\n[3.2] Multiplication Table")
    multiplication_table()

    print("\n[3.3] Sum of 1 to 100")
    sum_1_to_100()

    print("\n[3.4] Star Pattern")
    print_star_pattern()


# ------------------------------------------------------------------
# 4. WHILE LOOPS
# ------------------------------------------------------------------

def print_numbers_while():
    """Print numbers from 1 to 10 using a while loop."""
    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1
    print()


def password_check():
    """Keep asking the user to enter a password until they enter the correct one."""
    correct_password = "python123"
    password = input("Enter password: ")
    while password != correct_password:
        print("Incorrect password. Try again.")
        password = input("Enter password: ")
    print("Access Granted!")


def reverse_number():
    """Use a while loop to reverse a given number."""
    num = int(input("Enter a number to reverse: "))
    original_num = num
    reversed_num = 0

    # Handle negative numbers
    is_negative = num < 0
    if is_negative:
        num = -num

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    if is_negative:
        reversed_num = -reversed_num

    print(f"{original_num} reversed is {reversed_num}")


def run_while_loop_section():
    print("\n--- 4. While Loops ---")
    print("\n[4.1] Numbers 1 to 10")
    print_numbers_while()

    print("\n[4.2] Password Checker")
    password_check()

    print("\n[4.3] Reverse a Number")
    reverse_number()


# ------------------------------------------------------------------
# 5. BREAK, CONTINUE, AND PASS STATEMENTS
# ------------------------------------------------------------------

def break_example():
    """Print numbers 1 to 10, but stop the loop if the number is 7."""
    for i in range(1, 11):
        if i == 7:
            break
        print(i, end=" ")
    print()


def continue_example():
    """Print numbers 1 to 10, skipping the number 5."""
    for i in range(1, 11):
        if i == 5:
            continue
        print(i, end=" ")
    print()


def pass_example():
    """Go through numbers 1 to 5, but do nothing for number 3."""
    for i in range(1, 6):
        if i == 3:
            pass  # placeholder - do nothing for number 3
        else:
            print(i, end=" ")
    print()


def run_break_continue_pass_section():
    print("\n--- 5. Break, Continue, and Pass Statements ---")
    print("\n[5.1] Break Example (stop at 7)")
    break_example()

    print("\n[5.2] Continue Example (skip 5)")
    continue_example()

    print("\n[5.3] Pass Example (do nothing for 3)")
    pass_example()


# ------------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------------

def main():
    sections = {
        "1": ("If-Else Conditional Statements", run_if_else_section),
        "2": ("Match-Case Statements", run_match_case_section),
        "3": ("For Loops", run_for_loop_section),
        "4": ("While Loops", run_while_loop_section),
        "5": ("Break, Continue, and Pass Statements", run_break_continue_pass_section),
        "6": ("Run All Sections", None),
    }

    print("=" * 50)
    print("        PYTHON PRACTICE PROGRAM MENU")
    print("=" * 50)
    for key, (name, _) in sections.items():
        print(f"{key}. {name}")
    print("0. Exit")
    print("=" * 50)

    choice = input("Enter your choice: ").strip()

    if choice == "0":
        print("Goodbye!")
        return
    elif choice == "6":
        run_if_else_section()
        run_match_case_section()
        run_for_loop_section()
        run_while_loop_section()
        run_break_continue_pass_section()
    elif choice in sections:
        sections[choice][1]()
    else:
        print("Invalid choice. Please run the program again and select a valid option.")


if __name__ == "__main__":
    main()