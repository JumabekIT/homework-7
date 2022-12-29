# линейный поиск

name = ['бека', 'beka', 'erf', 'нурислам', 'adahan']

search_for = 'нурислам'  # что ищем


def linear_search(where, what):
    for v in enumerate(where):
        if v[1] == what:
            return v[0]  # возвращаем индекс

    return None


print('искомый элемент', search_for, 'найден под индексом',
      linear_search(name, search_for))

# o(5)


# сортировка выборкой
# o(n2)
nums = [2, 3, 1, 3, 1, 5, 7, 85, 5, 3, 44, 9, 9]
print(sorted(nums))
print('было', nums)

for i in range(len(nums)):
    lowest = i  # первый элемент за наименьший

    for j in range(i + 1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j

    nums[i],nums[lowest]=nums[lowest],nums[i]
n=1
m=2
n,m=m,n
print('стало',nums)




ma = sorted(nums)
print(ma)

nu = 44

lowest = 0
highest = len(ma) - 1
index = None

while(lowest <= highest) and (index is None):

    mid = (lowest + highest)//2
    if ma[mid] == nu:
        index = mid
    else:
        if nu < ma[mid]:

            highest = mid - 1
        else:

            lowest = mid + 1


print("исомый элемент", nu, "находится под индексом", index)


# алгоритм Евклида - назождение нод 

def nod(a, b):
    while a!= 0 and b!= 0:
        if a > b:
                a = a % b
        else:
                b = b % a
        return b + a
print("НОД чисел 69 120 =", nod(70, 120))
from math import gcd
print(gcd(70, 120))

# поворот строки 

some_string = "я не сегодня заболел!"

def reversee(s):
    chars = list(s)

    for i in range(len(s)//2):

        temp = chars[i]
        chars[i] = chars(len(s) - i - 1)
        chars[len(s) - i - 1] - temp
    
    return ''.join(chars)

print(some_string)
print(reversee(some_string))


