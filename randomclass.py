import random

random.seed(10) #будем получать одинаковые результаты

#четыре равномерные случайные величины
four_uniform_randoms = [random.random() for _ in range(4)]
print (four_uniform_randoms)

random.randrange(10) #случайный выбор из range(10)
random.randrange(3,6) # из range(10)

#перетасовка в случайном порядке:
listA = list(range(10))
random.shuffle(listA)
print (listA)

#случайный выбор из списка:
my_best_friends = random.choice(["Alice", "Bob", "Charlie"])
print (my_best_friends)

#выборка из списка без дублей:
lottery_numbers = list(range(60))
winning_numbers = random.sample(lottery_numbers, 6)
print (winning_numbers)
print (lottery_numbers)

#возможная реализация выборки из списка с дублями:
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print (four_with_replacement)
