'''1 Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.'''

listA = [
	'/строка один',
	'ст будет два',
	'строкhttp://вооочень',
	'http://такаявотпра вильная',
	'еще обычная http://',
	'http:/просто строка с од',
	'Еще одна',
	'http://',
	'hhttp://'
]
listSearch = []
for i in range(len(listA)):
	listTest = listA[i].split("http://")
	if len(listTest) > 1 and listTest[0] == "":
		listSearch.append(listA[i])

print(f'Заданный список: {listA}, \n\n\nНайденные строки с http://: {listSearch}')


'''2 Дана некоторая строка. Найдите позицию первого нуля в строке.'''
stringA = 'gуауцаhttpdw:0//такаявотпра вильная'

listSearch = stringA.split('0')
if(len(listSearch) > 1):
	print(len(listSearch[0]) + 1)
else:
	print ('символа 0 в строке не встречается')

'''3 Дан список. Удалите из него элементы с заданным значением.'''
deleteSymbol = ['h', 'd', '/']

newString = ''
count = 0
for i in stringA:
	for j in deleteSymbol:
		if i == j:
			count += 1
	if(count == 0):
		newString += i
	else:
		count = 0


print ('@' + newString)

''' 4 Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти.'''
listB = list(range(10, 1001))
nListB = []
for i in listB:
	blist = list(str(i))
	if (int(blist[0]) + int(blist[1])) == 5:
		nListB.append(i)


print (nListB)


''' 5 Дана некоторая строка:

'abcdeabc'
Очистите ее от дублей символов:

'abcde'''

stringA = 'abdsqqacdeabc'
n_listA = []
#оставить строку как она есть???
print(stringA)

lisAFromStr = list(stringA)

for i in lisAFromStr:
	if i not in n_listA:
		n_listA.append(i)

print (n_listA)

'''6 Дан список с числами. Подсчитайте количество отрицательных чисел в этом списке.'''

listA = [
	10, 
	2,
	3,
	-5,
	-8,
	3,
	12
]
count = 0
for i in listA:
	if i < 0:
		count += 1

print (count)

'''7 Дан список с числами. Оставьте в нем только положительные числа.'''

nlistA = []
for i in listA:
	if i > 0: nlistA.append(i)

print(nlistA)

'''8 Дана строка. Удалите предпоследний символ из этой строки.'''

#first solution

stringA = 'abdsqqacdeabc'
nstringA = ''
for i in range(len(stringA)):
	if i != len(stringA)-2:
		nstringA += stringA[i]

print(stringA)
print(nstringA)

#second solution

nstringA2 = stringA[0:-2] + stringA[-1:]


print(stringA)
print(nstringA2)

'''9 Дан список со строками. Оставьте в этом списке только те строки, которые заканчиваются на .html.'''

listA = [
	'/строка один',
	'ст будет два',
	'строкhttp://вооочень.html',
	'http://такаявотпра вильная',
	'еще обычная http://',
	'http:/просто строка с од.html',
	'Еще одна',
	'http://',
	'hhttp://'
]
nListA = []
for i in listA:
	listI = i.split(".")
	if len(listI) > 1 and listI[-1] == 'html':
		nListA.append(i)

print (nListA)

'''10 Дан список с дробями:

[1.456, 2.125, 3.32, 4.1, 5.34]
Округлите эти дроби до одного знака в дробной части.'''

listNum = [1.456, 2.125, 3.32, 4.1, 5.34]
for i in range(len(listNum)):
	listNum[i] = round(listNum[i], 1)

print (listNum)

'''11 Дан словарь:

{
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
Получите список его значений:

[1, 2, 3, 4]'''
dictA = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4
}
print (list(dictA.values()))


'''12 Даны два слова. Проверьте, что последняя буква первого слова совпадает с первой буквой второго слова.'''

wordA = 'буквой'
wordB = 'йслова'

if wordA[-1] == wordB[0]: print ("совпадают")
else: print("Не совпадают")

'''13 Дана некоторая строка. Найдите позицию третьего нуля в строке.'''
stringA = "dq0eg0wth40efwgrw0"
count = 0
lStringA = stringA.split('0')
if len(lStringA) >= 4:
	for x in range(3):
		count += len(lStringA[x]) + 1

print(stringA)
print(f'третий 0 - {count} по счету')

'''14 Даны числа, разделенные запятыми:

'12,34,56'
Найдите сумму этих чисел.'''
stringM = '12,34,56'
listM = stringM.split(',')
count = 0
stringCount = ''
for i in listM:
	count += int(i)
	stringCount += f"{i} + "
print(f'{stringCount} = {count}')


'''15 Дана дата в следующем формате:

'2025-12-31'
Преобразуйте эту дату в следующий словарь:

{
	'year' : '2025',
	'month': '12',
	'day'  : '31',
}'''

strDate = '2025-12-31'
listDateValue = strDate.split('-')
listDateKey = ['year', 'month', 'day']
dictDate = dict(zip(listDateKey, listDateValue))

print (dictDate)


'''16 Дан словарь:

{
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
Получите сет его значений:

{1, 2, 3, 4}'''

dictA = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4
}

setdictA = set(list(dictA.values()))
print (setdictA)

'''17 Дана некоторая строка с буквами и цифрами. Получите позицию первой цифры в этой строке.'''

