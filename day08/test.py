my_numbers = [1, 9, 8, 5, 4, 6, 0, 2, 3, 7]

def selection_sort(numbers):
	new_list = []
	while len(numbers) != 0:
		new_list.append(numbers.pop(numbers.index(min(numbers))))
	return new_list

def insertion_sort(numbers):
	for i in range(1, len(numbers)):
		for j in range(i):
			if numbers[i] < numbers[j]:
				to_insert = numbers.pop(i)
				numbers.insert(j, to_insert)
		print(numbers)
	return numbers

def bubble_sort(numbers):
	count = len(numbers)
	while count != 0:
		for j in range(1,count):
			if numbers[j] < numbers[j-1]:
				small_number = numbers.pop(j)
				numbers.insert(j-1, small_number)
				print(numbers)
		count -= 1		
	return numbers

print(bubble_sort(my_numbers))
