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

'''Дана некоторая строка. Найдите позицию третьего нуля в строке.'''
stringA = "dq0eg0wth40efwgrw0"
count = 0
lStringA = stringA.split('0')
if len(lStringA) >= 4:
	for x in range(3):
		count += len(lStringA[x]) + 1

print(stringA)
print(f'третий 0 - {count} по счету')