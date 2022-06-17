def fact(n, res=1):
    if n == 1:
        return res
    return fact(n-1, res*n)

#print(fact(5))

def evk(a, b):
    if b == 0:
        return a
    return evk(b, a % b)

#print(evk(24, 60))

def evk_rek(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#print(evk_rek(24, 60))

a = [1232, 12, 6, 63, 6, 21,22342, 3, 4, 43, 5, 12, 6, 6, 202,2]


def contain(data, val):
    count = 0
    while count < len(data):
        if data[count] == val:
            return True
        count += 1
    return False

#print(contain(a, 7))


def pop(data, i=None):
    if i is None:
        return a[:-1]
    count = 0
    new_list = []
    while count < len(data):
        if count != i:
            new_list.append(data[count])
        else:
            print('deleted item is: ', a[i] ,'\nindex: ', i)
        count += 1
    return new_list

#print(pop(a))

def remove_all(data, value):
    count = 0
    new_data = []
    while count < len(data):
        if data[count] != value:
            new_data.append(data[count])
        count += 1
    print('old data: ', data, '\nnew data: ', new_data )
    return new_data

#remove_all(a, 6)

def reverse(data):
    count = len(data) - 1
    new_data = []
    while count >= 0:
        new_data.append(data[count])
        count -= 1
    print('old data: ', data, '\nnew data: ', new_data )
    return new_data

#reverse(a)

# kisov krchatenq veronshyal funkcian DD
# bayc de meka ban chi poxvum grubi zakon ka O(n) a mnalu

def reverse_(data):
    print(data)
    first = 0
    end = len(data) - 1
    while first < len(data)/2:
        data[first], data[end] = data[end], data[first]
        first += 1
        end -= 1
    return data


#print(reverse_(a))


def min_and_max(data):
    count = 0
    min, max = data[0], 0
    while count < len(data):
        if min > data[count]:
            min = data[count]
        if max < data[count]:
            max = data[count]
        count += 1
    print(data)
    print('minimal value: ', min)
    print('maximal value: ', max)
    return min, max

#min_and_max(a)

