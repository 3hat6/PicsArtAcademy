

a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = [100, 200, 300, 400, 500]
d = [2, 3, 4, 5, 6]

def triple(data):
    result = [None] * len(data)
    for i in range(len(data)):
        result[i] = data[i] * 3
    return result

#print(triple(a))

def mul(a, b, c):
    return a * b * c

def sum(a, b, c):
    return a + b + c

# qani vor try except h@l@ chenq ancel es checker@ grelem vor stugi
# ka ed indexov element te che ete chka exeptiona qcum listn u tivna het veradardzum
def checker(index, list1, list2, list3):
    text = 'please add missed value in list %s at %d-th place'
    if index >= len(list1):
        ok = False
        text = text % (list1,  index+1)
        raise IndexError(text)
    elif index >= len(list2):
        text = text % (list2, index + 1)
        raise IndexError(text)
    elif index >= len(list3):
        text = text % (list3, index + 1)
        raise IndexError(text)
    else:
        ok = True
    return ok

def map3(func, data1, data2, data3):
    once = max(len(data1), len(data2), len(data3))
    result = [None] * once
    for i in range(once):
        if checker(i, data1, data2, data3):
            result[i] = func(data1[i], data2[i], data3[i])
    return result

#print(map3(mul, a, b, c))

def map2(data1, data2, func=pow):
    result = [None] * len(data1)
    for i in range(len(result)):
        result[i] = func(data1[i], data2[i])
    return result


print(map2(a, d))