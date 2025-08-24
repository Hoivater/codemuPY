
listA = ['a', 'b', 'c']
listB = [1, 2, 3]

# объединение в кортеж ???
pairs = [x for x in zip(listA, listB)]
print ('@', pairs) #[('a', 1), ('b', 2), ('c', 3)]
print ('@1', pairs[0][1])
# для разъединения:
letter, numbers = zip(*pairs)
print(letter)
print(numbers)

#ARGS KWARGS
def magic(*args, **kwargs):
	print('безымянные аргументы: ', args)
	print('аргументы по ключу: ', kwargs)

magic(1, 2, key="word", key2="word2")

def other_way_magic(x, y, z):
	return x+y+z

x_y_list = [1, 2]
z_dict = {"z" : 3}

assert other_way_magic(*x_y_list, **z_dict) == 6, "1+2+3 должно быть равно 6"

#удвоитель?
def doubler_correct(f):
	def g(*args, **kwargs):
		return 2 * f(*args, **kwargs)
	return g

# g = doubler_correct(2)
# print(g(1, 2))
