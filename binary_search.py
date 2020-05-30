def binary_search(list, item):
	low = 0
	high = len(list)

	while low <= high:
		mid = int((low + high)/2)
		guess = list[mid]
		if guess == item:
			return mid
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None


print(binary_search([1,32,123,321,312,4], 321))
print(binary_search([1,32,123,321,312,4], 3))