# Самый обычный алгоритм бинарного поиска

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
        else:
            low = mid + 1
    return None


l1 = [1, 2, 3, 44, 5, 6, 57, 7, 56, 5464, 34, 4, 24]

print(binary_search(l1, 6))





