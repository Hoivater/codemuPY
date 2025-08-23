


"""1 Дано число. Проверьте, отрицательное оно или нет. Выведите об этом информацию в консоль."""
a_list = list(range(-10, 20))
print(a_list)
a_set = set(a_list)
print(a_set)

for i in a_set:
	if i > 0:
		print (f'Число {i} больше нуля. Число положительное')
	elif i == 0:
		print (f'Число {i} равно нулю')
	else:
		print (f'Число {i} меньше нуля. Число отрицательное')


"""2 Дана строка. Выведите в консоль длину этой строки."""
stringA = "Дана строка. Выведите в консоль длину этой строки."
print(f'Длина строки: \'{stringA}\' равна {len(stringA)}')


"""3 Дана строка. Выведите в консоль последний символ строки."""
stringA = "Дана строка. Выведите в консоль последний символ строки."
print(stringA[-1])


"""4 Дано число. Проверьте, четное оно или нет."""
for i in a_list:
	res = i%2
	if res == 0:
		print(f'число {i} - четное')
	else:
		print(f'число {i} - нечетное. Остаток от деления на 2 равен: {res}') 


"""5 Даны два слова. Проверьте, что первые буквы этих слов совпадают."""
wordA = 'первый'
wordB = 'пароходьььььььььььььььь'

if wordA[0] == wordB[0]:
	print(f'{wordA[0]} и {wordB[0]} совпадают')
else:
	print(f'{wordA[0]} и {wordB[0]} несовпадают')


'''6 Дано слово. Получите его последнюю букву. Если слово заканчивается на мягкий знак, то получите предпоследнюю букву.'''
def wordEndLitera(word):
	a = ''
	for i in word:
		if(i != 'ь'):
			a = i
	return a
print(f'в слове {wordA} последней буквой, кроме Ь является: {wordEndLitera(wordA)}')
print(f'в слове {wordB} последней буквой, кроме Ь является: {wordEndLitera(wordB)}')


"""7 Дано число. Выведите в консоль первую цифру этого числа."""
numberA = 1234
print (str(numberA)[0])


"""8 Дано число. Выведите в консоль последнюю цифру этого числа."""
print(str(numberA)[-1])

"""9 Дано число. Выведите в консоль сумму первой и последней цифры этого числа."""
numA = str(numberA)[0]
numB = str(numberA)[-1]

print (f'{numA} + {numB} = {int(numA) + int(numB)}')


"""10 Дано число. Выведите количество цифр в этом числе."""
print(len(str(numberA)))

"""11 Даны два числа. Проверьте, что первые цифры этих чисел совпадают."""
numberB = 14313

if str(numberA)[0] == str(numberB)[0]:
	print('Цифры совпадают')
else:
	print('цифры не совпадают') 

'''12 дан список, получите срез'''
listA = [1, 2, 3, 4, 5, 6];
print(listA[:3])

'''13 Дана строка. Если в этой строке более одного символа, выведите в консоль предпоследний символ этой строки.'''
if len(wordA) > 1:
	print(f'Предпоследний символ строки: _{wordA}_ равен {wordA[-2]}')

'''14 Даны два целых числа. Проверьте, что первое число без остатка делится на второе.'''
intA = 20
intB = 11

if intA%intB == 0:
	print ('числа делятся без остатка')
else:
	print ('числа не делятся без остатка')


'''15 Дана некоторая строка:

'abcde'
Получите список ее символов:

['a', 'b', 'c', 'd', 'e']'''

stringB = 'abcde'
print(list(stringB))


'''16 Дан список:

[1, 2, 3, 4, 5, 6]
Получите из него следующий срез:

[3, 4, 5]'''

listB = [1,2,3,4,5,6]
print(listB[2:5])



'''17 Дан словарь с датой:

{
	'year' : '2025',
	'month': '12',
	'day'  : '31',
}
Из элементов этого словаря соберите дату в следующем формате:

2025-12-31'''

dictA = {
	'year' : '2025',
	'month': '12',
	'day'  : '31',
}

print(f"{dictA['year']}-{dictA['month']}-{dictA['day']}")


'''18 Выведите в консоль все целые числа от 1 до 100.'''

listC = list(range(1,101))
for i in listC:
	print(i)


'''19 Выведите в консоль все целые числа от -100 до 0.'''
stringC = ""
for i in reversed(range(1, 101)):
	stringC += f"{-i}, "

print(stringC[0:-2])
listD = []
'''20 Выведите в консоль все целые числа от 100 до 1.'''
for i in reversed(listC):
	listD.append(str(i))

print(", ".join(listD))

'''21 Выведите в консоль все четные числа из промежутка от 1 до 100.'''

for i in listC:
	if i%2 == 0:
		print(i)

'''22 Выведите в консоль все числа кратные трем в промежутке от 1 до 100.'''

for i in listC:
	if i%3 == 0:
		print (i)
#второе решение 
listE = [x for x in range(101) if x%3 == 0]
print ("@@@@@@@")
print (listE)

'''23 Дан список:

[1, 2, 3, 4, 5, 6]
Получите из него два последних элемента:

[5, 6]'''

listD = [1, 2, 3, 4, 5, 6]
listE = listD[-2:]
print(listE)


