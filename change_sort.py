def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def findBiggest(arr):
    biggest = arr[0]
    biggest_index = 0
    for i in range (1, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i
    return biggest_index

def selectionSort(arr: list, type: str="small"):
    newArr = []
    for i in range(len(arr)):
        if type == "big":
            element = findBiggest(arr)
        else:
            element = findSmallest(arr)
        newArr.append(arr.pop(element))
        """функция pop() удаляет элемент по индексу и возвращает значение удалённого элемента"""
    return newArr

print(selectionSort([5, 3, 3, 6, 1], "big"))