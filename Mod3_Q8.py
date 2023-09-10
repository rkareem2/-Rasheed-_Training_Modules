"""This code helps us identify Odd and even numbers by using the Modulo operator which is an operator 
   that shows the remainder of any arithmetic. if a numer is even and its divided by two it has no remainder
    but an odd number would have a remainder greater than 0. In this solution I used that logic to arrive at
     a solution """

# I defined a funtion that takes two numbers


def Odd_Even(num1, num2):
    sum = num1 + num2  # I sum up the two numbers and the resullt is Sum
    # I used the if and else statement to perform some logical arithmetic
    if sum % 2 > 0:
        print("sum is an odd number ")
    else:
        print("Sum is an even number")


# called the function multiple times with different numbers
Odd_Even(2, 3)
Odd_Even(2, 4)
Odd_Even(11, 4)
