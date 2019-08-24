import numpy as np
np.random.seed(453286) # seed random number generator
import time
import matplotlib.pyplot as plt
import math

## COUNTING SORT ##

def counting_sort(numbers):
	# suppose we have an array [7, 8, 4, 5, 7]
	sorted_numbers = [0] * len(numbers) # create a list of zeroes to store the sorted list
	count = [0] * len(range(max(numbers)-min(numbers)+1))
	# create a list of counts, length equals the max - min+1 e.g. min = 4, max = 8. e.g. counts => 0, 0, 0, 0, 0
	# each count corresponds to the number of times a number appears in the list e.g. numbers	=> 4, 5, 6, 7, 8
	sum_count = [count[0]]
	for i in numbers:
		count[i-min(numbers)] += 1 
		# for each number appearing in the array, its corresponding count in the count list
		# e.g. if min equals 4 and i is 4, then count[0] += 1
		# counts	==> 1, 0, 0, 0, 0
		# numbers 	==> 4, 5, 6, 7, 8
	for i in range(1, len(count)):
		sum_count.append(count[i] + sum_count[i-1])
		# if counts 		==> 1, 1, 0, 2, 1
		# then sum_counts 	==> 1, 2, 2, 4, 5
		# numbers 			==> 4, 5, 6, 7, 8
	for i in numbers:
		sorted_numbers[sum_count[i-min(numbers)]] = i
		sum_count[i-min(numbers)] -= 1
		# now we match the sum_counts to the position of the number
		# e.g. 4 goes to the first position, 8 goes to the fifth position, so on
		# once a number has been matched to its position, reduce its sum_count by 1
	return sorted_numbers

numbers = np.random.randint(0, 10, 10) # randomly pick ten numbers from 0 and 9
counting_sort(numbers) # test

## SHELL SORT ##

def shell_sort(numbers):
	gap = len(numbers)//2
	# specify a gap between a pair of numbers in the array (denote A, B)
	while gap > 0:
		for i in range(gap, len(numbers)):
			# we can think of i as the right hand side of the pair => B
			number = numbers[i]
			# store B temporarily
			j = i
			while j >= gap and numbers[j-gap] > number:
				# numbers[j-gap] corresponds to the left hand side of the pair (i.e. A)
				# so we're comparing whether A > B
				numbers[j] = numbers[j-gap]
				# if A > B, then replace B with A in the array
				j -= gap
				# return back to second while loop
			numbers[j] = number
			# replace B back to left hand side of the pair (i.e. where A was originally located)
		gap = gap // 2
		# divide gap between two after for loop is completed
	return numbers

numbers = np.random.randint(0, 10, 10) 
shell_sort(numbers) # test

average_times_counting_sort = []
for i in range(10, 500, 10):
	counter = 0
	times = []
	while counter < 10:
		random_numbers_array = np.random.randint(0, 1000, i)
		# i starts from 10, at increments of 10
		# so we're increasing the size of the array by 10 for each iteration
		start_time = time.time()
		counting_sort(random_numbers_array)
		times.append(time.time() - start_time)
		# store time taken in list of times
		counter += 1
		# we'll run the sorting algorithm 10 times for each i-sized array
	average_times_counting_sort.append(sum(times)/len(times))
	# and find the average time for each i-sized array

average_times_shell_sort = []
for i in range(10, 500, 10):
	counter = 0
	times = []
	while counter < 10:
		random_numbers_array = np.random.randint(0, 1000, i)
		start_time = time.time()
		shell_sort(random_numbers_array)
		times.append(time.time() - start_time)
		counter += 1
	average_times_shell_sort.append(sum(times)/len(times))

x = range(10, 500, 10)
y1 = average_times_counting_sort
y2 = average_times_shell_sort
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x,y1, color="olive")
plt.plot(x,y2, color ="blue")
plt.ylabel("Average Time")
plt.xlabel("Size of Array")
plt.title("The Effect of Different Sort Algorithms on Runtime")
plt.legend(['Counting Sort', 'Shell Sort'], loc = "upper left", prop = {"size":10})
plt.plot()
plt.savefig("plot.pdf")
