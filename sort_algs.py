# различные алгоритмы сортировки

# bubble sort O(n**2) (пузырьком)
def bubble_sort(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                t = l[j]
                l[j] = l[j + 1]
                l[j + 1] = t
    return l


l = [12, 6, 3, 5, 4, 11, 18, 19, 21, 24]
print(bubble_sort(l))


# merge sort O(nlogn) (слиянием)
def merge(l1, l2):
    l0 = []
    while l1 and l2:
        if l1[0] > l2[0]:
            l0.append(l2.pop(0))
        else:
            l0.append(l1.pop(0))
    while l1:
        l0.append(l1.pop(0))
    while l2:
        l0.append(l2.pop(0))
    return l0


def merge_sort(l):
    if len(l) == 1:
        return l

    l1 = l[:len(l) // 2]
    l2 = l[len(l) // 2:]
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    return merge(l1, l2)


l = [12, 6, 3, 5, 4, 11, 18, 19, 21, 24]
print(merge_sort(l))


# insertion sort O(n**2) (вставками)
def insertion_sort(l):
    for i in range(len(l) - 1):
        j = i
        while j > 0:
            if l[j - 1] > l[j]:
                t = l[j - 1]
                l[j - 1] = l[j]
                l[j] = t
            j -= 1
    return l

l = [12, 6, 3, 5, 4, 11, 18, 19, 21, 24]
print(insertion_sort(l))
