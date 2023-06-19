# def f(x):
#     return x*x

# a = f
# print(a(5))
# print(f(5))

# def calc1(a,b):
#     return a + b
# def calc2(a,b):
#      return a * b

# def math(op,x,y):
#      print(op(x,y))
# #calc1 = lambda a,b : a + b

# math(lambda a,b : a + b,5,45)    

# import math
# list_1 =[]
# length = int(input('length >'))

# for i in range(length):
#     list_1.append(int(input()))

# print(list_1)    

# def sq(list_1):
#     for i in range(len(list_1)):
#         if list_1[i] % 2 == 0:
#             print(f'{list_1[i]},{math.pow(list_1[i],2)}')

# sq(list_1)            

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data :
#   if i % 2 == 0:
#     out.append((i, i ** 2))
# print(out)

# def select(f,col):    вместо этой функции есть встроенная - map(что делать, аргумент)
#     return [f(x) for x in col]

# def where(f,col):     вместо этой функции есть встроенная - filter(что делать, аргумент) - возвращает то, что тру
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int,data)
# print(res)
# res = where(lambda x: x % 2 == 0,res )
# print(res)
# res = list(select(lambda x: (x,x**2),res))
# print(res)

# list_1 = [x for x in range (1,20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10,list_1)) 
# print(list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

#.split() # преобразует строку в список

# data = ' 15 5725 52 5 885 28 5'
# print(data)

# # data = data.split()
# # print(data)

# data = list(map(int, data.split()))
# print(data)

# data = [15,65,9,36,175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]


# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#  print(line)
# data.close()



