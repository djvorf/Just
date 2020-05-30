def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index


def selectionsSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr


print(selectionsSort([32,12,5,96,8,54]))