import string


def two_sum(lst: list, target: int):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] == target:
                return i, j


# print(two_sum([2, 9, 11, 7, 4, 5], 9))

def reverse_bits(num: str):
    num = num[::-1]
    return int(num, 2)


# print(reverse_bits('00000010100101000001111010011100'))


def remove_duplicates(lst: list):
    result = []
    counter = 0
    for elem in lst:
        if elem not in result:
            result.append(elem)
        else:
            counter += 1
    result += counter * '_'
    return result


# print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


def roman_to_integer(txt: str):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    summ = 0
    for i in range(len(txt) - 1, -1, -1):
        num = roman[txt[i]]
        if 3 * num < summ:
            summ = summ - num
        else:
            summ = summ + num
    return summ


# print(roman_to_integer("LVIII"))

# print(roman_to_integer())
def excel_sheets(num: int):
    result = ''
    di = dict(zip(string.ascii_letters, [ord(c) % 32 for c in string.ascii_letters]))
    new_dct = {v: k for k, v in di.items()}
    if num > 26:
        return new_dct[num // 26] + new_dct[num % 26]
    else:
        return new_dct[num]


# print(excel_sheets(701))

def buy_sell(lst: list):
    max = 0
    for i in range(len(lst) - 2):
        for j in range(i, len(lst) - 1):
            if lst[j] - lst[i] > max:
                max = lst[j] - lst[i]
    return max


# print(buy_sell([7, 1, 5, 3, 6, 4]))

def insertion_two_arrays(lst1: list, lst2: list):
    result = []
    [result.append(elem) for elem in lst1 if elem not in result and elem in lst2]
    return result


# print(insertion_two_arrays([4, 9, 5], [9, 4, 9, 8, 4]))

def merge_lst(lst1: list, lst2: list):
    return sorted(lst1 + lst2)


# print(merge_lst([1, 2, 4], [1, 3, 4]))


def my_atoi(num: str):
    res = ''
    for elem in num:
        if elem != ' ':
            try:
                int(elem)
                res += elem
            except:
                if elem == '-':
                    res += elem

    return int(res)


# print(my_atoi('-42'))

def max_area(lst: list):
    area = min(lst)
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1, i, -1):
            if min(lst[i], lst[j]) * (j - i) > area:
                area = min(lst[i], lst[j]) * (j - i)

    return area

# print(max_area([1, 1]))
