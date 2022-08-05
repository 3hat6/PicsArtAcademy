# 1
def sum_in_file():
    file = open('file.txt').read().split(',')
    result = 0
    for elem in file:
        result += int(elem)
    print(result)


# 2
def upper_only_first_char():
    file = open('text.txt').read().split(' ')
    result = ''
    for elem in file:
        elem = elem.lower()
        result += elem[0].upper() + elem[1:] + ' '
    print(result)
    attached = open('new_txt.txt', mode='w').write(result)


# 3
def repeats_in_list():
    lst = [1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9]
    dct = {}
    for elem in lst:
        if elem not in dct.keys():
            dct[elem] = lst.count(elem)
        else:
            pass
    return dct


# 4
def symbols_in_text():
    file = open('text.txt').read()
    result = len(file)
    print(result)


# 5
def every_third_symbol():
    str = open('text.txt').read()
    result = ''
    count = 1
    for elem in str:
        if count % 3 == 0:
            pass
        else:
            result += elem
        count += 1
    print(result)


# 6
def counts_of_words():
    file = open('text.txt').read().split(' ')
    result = ''
    for word in file:
        if result.__contains__(word):
            pass
        else:
            result += word + ' - ' + str(file.count(word)) + '\n'
    print(result)


# 7
def squares():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    new_array = [elem ** 2 for elem in arr]
    print(new_array)
    new_array = sorted(new_array)
    print(new_array)


# 8
def sum_numbers(num):
    result = 0
    while num != 0:
        result += num % 10
        num = num // 10
    return result


# 9
def innominato(num):
    multiply = 1
    sum = 0
    while num != 0:
        sum += num % 10
        multiply *= num % 10
        num = num // 10
    return multiply - sum


# 10
def kenter(start, end):
    result = [x for x in range(start, end + 1) if x % 2 != 0]
    return result


# day 2
# 1
def strmove(txt, count):
    start = len(txt) - count
    result = txt[start:] + txt[:start]
    return result


# 2
def idK():
    lst = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
    print(sum(lst))


# 3
def sum_even_fib():
    x = 1
    y = 2
    lst = [1, 1, 2]

    while lst[-1] < 4 * (10 ** 6):
        z = x + y
        lst.append(z)
        x, y = y, z
    attached = [x for x in lst if x % 2 == 0]
    print(lst)
    print(attached)
    return sum(attached)


# day 3
# 1

def blablabla():
    big = sum(range(100)) ** 2
    small = sum([x ** 2 for x in range(100)])
    return big - small


def palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


