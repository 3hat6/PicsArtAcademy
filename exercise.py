import math
import random
import Sorts_algorithms


def four_milliards_nums():
    file = open('new_file.txt', 'w')
    for i in range(4 * (10 ** 7)):
        file.write(str(random.randint(0, 200)) + ' ')


def remove_duplicates_from_sorted_array(lst: list):
    result = []
    count = 0
    for elem in lst:
        if elem not in result:
            result.append(elem)
        else:
            count += 1
    for i in range(count):
        result.append('_')
    print(result)
    return count


# print(remove_duplicates_from_sorted_array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


def merge_sorted_array(lst1, m, lst2, n):
    result = lst1[:n] + lst2[:m]
    return sorted(result)


# print(merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))


def contains_duplicate(lst: list):
    for elem in lst:
        if lst.count(elem) >= 2:
            return True

    return False


# print(contains_duplicate([1, 2, 3, 4]))


def single_number(lst: list):
    rand_index = []
    for i in range(len(lst) - 1):
        index = random.randint(0, len(lst) - 1)
        if index not in rand_index:
            if lst.count(lst[index]) == 1:
                return lst[index]
            else:
                rand_index.append(index)
    return -1


# print(single_number([4, 1, 2, 1, 2]))


def missing_number(lst: list):
    lst = sorted(lst)
    for i in range(max(lst)):
        if i != lst[i]:
            return i


# print(missing_number([3,0,1]))

def max_consecutive_ones(lst: list):
    count = 1
    max = 0
    for i in range(0, len(lst) - 1):
        if lst[i] == lst[i + 1]:
            count += 1
            max = count
        else:
            count = 1
            i -= 1
    return max


# print(max_consecutive_ones([1, 0, 1, 1, 1, 1, 0, 1]))

def array_partition(lst: list):
    pairings = []
    while len(lst) >= 2:
        pairings.append(lst[:2])
        print(pairings)
        lst = lst[2:]
    result = 0
    for elem in pairings:
        result += min(elem)
    return result


# print(array_partition([6, 2, 6, 5, 1, 2]))

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def largest_prime(num: int):
    for i in range(int(math.sqrt(num)), 0, -1):
        if is_prime(i) and num % i == 0:
            return i
    return -1


# print(largest_prime(600851475143))

def largest_palindrome():
    for i in range(999, 900, -1):
        if i == 993:
            for j in range(i, 900, -1):
                if j == 913:
                    if str(j * i) == (str(j * i)[::-1]):
                        return j * i
    return -1


# print(largest_palindrome())

def smallest_multiple():
    result = 2520
    ok = False
    while True:
        for i in range(1, 20):
            if result % i == 0:
                ok = True
            else:
                result += 1
                continue
        if ok:
            return result


def sum_square():
    small, big = 0, 0
    for i in range(101):
        small += i ** 2
        big += i
    return big ** 2 - small


# print(sum_square())
