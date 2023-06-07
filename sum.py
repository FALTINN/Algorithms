def sum(arr: list):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])

def quantity(arr: list):
    if len(arr) == 0:
        return 0
    else:
        return  1 + quantity(arr[1:])

def max(arr: list):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1] 
    else:
        sub_max = max(arr[1:])
        return arr[0] if arr[0] > sub_max else sub_max

print(sum([2, 4, 6]))
print(quantity([2, 4, 6, 'sdf']))
print(max([2, 4, 6, 12]))