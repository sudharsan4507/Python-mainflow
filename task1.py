
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TASK 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CODE 1 : The sum of Two Numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum of 7 and 3 is 10\n"
     ]
    }
   ],
   "source": [
    "def sum(a,b):\n",
    "    return a+b\n",
    "\n",
    "a = 7\n",
    "b = 3\n",
    "print(f\"Sum of {a} and {b} is {sum(a,b)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CODE 2 : Odd or Even"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number  16 is EVEN\n"
     ]
    }
   ],
   "source": [
    "def odd_or_even(a):\n",
    "    return \"EVEN\" if a%2==0 else \"ODD\"\n",
    "\n",
    "a = 16\n",
    "print(f\"Number  {a} is {odd_or_even(a)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CODE 3 : Factorial Calculation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of 5 is 120\n"
     ]
    }
   ],
   "source": [
    "def factorial(n):\n",
    "    result = 1\n",
    "    for i in range(1, n + 1):\n",
    "        result *= i\n",
    "    return result\n",
    "\n",
    "# Input from user\n",
    "num = 5\n",
    "\n",
    "# Check if input is valid\n",
    "if num < 0:\n",
    "    print(\"Factorial is not defined for negative numbers.\")\n",
    "else:\n",
    "    print(f\"Factorial of {num} is {factorial(num)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CODE 4 : Fibonacci Sequence"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n"
     ]
    }
   ],
   "source": [
    "def fibonacci(n):\n",
    "    sequence = [0, 1]\n",
    "    for i in range(2, n):\n",
    "        sequence.append(sequence[-1] + sequence[-2])\n",
    "    return sequence[:n]\n",
    "\n",
    "# Example: Generate first 10 Fibonacci numbers\n",
    "n = 10\n",
    "print(fibonacci(n))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CODE 5 - Reverse a String"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original String: Hello, World!\n",
      "Reversed String: !dlroW ,olleH\n"
     ]
    }
   ],
   "source": [
    "def reverse_string(s):\n",
    "    return s[::-1]\n",
    "\n",
    "# Example usage\n",
    "input_string = \"Hello, World!\"\n",
    "reversed_string = reverse_string(input_string)\n",
    "print(\"Original String:\", input_string)\n",
    "print(\"Reversed String:\", reversed_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CODE 6 - Palindrome Check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Palindrome!\n"
     ]
    }
   ],
   "source": [
    "def is_palindrome(s):\n",
    "    # Removing non-alphanumeric characters and converting to lowercase\n",
    "    s = ''.join(filter(str.isalnum, s)).lower()\n",
    "    return s == s[::-1]\n",
    "\n",
    "# Example usage\n",
    "word = input(\"Enter a word or phrase: \")\n",
    "if is_palindrome(word):\n",
    "    print(\"Palindrome!\")\n",
    "else:\n",
    "    print(\"Not a palindrome.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CODE 7 - Leap Year Check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True - It's a leap year!\n"
     ]
    }
   ],
   "source": [
    "def is_leap_year(year):\n",
    "    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\n",
    "\n",
    "# Example usage\n",
    "year = 2056\n",
    "if is_leap_year(year):\n",
    "    print(\"True - It's a leap year!\")\n",
    "else:\n",
    "    print(\"False - Not a leap year.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "CODE 8 - Armstrong Number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False - Not an Armstrong number.\n"
     ]
    }
   ],
   "source": [
    "def is_armstrong_number(n):\n",
    "    total = 0\n",
    "    temp = n\n",
    "    num_digits = len(str(n))\n",
    "    while temp > 0:\n",
    "        digit = temp % 10\n",
    "        total += digit ** num_digits\n",
    "        temp //= 10\n",
    "    return total == n\n",
    "\n",
    "# Example usage\n",
    "num = 16\n",
    "if is_armstrong_number(num):\n",
    "    print(\"True - It's an Armstrong number!\")\n",
    "else:\n",
    "    print(\"False - Not an Armstrong number.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
