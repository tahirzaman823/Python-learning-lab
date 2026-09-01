#Q1
#Write a program that prints: Hello, World! Welcome to Python.
print("Hello, World! Welcome to Python")

#Q2
#Write a program that prints the following poem using a single print() statement:
'''Twinkle, twinkle, little star,
How I wonder what you are!'''

print('''Twinkle, twinkle, little star,
How I wonder what you are!''')


#Q3
'''
Create variables to store:

Your name (string)
Your age (integer)
Your height in meters (float)
A boolean value representing whether you are a student
Print all of them in one line.'''

name = 'Tahir'
age =  23
height = 5.4
Student = True

print("\n","Name:",name,"\n","Age:",age,"\n","Height:",height,"\n","Student:",Student)

#Q4
'''You are given a string:

num = "45"
Convert it into an integer
Add 10 to it
Print the result'''

num = "45"
print(type(num))
num_int = int(num)

addition = num_int + 10
print(addition)



#Q5
'''Write a program that:

Asks the user for their favorite food.
Prints:
Wow! I also like <food>. '''

userFood = str(input("Type Your Favorite Food:"))
print("Wow! I also like",userFood)

#Q6
'''Takes two numbers as input from the user.
Prints their:
Sum
Difference
Product
Quotient'''

num1 = int(input("Entre Any number:"))
num2 = int(input("Entre another number:"))

sum = num1 + num2
print("sum of num1 and num2 is:",sum)

Difference = num1 - num2
print("Difference of num1 and num2 is:",Difference)

Product = num1 * num2
print("Product of num1 and num2 is :",Product)

Quotient = num1 / num2
print("Quotient of num1 and num2 is:",Quotient)

#Q7 
'''Print the following output using escape sequences:

Hello "Python" World!
This is on a new line.
This is a tab →	    after tab.'''

print('''
Hello "Python" World!
This is on a new line.
This is a tab →	    after tab. ''')


#Q8
'''Write a program that:

Takes an integer as input from the user.
Prints the square and cube of that number.'''

usernumber = int(input("entre any number"))
print("square of number is:",usernumber**2)
print("Cube of number is:",usernumber**3)