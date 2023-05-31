# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# n=int(input('Введите N: '))
# a=list(range(1,n+1))
# print(*a)
# x=int(input('Введите Х: '))
# if x > 0 and x < n:
#     print(1)
# else:
#     print(0)



n=int(input('Введите N: '))
import random
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(1,n))
print(*rand_list)
x=int(input('Введите X: '))
res=0
for i in range(len(rand_list)):
    if rand_list[i]==x:
        res+=1
print(res)

