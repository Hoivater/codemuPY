from matplotlib import pyplot as plt
#LINEAGE GRAPHICS
'''years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#создать линейную диаграмму: годы по оси x, ВВП по оси y
plt.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')

#добавить название диаграммы:
plt.title('Номинальный ВВП')

#Добавить подпись к оси y
plt.ylabel("Млрд $")

plt.show()

#СТОЛБЧАТЫЕ ГРАФИКИ
movies = ["Энни Холл", "Бен-Гур", "Касабланка", "Ганди", "Вестсайдская история"]
num_oscars = [5, 11, 3, 8, 10]

#Построить столбцы с левыми координатами X - xs, и высотами [num_oscars]

plt.bar(range(len(movies)), num_oscars)
plt.title("Мои любимые фильмы")
#метка на оси y:
plt.ylabel("Количество наград")
#пометить ось x названием фильмов в центре каждого столбца 
plt.xticks(range(len(movies)), movies)
plt.show()
'''
#построение гистограмм сгруппированных числовых значений
from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77]
#сгруппировать оценки подецильно, но разместить 100 вместе с отметками 90 и выше
histogram = Counter(min(grade // 10*10, 90) for grade in grades)

#аналог строки 35. Пиздец
# histogram_f = []
# for grade in grades:
# 	new = grade // 10 * 10
# 	if new > 90: new = 90
# 	histogram_f.append(new)
# hist_f = Counter(histogram_f)

plt.bar([x+5 for x in histogram.keys()], #сдвиг каждого из столбцов на 5 единиц влево
	list(histogram.values()), #высота столбца
	10) #ширина столбца

plt.axis([-5, 105, 0, 5]) #ось x [-5 : 105] ось y [0 : 5]
plt.xticks([10*x for x in range(11)])#метки по оси x: 0, 10, 20... 100
plt.xlabel('дециль')
plt.ylabel('число студентов')
plt.title('распределение оценок за экзамен №1')
plt.show()

