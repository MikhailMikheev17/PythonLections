# list_1 = []
# list_1 = list()
# print(list_1)


# list_1 = [1, 5]
# # print(*list_1) # звездочка , чтобы убрать []

# # print(len(list_1))
# # for i in list_1:
# #     print(i)

# # print(list_1[3])

# print(list_1)
# #append позволяет добавить элемент в конец нашего списка
# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)

# list_1 =[]
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)


#pop удаляет значение( и возвращает значение), если в pop в скобочках указать аргумент - то это индекс удаляемого элемента 
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]
    
#Надо указать значение индекса в качестве аргумента функции pop:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]


# Функция insert — указание индекса (позиции) и значения.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0] 

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# Кортеж — это неизменяемый список.
# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990,)
# print(type(t))

# v = [1,8,9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))


# # a = b =1
# # a,b = 1, 2
# a,b,c = v

# print(a,b,c)

# t = (1, 2, 3 , 5,)
# # for i in range(len(t)):
# #     print(t[i])

# # for i in t:
# #     print(i) 
# #
# t[0] = 2


# Словари и — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для определения
# элемента используется значение ключа (строка, число).
# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

# print('   ')

# print(dictionary.items())

# for (k,v) in dictionary.items():
#     print(k,v)

# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два множества,
# Вы можете совершать над ними любые стандартные операции, например, объединение,
# пересечение и разность. Давайте разберем их.
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# colors.clear() # { }
# print(colors) # set() - пустое множество

# Операции со множествами 
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                                      # c = {1, 2, 3, 5, 8}
# u = a.union(b)                                    # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)                             # i = {8, 2, 5}
# dl = a.difference(b)                              # dl = {1, 3}
# dr = b.difference(a)                              # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))      # {1, 21, 3, 13}

# a = {1, 8, 6}

# b = frozenset(a)

# print(b)

# Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#    list_1.append(i)

# print(list_1) # [1, 2, 3,..., 100]
# # Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
# print(list_1)
# print('  ')
# # Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
# print(list_1)
# print('  ')
# # Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]

# SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second # !!!!!
#  print(number_first)
# # Отсутствие :

# IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
#   print(number_first) # !!!!!
# # Отсутствие отступов

# #TypeError(Типовая ошибка)
# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа

# ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second)
# # Делить на 0 нельзя

#KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует

#NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# # Переменной names не существует

#ValueError(Ошибка значения)
# text = 'Python'
# print(int(text))
# Нельзя символы перевести в целые значения


