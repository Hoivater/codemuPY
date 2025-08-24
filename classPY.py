class CounterClicker:

	def __init__(self, count = 0):
		self.count = count

	def __repr__(self):
		return f'CounterClicker (count = {self.count})'

	def click(self, num_times = 1):
		self.count += num_times

	def read(self):
		return self.count

	def reset(self):
		self.count = 0

#создание дочернего класса
class noResetCounter(CounterClicker):
	#он унаследовал все методы из родительского класса. переопределение reset:
	def reset(self):
		pass
	#теперь reset ничего не делает

clicker = CounterClicker()

assert clicker.read() == 0, "счетчик должен начинаться со значения 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "счетчик должен иметь значение 2"
clicker.reset()
assert clicker.read() == 0, "счетчик должен иметь значение 0"

