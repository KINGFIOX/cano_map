from PrimeImplied import PrimeImplied  # 首要蕴含式
import heapq
import numpy as np


class Quine:
    def __init__(self, vars, min_term) -> None:
        self._first_implied_obj = PrimeImplied(vars, min_term)
        self._first_implied_arr = self._first_implied_obj.get_implied()
        self._var_num = len(vars)
        self._y_size = 2**self._var_num
        self._x_size = len(self._first_implied_arr)
        self._map = np.zeros((self._x_size, self._y_size))

    def _implied2minterm(self):
        m_path = ""
        m_result = []

        def min_term_util(rest_str: str):
            if len(rest_str) == 0:
                # base case
                m_result.append(m_path)
                return
            cur_char = rest_str[0]
            if cur_char == "1":
                m_path = m_path + "1"
                min_term_util(rest_str[1:])
            if cur_char == "0":
                m_path = m_path + "0"
                min_term_util(rest_str[1:])
            else:
                # cur_char = "-"
                m_path = m_path + "1"
                min_term_util(rest_str[1:])
                m_path = m_path[:-1]
                m_path = m_path + "0"
                min_term_util(rest_str[1:])


class implied2minterm:
    def __init__(self, text) -> None:
        self._m_path = ""
        self._m_result = []
        self._min_term_util(text)

    def _min_term_util(self, rest_str: str):
        if len(rest_str) == 0:
            # base case
            self._m_result.append(self._m_path)
            return

        cur_char = rest_str[0]
        if cur_char == "1":
            self._m_path = self._m_path + "1"
            self._min_term_util(rest_str[1:])
        if cur_char == "0":
            self._m_path = self._m_path + "0"
            self._min_term_util(rest_str[1:])
        if cur_char == "-":
            m_path = self._m_path + "1"
            self._min_term_util(rest_str[1:])
            m_path = m_path[:-1]
            m_path = m_path + "0"
            self._min_term_util(rest_str[1:])

    def get_result(self):
        return self._m_result


if __name__ == "__main__":
    str_arr = "11--"
    arr = implied2minterm(str_arr)
    print(arr.get_result())
    print(str_arr)
    str_arr = str_arr[:-1]
    print(str_arr)
    print("hello world")
