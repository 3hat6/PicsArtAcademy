import math


def _print():
    print('Leo from California 666')

def _output():
    name = input("input your name: ")
    print(f'Welcome to our industry {name}!')

def _are():
    height = int(input('input room`s height: '))
    length = int(input('input room`s length: '))
    return height * length

def _are_in_funts():
    height = int(input('input room`s height in akreqov: '))
    length = int(input('input room`s length in akreqov: '))
    return height * length / 43560

def bottles():
    bigger = float(input("input counts of bigger than 1l: "))
    smaller = float(input("input counts of smaller than 1l: "))
    print(f"small bottles price is {smaller*0.10:.2f} bigs are {bigger*0.25:.2f}")

def taxes():
    profit = float(input('input profit: '))
    _taxes = profit * 0.20
    tip = (profit - _taxes) * 0.18
    profit += _taxes + tip
    print(f"all profit is {profit} in this profit already include the taxes ({_taxes}) and the tip ({tip})")

def sum_of_nums():
    n = int(input("input any num and i calculate all the sum untill your num): "))
    sum = 0
    while n!=0:
        sum+=n
        n-=1
    return sum


def gifts():
    bigs = int(input("input counts of big gifts: ")) * 112
    smalls = int(input("input counts of small gifts: ")) * 75
    print(f"all weight of gifts is {bigs*smalls} grams")

def bank():
    investement = float(input('input investment sum in $: '))
    for_since = investement
    year = int(input('input how many years you wanna keep your money: '))
    for i in range(year):
        percent = investement * 0.04
        investement += percent
        print(f'for {i+1} year bank gives u {percent:.2f} percent and your money will be like {investement:.2f}')
    print(f"so in {year} years you make {investement-for_since:.2f} money")

def calculate():
    a = int(input("input a num: "))
    b = int(input("input another num: "))
    print(f"your nums sum is {a+b} diminish is {a-b} decrease is {a/b} remainder is {a % b} rounder is {a//b}"
          f"logarithm is {math.log(a)}")

def milles_to_km():
    mpg = float(input("input miles-per-gallon(MPG) i will change it on liters-per-hundred: "))
    lph = mpg / 3.78541178
    print(f"{mpg} mpg will be {lph:.4f} lph")

def height_in_sm():
    height = [float(x) for x in input("input how much is your height in futs and inch: ").split(' ')]
    _height = height[0] * 12 * 54 + height[1]
    print(f"your height in sm will be {_height}")

def different_distance():
    foot = float(input("input distance in foots: "))
    inch = foot * 12
    yard = foot/3
    mile = foot / 5280
    print(f"{foot} foot will be {inch} in inch, {yard:.2f} in yards, {mile:.2f} in miles")

def circle_area():
    r = float(input("input circles radius: "))
    area = 3.14 * math.pow(r, 2)
    volume = 4/3 * 3.14 * math.pow(r, 3)
    print(f'circle are is {area:.2f}, and the bools is {volume:.2f}')

def glani_caval_voshm_angeleren_chgitem():
    r = float(input("input circles radius: "))
    heigth = float(input("input glan`s height: "))
    area = 3.14 * math.pow(r, 2)
    print(f'glani caval@ {area*heigth:.1f} esqana')

glani_caval_voshm_angeleren_chgitem()
