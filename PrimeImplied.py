import sympy
import copy


class PrimeImplied:
    def __init__(self, min_term: list, vars: list) -> None:
        self.min_term: list = min_term
        self._vars: list = vars
        self._var_num: int = len(vars)
        self._implied_before: list[list] = self._count_s_min_term()  # 前面的列
        self._implied_cur: list[list] = [[]]  # 当前列的
        self._implied: list = []  # 首要蕴含项
        self._until_cur()

    def _one_different(self, str1: str, str2: str):
        # 返回值是(bool, str), 第一个是只有一个不同, 第二个是, 返回带有-
        if len(str1) == None or len(str2) == None:
            return (False, "")
        count_different = 0
        str_different = ""
        for i, j in zip(str1, str2):
            if not i == j:
                count_different += 1
        if count_different == 1:
            for i, j in zip(str1, str2):
                if i == j:
                    # 相同
                    str_different = str_different + i
                else:
                    # 如果不相同的话, 其中有一个出现了-, 那么就不行
                    if i == "-" or j == "-":
                        return False, ""
                    else:
                        str_different = str_different + "-"
        else:
            return (False, "")
        return (True, str_different)

    def _count_s_min_term(self):
        # 装进 对应的桶里
        text_arr = [bin(i)[2:].zfill(self._var_num) for i in self.min_term]
        arr = self._count_s(text_arr)
        return arr

    def _count_s(self, arr: list):
        # arr是一维数组, 装进对应的桶里
        # 返回两个值(bool, list[list])
        if len(arr) == 0:
            return [[]]
        temp: list[list] = [[]]
        max_count = max([i.count("1") for i in arr])
        for i in range(max_count):
            temp.append(list())
        for i in arr:
            num_b_i = i.count("1")
            temp[num_b_i].append(i)
        return temp

    def _have_cur(self) -> bool:
        # 由before得到cur, 并且加入首要蕴含项
        arr: list = []
        mark_arr: list[list] = copy.deepcopy(self._implied_before)
        for i in range(len(self._implied_before) - 1):
            # i表示, 含有i个1
            for j in range(len(self._implied_before[i])):
                for k in range(len(self._implied_before[i + 1])):
                    is_one, one_text = self._one_different(
                        self._implied_before[i][j], self._implied_before[i + 1][k]
                    )
                    if is_one:
                        # 标记
                        arr.append(one_text)
                        mark_arr[i][j] = 1
                        mark_arr[i + 1][k] = 1

        new_arr = list(set(arr))
        for i in range(len(mark_arr)):
            for j in range(len(mark_arr[i])):
                # 如果没有被标记, 那么就加入首要蕴含项中
                if not mark_arr[i][j] == 1:
                    self._implied.append(mark_arr[i][j])
        self._implied_cur = self._count_s(new_arr)
        # print(new_arr)
        if len(new_arr) == 0:
            return False
        else:
            return True

    def _until_cur(self):
        # 先进行第一轮
        right = self._have_cur()
        while right:
            self._implied_before = copy.deepcopy(self._implied_cur)
            right = self._have_cur()
        # 结束的时候, 说明cur没东西了

    # test start
    def get_implied(self):
        # right = self._have_cur()
        # print("self._implied_before: ", self._implied_before)
        # print("self._implied_cur: ", self._implied_cur)
        # print(right)
        return self._implied


if __name__ == "__main__":
    arr = sympy.symbols("a,b,c,d")
    min_term = []  # 只有最小项
    for i in range(0, 2 ** len(arr)):
        min_term.append(i)
        q = PrimeImplied(min_term, arr)
        implied_arr = q.get_implied()
        print(implied_arr)
    pass
