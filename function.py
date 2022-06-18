def add_numbers(num1,num2):
    sum = num1 + num2
    return sum

def multiply_numbers(n1, n2):
    multiply = n1 * n2
    return multiply

def divide_num(number1, number2):
    divide = number1 / number2
    return divide

num1 = 5
num2 = 6
sum= add_numbers(num1,num2)

num1 = int(input("enter first number"))
num1 = int(input("enter sexond number"))
multiply = (num1 + num2)
multiply = multiply_numbers(num1, num2)

number1 =  10
number2 = 5
num = divide_num(number1,number2)

print("sum of two numbers is: ",sum)
print("multiplication of two numbers is: ",multiply)
print("division of two numbers is: ",num)