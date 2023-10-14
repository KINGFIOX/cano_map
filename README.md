# cano_map

### Getting Started

#### Example

```py
from cano import logic_expr
import sympy
a, b, c, d = sympy.symbols('a,b,c,d')
expr = c | ~b & ~d | ~a & b & d
my_expr = logic_expr(expr)
my_expr.show_cano()
```
and you could see the output

```output
cd     00     01    11    10
ab                          
00   True  False  True  True
01  False   True  True  True
11  False  False  True  True
10   True  False  True  True
```