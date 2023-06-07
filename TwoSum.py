def TwoSum(list, k):
    leftIndicator = 0
    rightIndicator = len(list) - 1
    while leftIndicator < rightIndicator:
        sum = list[leftIndicator] + list[rightIndicator]
        if sum == k:
            return [list[leftIndicator], list[rightIndicator]]
        elif sum < k:
            leftIndicator += 1
        else:
            rightIndicator -= 1
    return []


list = list()
for i in range(1, 90000 + 1):
    list.append(i)
print(TwoSum(list, 124500))