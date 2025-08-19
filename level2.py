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

'''Дан список с числами. Подсчитайте количество отрицательных чисел в этом списке.'''

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

'''Дан список с числами. Оставьте в нем только положительные числа.'''

nlistA = []
for i in listA:
	if i > 0: nlistA.append(i)

print(nlistA)

'''Дана строка. Удалите предпоследний символ из этой строки.'''

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
