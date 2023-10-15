from FirstImplied import FirstImplied  # 首要蕴含式
from HeapGreater import MinHeap  # 最小加强堆
import numpy as np


class Quine:
    def __init__(self, vars, min_term) -> None:
        self._first_implied_obj = FirstImplied(vars, min_term)
        self._first_implied_arr = self._first_implied_obj.get_implied()
        self._var_num = len(vars)
        self._y_size = 2**self._var_num
        self._x_size = len(self._first_implied_arr)
        self._map = np.zeros((self._x_size, self._y_size))

    pass