'''24 Дана некоторая строка:

'abcdeabc'
Получите сет ее символов:

{'a', 'b', 'c', 'd', 'e'}'''

stringD = 'abcdeabc'
listForStringD = list(stringD)
print(set(listForStringD))

''' 25 Найдите сумму всех целых чисел от 1 до 100.'''
all_sum = sum(listC)
print(all_sum)

'''26 Найдите сумму всех целых четных чисел в промежутке от 1 до 100.'''
sum_chet = 0
for i in listC:
	if i%2 == 0:
		sum_chet += i

print (sum_chet)

sum_nechet = 0
for i in listC:
	if i % 2 != 0:
		sum_nechet += i

print(sum_nechet)

print(f'контроль: {sum_chet + sum_nechet} = {all_sum}')

'''27 Дан список:

[1, 2, 3, 4, 5, 6]
Получите из него каждый второй элемент:

[1, 3, 5]'''

listF = [1, 2, 3, 4, 5, 6]
print(listF[::2])


'''28 Дан список с числами:

[1, 2, 3, 4, 5]
Найдите сумму элементов этого списка.'''

listD = [1, 2, 3, 4, 5]
print(sum(listD))

'''29 Дан список с числами:

[1, 2, 3, 4, 5]
Найдите сумму квадратов элементов этого списка.'''
sumsqrtD = 0
for i in listF:
	sumsqrtD += i*i
print(sumsqrtD)


'''30 Дан список с числами:

[1, 2, 3, 4, 5]
Найдите сумму квадратных корней элементов этого списка.'''
import math
sum_sqrt = 0
for i in listD:
	sum_sqrt += math.sqrt(i)
print (sum_sqrt)

'''31 Дан список с числами:

[1, 2, -3, 4, -5]
Найдите сумму положительных элементов этого списка.'''
listD = [1, 2, -3, 4, -5]
sumP = 0

for x in range(len(listD)):
	if listD[x] > 0:
		sumP += listD[x]

print(sumP)

'''32 Дан список с числами:

[-1, 2, -3, 4, 5, 11]
Найдите сумму тех элементов этого списка, которые больше нуля и меньше десяти.'''
listD = [-1, 2, -3, 4, 5, 11]
sumP = 0
for i in range(len(listD)):
	if 0 < listD[i] < 10:
		sumP += listD[i]

print(sumP)


'''33 Дана некоторая строка:

'abcde'
Переберите и выведите в консоль по очереди все символы с конца строки.'''

stringD = 'abcde'
for i in reversed(list(stringD)):
	print (i)

'''34 Дан словарь:

{
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
Найдите сумму элементов этого словаря.'''
dictA = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
print(sum(list(dictA.values())))

'''35 дан словарь:

{
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
Найдите сумму квадратов элементов этого словаря.'''
sumpow = 0
valDictA = list(dictA.values())
for i in valDictA:
	sumpow += (i ** 2)

print(sumpow)


'''36 Дана строка:

'abcde'
Получите список букв этой строки.'''
stringE = 'abcde'
print(list(stringE))

'''37 Дано некоторое число:

12345
Получите список цифр этого числа.'''

numberC = 12345
print(list(str(numberC)))


'''38 Дано некоторое число:

12345
Переверните его:

54321
'''
listFromNumberC = list(str(numberC))
new = []
for i in reversed(listFromNumberC):
	new.append(i)
bh = int("".join(new))
print (bh)


'''39 Дано некоторое число:

12345
Найдите сумму цифр этого числа.'''
for i in range(len(listFromNumberC)):
	listFromNumberC[i] = int(listFromNumberC[i])
print(sum(listFromNumberC))

'''40 Дан кортеж с числами:

(1, 2, 3, 4, 5)
Найдите сумму элементов этого кортежа.'''
sumKA = 0
korteshA = (1, 2, 3, 4, 5)
for i in korteshA:
	sumKA += i
print(f'сумма кортежа а равна {sumKA}')


'''41 Дан список с числами:

[1, 2, 3, 4, 5, 6]
Увеличьте каждое число из списка на 10 процентов.'''

listA = [1, 2, 3, 4, 5, 6]

for i in range(len(listA)):
	listA[i] = round(listA[i] * 1.1, 2)

print (listA)


'''42 Дана строка:

'abcdef'
Получите первых три символа этой строки:

'abc'''

stringA  = 'abcdef'
print(stringA[:3])


'''43 Дана строка:

'abcdef'
Получите три последних символа этой строки:

'def'''

print(stringA[-3:])


''' 44 Дан словарь с числами:

{
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
Увеличьте каждое число из словаря в 2 раза:

{
	'a': 2,
	'b': 4,
	'c': 6, 
	'd': 8,
}'''

dictA = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}

for key, val in dictA.items():
	dictA[key] = val * 2

print (dictA)

'''45 Дана строка:

'abcdef'
Получите каждый второй символ этой строки:

'ace'''
print(stringA[::2])

'''46 Дано некоторое число:

12345
Выведите в консоль все его символы с конца.'''

numberA = 12345

strnumA = list(str(numberA))
print(strnumA)
for x in range(len(strnumA)):
	print(strnumA[-x-1])
