import math
import random


def reverse_num():
    num = input("input any number: ")
    _reverse = num[::-1]
    return _reverse


# print(reverse_num())

def joint():
    _list = tuple(input("input numbers: ").split(' '))
    result = ''
    for elem in _list:
        result += elem
    return result


# print(joint())

def sum_of_min_max(data: list):
    return max(data) + min(data)


# print(sum_of_min_max([1, 2, 55, 3, 4, 5, 6, 19]))

def even_index(data: list):
    for i in range(len(data)):
        if data[i] % 2 == 0:
            print(f"index: {i} elem {data[i]}")


# even_index([1, 2, 3, 4, 5, 6, 7, 8])

def reversed_str():
    word = input("input any word i show u reversed version: ")
    result = ""
    for i in range(len(word) - 1, -1, -1):
        result += word[i]
    return result


#print(reversed_str())


def smallest_prime(n):
    while True:
        ok = True
        n += 1
        for j in range(2, int(n/2) + 1):
            if n % j == 0:
                ok = False

        if ok:
            return n


#print(smallest_prime(19))

def get_median(data):
    if len(data) % 2 != 0:
        return data[int(len(data)/2)]
    else:
        return (data[int(len(data)/2) - 1] + data[int(len(data)/2)])/2


#print(get_median([1, 2, 3, 4, 5, 6, 7, 8]))

def days_in_month(month:int, year):
    if month == 2:
        if year % 4 == 0:
            return 29
        return 28
    if month % 2 == 0 and month != 6:
        return 30
    else:
        return 31

#print(days_in_month(3, 2025))

def random_passwd(n):
    passwrd = ''
    for i in range(n):
        num = random.randint(33, 126)
        passwrd += chr(num)
    return passwrd


#print(random_passwd(50))

def same_parity(n, *args):
    result = []
    for elem in args:
        try:
            if elem % n == 0:
                result.append(elem)
        except:
            pass
    return result


#print(same_parity(3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 21, "juju"))
