import random
import re


def output():
    user_input = input("input words: ").split(',')
    result = []
    for elem in user_input:
        if elem not in result:
            result.append(elem)
    return result


# print(output())


def bajanarars(num: int):
    result = []
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            result.append(i)
    return result


# print(bajanarars(12))

def ideal_num(num: int):
    result = []
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            result.append(i)
    if sum(result) == num:
        return True
    else:
        return False


# print(ideal_num(12))
def zip(data1, data2):
    result = []
    if len(data1) == len(data2):
        for i in range(len(data1)):
            result.append(data1[i])
            result.append(data2[i])
    return result


a1 = [1, 2, 3, 4, 5, 6]
a2 = [10, 20, 30, 40, 50, 60]


# print(zip(a1,a2))

def polindrom(str: str):
    # result = re.sub('[^A-Za-z0-9]+', ' ', str).lower().split(' ')
    # result.pop()
    str = re.sub('[^A-Za-z0-9]+', ' ', str).lower().split(' ')
    str.pop()
    result = str[::-1]
    print(result)
    print(str)
    if str == result:
        return True
    else:
        return False


# print(polindrom("Herb the sage eats sage, the herb "))


def middle():
    nums = (input("input list of numbers: ").split(' '))
    nums = list(int(x) for x in nums)
    nums = sorted(nums)
    _midlle = sum(nums)/len(nums)
    low_then = []
    high_then = []
    for elem in nums:
        if elem < _midlle:
            low_then.append(elem)
    for elem in nums:
        if elem > _midlle:
            high_then.append(elem)

    return _midlle, low_then, high_then


#print(middle())

def for_game():
    result = []
    for i in range(6):
        x = random.randint(1, 49)
        if x not in result:
            result.append(x)
    return sorted(result)

#print(for_game())

def is_sorted():
    result = [int(x) for x in input("input nums: ").split()]
    print(result)
    if sorted(result) == result:
        return True
    elif sorted(result)[::-1]==result:
        return True
    else:
        return False


#print(is_sorted())

def  is_sublist(larger:list, smaller:list): #[1,2,3,4] [1,2]
    ok = True
    for i in range(len(smaller)):
        try:
            x = larger.index(smaller[i])
            if x + 1 !=  larger.index(smaller[i+1]):
                ok = False
        except:
            pass
    return ok


#print(is_sublist([1, 2, 3, 4, 5], [2, 3, 5]))