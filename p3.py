from z3 import *

x = Real("x")
p = Int("p")
q = Int("q")
y = Real("y")
m = Int("m")
n = Int("n")
s = Solver()

s.add(q * x == p)
s.add(n * y == m)
s.add(ForAll([x], Exists([y], And(2 * y > 3 * x, 4 * y < (8 * x + 10)))))
print(s.check())
