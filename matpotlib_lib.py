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
grades = [83, 95, 91,87,70,0,85,82,100,67,73,77]
#сгруппировать оценки подецильно, но разместить 100 вместе с отметками 90 и выше
histogram = Counter(min(grade // 10*10, 90) for grade in grades)
print(grades)
print(histogram)