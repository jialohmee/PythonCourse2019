## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

import time

## Problem 2
## Write a function using recursion that returns prime numbers less than 121


def find_primes(me = 2):
	numbers = list(range(2, me+1))
	for number in range(2, me+1):
		for divisor in range(2, number):
			if number % divisor == 0 and number != divisor:
				try:
					numbers.remove(number)
				except:
					pass
	return numbers
	#return numbers

print(find_primes(2000))

def gcd(x, y):
	if x <= y:
		primes = find_primes(y)
	else:
		primes = find_primes(x)
	factor = 1
	for divisor in primes:
		count = 0
		while x % divisor == 0 and y % divisor == 0:
			x = x / divisor
			y = y / divisor
			count += 1
		factor = factor * divisor**count
	return factor


gcd(20,24)
 
## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html

#number = 18
#def is_prime(number):
