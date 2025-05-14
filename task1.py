# Task 1: The Sum of Two Numbers
def sum_of_two_numbers(a, b):
    return a + b

# Example usage for Task 1
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
result = sum_of_two_numbers(num1, num2)
print("The sum of the two numbers is:", result)


# Task 2: Odd or Even
def odd_or_even(number):
    return "Even" if number % 2 == 0 else "Odd"

# Example usage for Task 2
num = int(input("Enter an integer: "))
result = odd_or_even(num)
print(f"The number is: {result}")


# Task 3: Factorial Calculation
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage for Task 3
num = int(input("Enter a non-negative integer: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")


# Task 4: Fibonacci Sequence
def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage for Task 4
num = int(input("Enter the number of Fibonacci numbers to generate: "))
result = fibonacci_sequence(num)
print(f"The first {num} Fibonacci numbers are: {result}")


# Task 5: Reverse a String
def reverse_string(s):
    return s[::-1]

# Example usage for Task 5
input_string = input("Enter a string to reverse: ")
result = reverse_string(input_string)
print("The reversed string is:", result)


# Task 6: Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

# Example usage for Task 6
input_string = input("Enter a string to check if it's a palindrome: ")
result = is_palindrome(input_string)
print("Is the string a palindrome?", result)


# Task 7: Leap Year Check
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage for Task 7
year = int(input("Enter a year to check if it's a leap year: "))
result = is_leap_year(year)
print("Is the year a leap year?", result)


# Task 8: Armstrong Number
def is_armstrong_number(n):
    digits = str(n)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == n

# Example usage for Task 8
num = int(input("Enter a number to check if it's an Armstrong number: "))
result = is_armstrong_number(num)
print("Is the number an Armstrong number?", result)
