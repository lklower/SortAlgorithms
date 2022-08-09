
def bubble_sort(data: list) -> list:
    n: int = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


def selection_sort(data: list) -> list:
    n: int = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[min_idx] > data[j]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

    return data


def insertion_sort(data: list) -> list:
    n: int = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

    return data


def merge_sort(data: list) -> list:
    if len(data) > 1:
        mid: int = len(data) // 2
        left: list = data[:mid]
        right: list = data[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp lists left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    return data


def quick_sort(data: list) -> list:
    return quickSort(data, 0, len(data) - 1)


def quickSort(data: list, low: int, high: int) -> list:
    if low < high:
        pi = partition(data=data, low=low, high=high)
        # Recursive call on the left of pivot
        quickSort(data, low, pi - 1)
        # Recursive call on the right of pivot
        quickSort(data, pi + 1, high)

    return data


def partition(data: list, low, high) -> int:
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] <= pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1
