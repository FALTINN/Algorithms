def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    return None


list = list()
for i in range(1, 500000000 + 1):
    list.append(i)
print(binary_search(list, 500000000))