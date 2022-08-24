import re

def push_pop(lst: list, n: int):
    result = []
    for i in range(lst[0], lst[-1] + 1):
        if i in lst:
            result.append('push')
        else:
            result.append('push')
            result.append('pop')
    return result


# print(push_pop([1, 2, 4, 5], 7))
# 2
def intersection(lst1: list, lst2: list):
    # result = [x for x in lst1 if x in lst2]
    result = []
    for elem in lst1:
        if elem in lst2 and elem not in result:
            result.append(elem)
    return result


# print(intersection([1, 2, 2, 1], [2, 2]))
# 3
def frequency(lst: list):
    max, element = 0, 0
    for elem in lst:
        count = lst.count(elem)
        if count > max:
            max = count
            element = elem
    start = lst.index(element)
    lst.reverse()
    end = lst.index(element)
    lst.reverse()
    result = lst[start: len(lst) - end]
    return result


# print(frequency([1, 2, 2, 3, 4]))

# 4

def sort_array_by_parity(lst: list):
    lst1 = [x for x in lst if x % 2 == 0]
    lst2 = [x for x in lst if x % 2 != 0]
    return lst1 + lst2


# print(sort_array_by_parity([1,2,3,1,2,3,4,5,2,3,4,1]))


# 5
def sum_of_unique(lst: list):
    result = [x for x in lst if lst.count(x) == 1]
    return sum(result)


# print(sum_of_unique([1, 2, 3, 4, 1, 2, 5, 4]))

# 6
def implement_strstr(needle: str, haystack: str):
    if needle.__contains__(haystack):
        return needle.index(haystack[0])
    else:
        return -1


# print(implement_strstr('hello', 'll'))

# 7
def length_of_last_word(text: str):
    lst = text.split(' ')
    return len(lst[-1])


# print(length_of_last_word('hello world'))

# 8
def valid_palindrome(text: str):
    text = re.sub('[!@#$:,?` ]', '', text).lower()
    if text == text[::-1]:
        return True
    else:
        return False


# print(valid_palindrome('A man, a plan, a canal: Panama'))

# 9
def valid_email(lst: list):
    result = []
    for elem in lst:
        end = str(elem).index('@')
        attached = re.sub('[+.]', '', elem[:end])
        attached += elem[end:]
        if attached.count('.') == 1:
            result.append(attached)
    return len(result)


print(valid_email(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))


# 10
def non_decreasing(lst: list, target: int):
    result = [x for x in range(len(lst)) if lst[x] == target]
    return result

# print(non_decreasing([1, 2, 2, 3, 3, 3, 3, 4, 5, 6], 3))
