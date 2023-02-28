'''  enumerate(iterable, [start - chislo, po defoltu 0])''' # generator, где каждый элемент - tuple состоящий из числа и элемента 

# нумерует элементы

# list_ = ['a', 'b', 'c', 'd']
# for i in enumerate (list_, 10):
#    print(i)
#  (0,a)
#   for a, b in enumerate(list_):
#    print('index -',a, 'element-', b)


''' zip(iterable, iterable -> * iterable) -> соединяет последовательности '''


#print(zip(list_1, list_2))

#print(list(zip(list_1,list_2)))

#list_1 = [1,2,3,4,5]
#list_2 = ['a', 'b,', 'c']
#print(list(zip(list_1,list_2)))




#lt = [1,2,3,4,5,33]
#lt2 = [0,0,0,0,0,0]
#lt3 = ['a', 'b', 'b', 'c', 'l']
#print(list(zip(lt, lt2,lt3)))



#dict_ = {1:2, 2:3, 3:4, 4:5}

#res = list(map(str, dict_.values()))
#diict_2 = dict(zip(dict_.keys(), res))

#print(diict_2)


# list_ = [1, 1, 3, 4, 54]

# def str_num(number):
#     if number %2 ==0:
#         return 'четное'
#     else:
#         return 'нечетное' 

# result = list(map(str_num, list_))
#print(result)

#print(list(map(lambda number: 'четное' if number %2 ==0 else 'нечетное', list_)))


# a = input()
# l = a.split()
# a,b = map(int, l)
# print(a,b)


