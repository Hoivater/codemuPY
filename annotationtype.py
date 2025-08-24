from typing import Union
from typing import List
from typing import Optional
from typing import Dict
from typing import Iterable
from typing import Tuple
from typing import Callable

def summa(a: int, b: int) -> int:
	return a+b

print( summa(10, 1))


#функиця принимает целое число, а второй аргумент может быть str, int, float или bool
def ugly_function(value: int,
	operation: Union[str, int, float, bool]) -> int:
	return 1


#если необходимо указать тип: список, или список из чисел с плавающей точкой

def total(xs: list) -> float:
	return 1.1

def total(xs:List[float]) -> float:
	return 1.1

#переменные:
x: int = 14313
value: List[int] = []
best_so_far: Optional[float] = None #Допустимо иметь тип float или None

#словари:
counts: Dict[str, int] = {'data':1, 'science':2} #ключ - строка, значение - целое число

#списки и генераторы: итерируемые объекты:
evens: Iterable[int] = (x for x in range(10) if x%2==0)

#кортежам необходимо обозначать каждый элемент

triple: Tuple[int, float, int] = (10, 2.1, 11)


#функция??????????

def twice(repeater: Callable[[str, int], str], s: str) -> str:
	return repeater(s, 2)


def comma_repeater (s: str, n: int) -> str:
	n_copies = [s for _ in range(n)]
	return ', '.join(n_copies)

	assert twice(comma_repeater, "подсказки типов")