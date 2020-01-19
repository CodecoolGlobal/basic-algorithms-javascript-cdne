"""
Write a program that prints the numbers from 1 to 100. But:
 - for multiples of three print “Fizz” instead of the number and
 - for the multiples of five print “Buzz”.
 - For numbers which are multiples of both three and five print “FizzBuzz”.
"""


def fizz_buzz(number):
    for x in range(number):
        if x % 3 == 0:
            print("Fizz", x)
        if x % 5 == 0:
            print("Buzz", x)
        else:
            print("FizzBuzz")


fizz_buzz(101)
