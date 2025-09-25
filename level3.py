'''
С помощью включения создайте следующий список:

[1, 2, 3, 4, 5, 6]

'''
print([i for i in range(1,7)])


'''
Даны два списка:

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
Объедините эти списки в один:

[1, 2, 3, 4, 5, 6]

'''

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(lst1 + lst2)

'''
Дан некоторый список, например, вот такой:

[1, 2, 3, 4, 5, 6]
Найдите сумму первой половины элементов этого списка.

'''
listA = [1, 2, 3, 4, 5, 6]
# for i, name in enumerate(listA):
# 	if(i < len(listA)/2)
print(sum(listA[0:int(len(listA)/2)]))

'''
С помощью включения создайте следующий список:

[1, 3, 5, 7, 9]

'''
print([i for i in range(1,10) if i%2!=0])


'''
Даны два кортежа:

tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
Объедините эти кортежи в один:

(1, 2, 3, 4, 5, 6)

'''
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
print(tpl1+tpl2)

'''
Даны два словаря:

dct1 = {
	'a': 1,
	'b': 2,
}
dct2 = {
	'c': 3, 
	'd': 4,
}
Объедините эти словари в один:

{
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}

'''

dct1 = {
	'a': 1,
	'b': 2,
}
dct2 = {
	'c': 3, 
	'd': 4,
}
listDct1K = list(dct1.keys())
listDct1V = list(dct1.values())
listDct2K = list(dct2.keys())
listDct2V = list(dct2.values())

dct3 = dict(zip(listDct1K + listDct2K, listDct1V + listDct2V))
print(dct3)

dct4 = {**dct1, **dct2}
print (dct4)
'''
Дан некоторый список, например, вот такой:

[1, 2, 3, 4, 5, 6]
Поделите сумму первой половины элементов этого списка на сумму второй половины элементов.

'''
listA = [1, 2, 3, 4, 5, 6]
sumOne = sum(listA[0: int(len(listA)/2)])
sumTwo = sum(listA[int(len(listA)/2): len(listA)])

print(sumOne/sumTwo)



'''
Дано некоторое число:

1357
Проверьте, что все цифры этого числа являются нечетными.
'''
numA = 13257
strA = str(numA).split()
x = 0
for i in range(len(strA)):
	if int(strA[i]) % 2 == 0:
		x += 1
if x == 0:
	print(f'{numA} - четных цифр число не содержит. {x}')
else:
	print(f'{numA} - четные цифры присутствуют. {x}')


'''
Дано некоторое слово:

'abcba'
Проверьте, что это слово читается одинаково с любой стороны.
'''
strA = 'abcbaR'
Arts = ''

for i in reversed(range(len(strA))):
	Arts += strA[i]

if(strA == Arts): print(f'{Arts} и {strA} читаются одинаково')
else: print(f'{Arts} и {strA} читаются по-разному')


'''
Даны два сета:

st1 = {1, 2, 3}
st2 = {4, 5, 6}
Объедините эти сеты в один:

{1, 2, 3, 4, 5, 6}
'''

st1 = {1, 2, 3}
st2 = {4, 5, 6}
print(st1.union(st2))


'''
Даны два сета:

st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}
Получите сет их общих элементов:

{4, 5}
'''

st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}

st3 = st1.intersection(st2)


'''
Даны два сета:

st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}
Получите сет элементов, входящих только в один из сетов:

{1, 2, 3, 6, 7, 8}
'''

print((st1.union(st2)).difference(st3))


'''


Дан текст со словами. Запишите в список все слова, начинающиеся на букву 'a'.
'''
stringA = 'Дан атекст со словами. Запишите в асписок все слова, начинающиеся на букву a.'
listA = stringA.split(' ')
newList = [i for i in listA if i[0] == 'а']
print (newList)

'''
Дан список со числами. Проверьте, что все элементы этого списка являются положительными числами.
'''
listA = [324,4234,42,314,324,-434]
listN = [i for i in listA if i > 0]

if len(listA) != len(listN) : print(f'{listA} \nОтрицательных чисел в списке: {len(listA) - len(listN)}')
else: print('Отрицательных чисел нет') 

'''
Даны два списка:

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
Получите список их общих элементов:

[4, 5]
'''
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

lst3 = set(lst1).intersection(set(lst2))
print (list(lst3))


'''
Дана некоторая переменная с числом:

num = 5;
Сделайте строку, содержащую столько нулей, сколько указано в переменной. В нашем случае получится такая строка:

'00000'
'''
num = 5
strA = ''
for i in range(5):
	strA += '0'

print(strA)

'''
Дан список со числами. Удалите из него числа, состоящие более чем из трех цифр.
'''
listN = [32, 134, 52344, 32, 52542, 25, 43, 43435]
listNew = [x for x in listN if round(x/1000) == 0]
print(listNew)
'''
Дана строка. Проверьте, что эта строка состоит только из цифр.
'''
stringA = "3425413342123"
listNumeric = []
listAlphabet = []
for i, value in enumerate(stringA):
	if value.isdigit():
		listNumeric.append(value)
	else:
		listAlphabet.append(value)

if len(listAlphabet) > 0: print(f"{stringA} - строка содрежит буквы: {listAlphabet}")
else: print(f"{stringA} - строка не содрежит букв")

