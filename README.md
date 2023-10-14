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
