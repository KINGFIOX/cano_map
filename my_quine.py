from PrimeImplied import PrimeImplied  # 首要蕴含式
import heapq
import numpy as np
import sympy


class Quine:
    def __init__(self, vars: list, min_term: list) -> None:
        self._first_implied_obj = PrimeImplied(vars, min_term)
        self._first_implied_arr = self._first_implied_obj.get_implied()
        self._var_num = len(vars)
        self._x = []
        self._first_implied2dig_s()
        self._x_size = len(self._x)
        # self._x_size = len(self._first_implied_arr)
        # self._map = np.zeros((self._x_size, self._y_size))

    def _first_implied2dig_single(self, text: str) -> list:
        convertor = ImpliedMintermGenerator(text)
        return convertor.get_minterms()

    def _first_implied2dig_s(self) -> None:
        for i in self._first_implied_arr:
            arr = self._first_implied2dig_single(i)
            self._x.append(arr)

    # test
    def test_digs(self):
        print(self._x)
        pass


class ImpliedMintermGenerator:
    def __init__(self, text: str) -> None:
        self._minterms = []
        self._generate_minterms(text)
        self._min_terms_dig = []
        self._bin2num_s()

    def _generate_minterms(self, input_str):
        def backtrack(path, remaining_str):
            if not remaining_str:
                # Base case: Add the current path to the minterms list
                self._minterms.append(path)
                return

            current_char = remaining_str[0]

            if current_char == "1":
                backtrack(path + "1", remaining_str[1:])
            elif current_char == "0":
                backtrack(path + "0", remaining_str[1:])
            elif current_char == "-":
                # Branch for don't-care values
                backtrack(path + "1", remaining_str[1:])
                backtrack(path + "0", remaining_str[1:])

        backtrack("", input_str)

    def _bin2num_single(self, text: str):
        return int(text, 2)

    def _bin2num_s(self):
        for i in self._minterms:
            temp = self._bin2num_single(i)
            self._min_terms_dig.append(temp)

    def get_minterms(self):
        print(self._minterms)
        print(self._min_terms_dig)
        return self._min_terms_dig


if __name__ == "__main__":
    arr = sympy.symbols("a,b,c,d")
    min_term = [0]
    q = Quine(arr, min_term)
    # q.test_digs()
    print("hello world")
