#TASK 2 

# Task 9: Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime: "))
print("Is the number prime?", is_prime(num))


# Task 10: Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

num = int(input("Enter an integer to find the sum of its digits: "))
print("The sum of the digits is:", sum_of_digits(num))


# Task 11: LCM and GCD
import math

def lcm_and_gcd(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm, gcd

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
lcm, gcd = lcm_and_gcd(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")
print(f"The GCD of {num1} and {num2} is: {gcd}")


# Task 12: List Reversal
def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst

input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
print("The reversed list is:", reverse_list(input_list))


# Task 13: Sort a List
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
print("The sorted list is:", bubble_sort(input_list))


# Task 14: Remove Duplicates
def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
print("The list with unique elements is:", remove_duplicates(input_list))


# Task 15: String Length
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

input_string = input("Enter a string to find its length: ")
print("The length of the string is:", string_length(input_string))


# Task 16: Count Vowels and Consonants
def count_vowels_and_consonants(s):
    vowels = set('aeiouAEIOU')
    vowel_count, consonant_count = 0, 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

input_string = input("Enter a string to count vowels and consonants: ")
vowels, consonants = count_vowels_and_consonants(input_string)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
