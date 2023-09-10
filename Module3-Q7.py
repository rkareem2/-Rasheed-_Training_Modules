""" This python code calculates the average of four input numbers by adding them together and dividing the sum 
   by 4. The result is then stored in the average variable. The result is going to be in a float type"""

if __name__ == "__main__":# we statrt by checking if the python code is being run as the main program or just an imported program
    num1 = float(input("Enter the first number: "))#we use the input() function to accept users input for num1-num4 and we convert the input to a float
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))

    #we find the average of all numbers by adding and dividing by 4
    average = (num1 + num2 + num3 + num4) / 4
    #we display our average using the print() function
    print(f"The average of {num1}, {num2}, {num3}, and {num4} is: {average:.2f}")