stringS = 'Да2на н343еко2т4ора4я с44т5рока.'
numericN = -1
for j in range(len(stringS)):
	if numericN == -1:
		for i in range(10):
			if stringS[j] == str(i):
				numericN = j
				break
print(f'Позиция: {numericN}, то есть: {stringS[numericN]}')

'''18 Дано число. Выведите в консоль количество четных цифр в этом числе.'''
numberD = '24314352'
listD = list(str(numberD))
try:
	listAevel = [x for x in listD if int(x)%2 == 0]
	print (len(listAevel))
except ValueError:
	print('не преобразовать к числу!')

'''19 Дан словарь:

{
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
Получите список его ключей:

['a', 'b', 'c', 'd']'''

dictA = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4
}
print (dictA.keys())


'''20 Дана некоторая строка:

'abcde'
Переведите в верхний регистр все нечетные буквы этой строки. В нашем случае должно получится следующее:

'AbCdE'''
stringA = 'abcde'
liststrA = list(stringA)
for i in range(len(liststrA)):
	if i % 2 == 0:
		liststrA[i] = liststrA[i].upper()
nstringA = "".join(liststrA)
print(nstringA)

'''21 Дана некоторая строка со словами:

'aaa bbb ccc'
Сделайте заглавным первый символ каждого слова в этой строке. В нашем случае должно получится следующее:

'Aaa Bbb Ccc'''

stringA = 'Сделайте заглавным первый символ'
listA = stringA.split(' ')
listkey = list(range(len(listA)))
dictA = dict(zip(listkey, listA))
for key, value in dictA.items():
	listV = list(value)
	listV[0] = listV[0].upper()
	strV = ''.join(listV)
	dictA[key] = strV

valueA = list(dictA.values())

print (stringA)
print(" ".join(valueA))

# print (dictA)

'''22 Дана дата в следующем формате:

'2025-12-31'
Преобразуйте эту дату в следующий кортеж:

('31', '12', '2025')'''
dates = '2025-12-31'
listD = dates.split('-')
print(tuple(listD))


'''23 Дана некоторая строка, например, вот такая:

'023m0df0dfg0'
Получите сет позиций всех нулей в этой в строке.'''

stringG = '023m0df0dfg0'
list0 = []
for i in range(len(stringG)):
	if stringG[i] == '0':
		list0.append(i)

print(set(list0))

'''24  Дана некоторая строка:

'abcdefg'
Удалите из этой строки каждый третий символ. В нашем случае должно получится следующее:

'abdeg'''

stringA = 'abcdefg'
listA  = list(stringA)

resultNumA = [x for x in range(len(stringA)) if x%3==0]
resultA = ""
for i in range(len(stringA)):
	if i%3!=0:
		resultA += stringA[i]
print (stringA)
print (resultA)


'''25 Дан некоторый список, например, вот такой:

[1, 2, 3, 4, 5, 6]
Поделите сумму элементов, стоящих на четных позициях, на сумму элементов, стоящих на нечетных позициях. '''
listA = [1, 2, 3, 4, 5, 6]
sum_even = 0
sum_odd = 0
for i in range(len(listA)):
	if i % 2 == 0:
		sum_even += listA[i]
	else:
		sum_odd += listA[i]
print(sum_even/sum_odd)





'''26 Дана дата в следующем формате:

['2025', '12', '31']
Преобразуйте эту дату в следующий кортеж:

('31', '12', '2025') '''
listA = ['2025', '12', '31']

listB = [listA[2], listA[1], listA[0]]

print(tuple(listB))


'''27 Дана некоторая строка с буквами и цифрами. Получите список позиций всех цифр из этой строки.'''

stringA = 'ef2rgegr42gr42tgr43tr3rg42f'
print (stringA)
listA = list(stringA)
listNum = []
for i in range(len(listA)):
	if listA[i].isdigit():
		listNum.append(i)

print(f'{listNum} - список позиций цифр')

	
'''28 Дана некоторая строка:

'AbCdE'
Смените регистр букв этой строки на противоположный. В нашем случае должно получится следующее:

aBcDe'''
stringA = 'AbCdE'
listA = list(stringA)
print (f'{stringA} - исходная строка')
for i in range(len(listA)):
	if listA[i].islower():
		listA[i] = listA[i].upper()
	else:
		listA[i] = listA[i].lower()
print ("".join(listA))


'''29 Дан некоторый список с числами, например, вот такой:

[1, 2, 3, 4, 5, 6]
Слейте пары элементов вместе:

[12, 34, 56]'''

listA = [1, 2, 3, 4, 5, 6]
nlistA = []
for i in range(int(len(listA)/2)):
	nlistA.append(f'{listA[2*i]}{listA[2*i+1]}')

print(listA, "\n", nlistA)

'''30 Дана некоторая строка со словами:

'aaa bbb ccc eee fff'
Сделайте заглавным первый символ каждого второго слова в этой строке. В нашем случае должно получится следующее:

'aaa Bbb ccc Eee fff'''
stringA = 'aaa bbb ccc eee fff'
listA = stringA.split(' ')
for i in range(len(listA)):
	if i%2 != 0:
		listA[i] = f'{listA[i][0].upper()}{listA[i][1:]}'

print(" ".join(listA))


'''31 '''


'''32 '''


'''33 '''



