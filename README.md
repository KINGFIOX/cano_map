# cano_map

### get start

#### example

```py
a, b, c, d = sympy.symbols('a,b,c,d')
expr = c | ~b & ~d | ~a & b & d
my_expr = logic_expr(expr)
my_expr.show_cano()
```
