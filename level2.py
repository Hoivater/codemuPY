'''Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.'''

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


'''Дана некоторая строка. Найдите позицию первого нуля в строке.'''
stringA = 'gуауцаhttpdw:0//такаявотпра вильная'

listSearch = stringA.split('0')
if(len(listSearch) > 1):
	print(len(listSearch[0]) + 1)
else:
	print ('символа 0 в строке не встречается')

'''Дан список. Удалите из него элементы с заданным значением.'''
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

'''Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти.'''
listB = list(range(10, 1001))
nListB = []
for i in listB:
	blist = list(str(i))
	if (int(blist[0]) + int(blist[1])) == 5:
		nListB.append(i)


print (nListB)


'''Дана некоторая строка:

'abcdeabc'
Очистите ее от дублей символов:

'abcde'''

listA = 'abcdeabc'
dictA = {}
setA = set(list(listA))
lsetA = list(setA)

#оставить строку как она есть???
print(listA)
nstr = ''
for i in range(len(setA)):
	dictA[lsetA[i]] = 0
for k in listA:
	dictA[k] += 1

print (dictA)

for lA in listA:
	for keyA, valueA in dictA.items():
		if keyA == lA and valueA > 0:
			nstr += lA
			dictA[keyA] -= 1


print (dictA)

print(nstr)
