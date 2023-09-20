# Алгоритм быстрой сортировки. Каждый этап подробно описывается
# Исходный массив разбивается на два, исходя из выбранной опорной точки: элементы меньше опорного и больше опорного
# Использование случайного опорного элемента может помочь уменьшить затрачиваемое время.

import random


def quick_sort(list):  # ОПОРНЫЙ ЭЛЕМЕНТ - ПЕРВЫЙ В СПИСКЕ
    print(f"Исходный массив:\n{list}")
    if len(list) < 2:
        print(
            "Массив содержит всего один элемент (или не содержит элементов вообще), следовательно, он не нуждается в сортировке.")
        print()
        return list
    print(
        "Выберем опорную точку среди элементов массива (элемент, относительно которого будут созданы массивы меньших и больших величин):")
    pivot = list[0]
    print(f"данной точкой стал элемент {pivot}. Создадим массивы меньших и больших величин.")
    print("Массив меньших величин:")
    less_than_pivot = [i for i in list[1:] if i <= pivot]
    print(less_than_pivot)
    print("Массив больших величин:")
    greater_than_pivot = [i for i in list[1:] if i > pivot]
    print(greater_than_pivot)
    print("Теперь отсортируем по отдельности массивы меньшиих и больших величин.")
    print()
    print()
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


test_list = [37, 83, 53, 35, 18, 72, 43, 99, 42, 85, 54, 76, 92, 78, 58, 15, 43]


# print(quick_sort(test_list))


def quick_sort_rand(list):  # ОПОРНЫЙ ЭЛЕМЕНТ - СЛУЧАЙНЫЙ
    print(f"Исходный массив:\n{list}")
    if len(list) < 2:
        print(
            "Массив содержит всего один элемент (или не содержит элементов вообще), следовательно, он не нуждается в сортировке.")
        print()
        return list
    print(
        "Выберем опорную точку среди элементов массива (элемент, относительно которого будут созданы массивы меньших и больших величин):")
    pivot = list.pop(random.randint(0, len(list) - 1))
    print(f"данной точкой стал элемент {pivot}. Создадим массивы меньших и больших величин.")
    print("Массив меньших величин:")
    less_than_pivot = [i for i in list if i <= pivot]
    print(less_than_pivot)
    print("Массив больших величин:")
    greater_than_pivot = [i for i in list if i > pivot]
    print(greater_than_pivot)
    print("Теперь отсортируем по отдельности массивы меньшиих и больших величин.")
    print()
    print()
    final_result = quick_sort_rand(less_than_pivot) + [pivot] + quick_sort_rand(greater_than_pivot)
    return final_result


print(quick_sort_rand(test_list))
