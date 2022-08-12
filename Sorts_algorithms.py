# Bubble sort

def bubble_sort(lst: list):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


# print(bubble_sort([12, 2, 3, 12, 45, 23, 123, 46]))
def argmin(lst: list):
    x = lst[0]
    for i in range(len(lst)):
        if x > lst[i]:
            x = lst[i]
    return x


def selection_sort(lst: list):
    for i in range(len(lst) - 1):
        lst1 = lst[i:]
        min_index = lst1.index(min(lst1)) + i
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


# print(selection_sort([123, 12, 31, 25, 51, 20, 20, 20]))

def insertion_sort(lst: list):
    for i in range(1, len(lst) - 1):
        while i != 0:
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                i -= 1
            else:
                break
    return lst


# print(insertion_sort([2, 4, 6, 1, 3, 8, 0, 12]))


def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2

    left = merge_sort(array[:half])
    right = merge_sort(array[half:])
    return merge(left, right)
