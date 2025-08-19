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