'''
Дано число, например, вот такое:

num = 12345;
Проверьте, что все цифры этого числа больше нуля.
'''
num = 123405
minus = 0
stringA = str(num)
for i, value in enumerate(stringA):
	if (int(value) == 0): minus += 1 
print("есть цифры равные 0") if minus>0 else print("отсутсвуют 0")

'''
Даны два списка:

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3]
Проверьте, что все элементы первого списка есть во втором.
'''
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3]

for i in lst2:
	if i in lst1:
		print(f'элемент {i} найден')
	else:
		print(f'элемент {i} не найден')

'''
Дана строка. Сделайте заглавной последнюю букву каждого слова в этой строке.
'''
strA = 'Дана строка Сделайте заглавной последнюю букву каждого слова в этой строке'
listA = strA.split(' ')
listNew = [i[0:-1] + i[-1].upper() for i in listA]
print(' '.join(listNew))



'''
Дана строка. Проверьте, что эта строка состоит только из четных цифр.
'''

stringA = '4848838466'
n = 0
for x, value in enumerate(stringA):
	if int(value)%2!=0: n+=1
print ('только четные цифры') if n == 0 else print ('есть нечетные цифры')


'''
Даны две строки:

txt1 = '12345'
txt2 = '45678'
Получите символы, которые есть и в одной, и в другой строке:

'45'
'''

txt1 = '12345'
txt2 = '45678'
listA = []
listB = []
for i, value in enumerate(txt1):
	listA.append(txt1[i])
	listB.append(txt2[i])

setN = set(listA).intersection(set(listB))
print ("".join(list(setN)))


'''
Дана некоторая строка:

'a bc def ghij'
Переведите в верхний регистр все подстроки, в которых количество букв меньше или равно трем. В нашем случае должно получится следующее:

'A BC DEF ghij'
'''
stringA = 'a bc def ghij'
listA = stringA.split(' ')
listN = [i.upper() if len(i) <= 3 else i for i in listA]
print (' '.join(listN))
'''
Дан список со числами. Проверьте, что все числа из этого списка содержат в себе цифру 3.
'''
listA = [2233, 3432, 3422, 232, 4455, 122]
listN = [i for i in listA if '3' in str(i)]
print(f'нет цифры три в {len(listA) - len(listN)} числах списка')
'''
Через запятую написаны числа. Получите максимальное из этих чисел.
'''

strA = "1,2,3,54,21,23"
listA = strA.split(',')
print (listA)
print(max(listA))
a = 0
for i in listA:
	if (a < int(i)):
		a = int(i)
print (a)


'''
Дана строка в формате:

'kebab-case'
Преобразуйте ее в формат:

'snake_case'
'''
strA = 'kebeb-case'

listA = strA.split('-')
strB = '_'.join(listA)
print (f'{strA} -> {strB}')


'''
Дана строка в формате:

'snake_case'
Преобразуйте ее в формат:

'snakeCase'
'''
strA = 'snake_case'
listA = strA.split('_')
s = listA[1][0].upper()
strB = listA[0] + s + listA[1][1:]

print(strB)

'''
Дана строка в формате:

'camelCase'
Преобразуйте ее в формат:

'camel_case'
'''
strA = 'camelCase'
strB = ''
for i in strA:
	if i.islower():
		strB += i
	else: 
		strB += '_'+i
print(strB)
'''
Дан список с числами. Удалите из него числа, имеющие два и более нуля.
'''
from collections import Counter
listA = [12, 43, 5400, 3043, 43004, 244]
print(listA)
listB = []
for i, value in enumerate(listA):
	newA = Counter(str(value))
	if newA['0'] < 2:
		listB.append(value)
print(listB)


'''
Найдите все числа от 1 до 1000, сумма цифр которых равна 13. Результат запишите в сет.
'''
listA = list(range(1,1001))
listB = [x for x in listA if sum(list(map(int, str(x)))) == 13]
print (listB)
'''
Дан список:

[1, 2, 3]
Сделайте так, чтобы в нем каждый элемент повторился два раза:

[1, 1, 2, 2, 3, 3]
'''
listA = [1, 2, 3]

def functtr(n):
	return str(n)+str(n)

strA = ''.join(map(functtr, listA))

print(list(map(int, strA)))

'''
Даны два списка:

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
Переберите эти списки одним циклом и в каждой итерации выводите их элементы следующим образом:

'1,4'
'2,5'
'3,6'
'''


'''
Дан список и число. Оставьте в списке только те числа, которые являются делителями заданного числа.
'''


'''
Дан список с числами. После каждого однозначного числа вставьте еще такое же.
'''


'''
Даны два числа. Получите список цифр, которые есть и в одном, и во втором числе.
'''


'''
Дано число. Получите список позицией всех цифр 3 в этом числе, за исключением первой и последней.
'''


'''
Дан список со числами. Оставьте в нем числа, состоящие из разных цифр, а остальные удалите.
'''


'''
Даны два списка:

lst1 = [1, 2, 3];
lst2 = [1, 2, 3, 4, 5];
Удалите из большего списка лишние элементы с конца так, чтобы длины списков стали одинаковыми.
'''


'''
Дан список с некоторыми числами, например, вот такой:

[123, 456, 789]
Напишите код, который перевернет числа в этом списке по следующему принципу:

[321, 654, 987]
'''

'''

'''

'''

'''

'''

'''

'''

'''