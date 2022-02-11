def binary_search(num_list, target, start, last):
    if start <= last:
        mid = (start + last) // 2
        if num_list[mid] == target:
            return mid
        elif num_list[mid] > target:
            return binary_search(num_list, target, start, mid - 1)
        else:
            return binary_search(num_list, target, mid + 1, last)
    else:
        return "target is not in the list"

#try
numbers = [6,12,23,53,222,555,2222]
want = 23

result = binary_search(numbers, want, 0, len(numbers) - 1)
print("The target is at index: " + str(result))