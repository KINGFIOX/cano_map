import pandas as pd
import sympy


class k_map:
    """
    输入变量是ABCDE
    输入的真值表顺序是EDCBA
    x: ED
    y: CBA
    实例：truth_map = [true, true, false ...]
    """

    def __init__(self, var, truth_map: list):
        self.variables = var
        self.truth_map = truth_map
        self.var_nums = len(self.variables)
        self.x = self.var_nums // 2
        self.y = self.var_nums - self.x
        self.rows = 2 ** self.x
        self.cols = 2 ** self.y
        self.all = 2 ** self.var_nums
        # 注册，将十进制转化为格雷码
        self.c_bin2gray = k_map._bin2gray(self.cols)
        self.r_bin2gray = k_map._bin2gray(self.rows)
        self.df = self._create_map()
        self._all_marks()
        self.x_label: str = ""
        self.y_label: str = ""
        self._table_name()

    def _table_name(self):
        x_label_symbol = self.variables[:self.x]
        y_label_symbol = self.variables[self.x:]
        self.x_label = ''.join([str(i) for i in x_label_symbol])
        self.y_label = ''.join([str(i) for i in y_label_symbol])
        self.df.index.name = self.x_label
        self.df.columns.name = self.y_label

    @staticmethod
    def _bin2gray(n: int):
        # 将十进制转化为格雷码
        length = len(bin(n)[2:]) - 1

        def inner(dig) -> str:
            arr = bin(dig)[2:]
            arr = int(arr, 2)
            return bin(arr ^ (arr >> 1))[2:].zfill(length)

        return inner

    def _create_map(self):
        # 创建一个空的表
        c_index = [i for i in range(self.cols)]
        c_index = [self.c_bin2gray(i) for i in c_index]
        r_index = [i for i in range(self.rows)]
        r_index = [self.r_bin2gray(i) for i in r_index]
        # x是行的变量数，y是列的变量数
        return pd.DataFrame(0, index=r_index, columns=c_index)

    def _mark(self, x: str, y: str, value: bool):
        # x是ED, y是CBA
        self.df.at[x, y] = value

    def _divide_x_y(self, index: int) -> (str, str):
        # 将index拆分成x和y的格雷码
        index_bin = bin(index)[2:].zfill(self.var_nums)
        x_index_bin_str = index_bin[:self.x]
        y_index_bin_str = index_bin[self.x:]
        return x_index_bin_str, y_index_bin_str

    def _all_marks(self):
        for index, value in zip(range(len(self.truth_map)), self.truth_map):
            x_index, y_index = self._divide_x_y(index)
            self._mark(x_index, y_index, value)

    def show_cano(self):
        # TODO
        print(self.df)


class logic_expr:
    def __init__(self, expression):
        # 传入逻辑表达式
        self.expr = expression
        self.parsed_expr = sympy.parse_expr(str(self.expr))
        # 维护变量列表，但是e,d,c,b,a
        self.variables = list(self.parsed_expr.free_symbols)
        self.variables = sorted(self.variables, key=lambda a: str(a))
        # 维护真值表
        self.df = None
        # 真值列表
        self.truth_table = []
        # 注册
        self._wrap_truth_table()
        # 维护卡诺图
        self.m_map: k_map = None
        self._wrap_k_map()

    def _wrap_truth_table(self) -> None:
        # 维护一个真值表，原本的真值表是不可逆迭代
        temp = []
        for binary, val in sympy.logic.boolalg.truth_table(self.expr, self.variables):
            temp.append((binary, val))
            self.truth_table.append(val)
        self.df = pd.DataFrame(temp, columns=["binary", "value"])

    def _wrap_k_map(self) -> None:
        self.m_map = k_map(self.variables, self.truth_table)

    def update_expr(self, new_expr):
        # 更新表达式
        self.expr = new_expr
        self.parsed_expr = sympy.parse_expr(str(self.expr))
        self.variables = list(self.parsed_expr.free_symbols)
        self._wrap_truth_table()
        self._wrap_k_map()

    def show_cano(self):
        # TODO
        self.m_map.show_cano()


if __name__ == "__main__":
    # 运行程序可以改这里
    a, b, c, d = sympy.symbols('a,b,c,d')
    expr = c | ~b & ~d | ~a & b & d
    my_expr = logic_expr(expr)
    my_expr.show_cano()
