# Сортировка выбором

def find_smallest(arr):  # поиск минимального элемента
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):  # генерация отсортированного массива
    sorted_arr = []
    for i in range(len(arr)):
        sorted_arr.append(arr.pop(find_smallest(arr)))
    return sorted_arr


print(selection_sort([1, 2, 3, 44, 5, 6, 57, 7, 56, 5464, 34, 4, 24]))
