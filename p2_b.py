from z3 import *

la = Real("la")
ua = Real("ua")
lb = Real("lb")
ub = Real("ub")
lc = Real("lc")
uc = Real("uc")
ld = Real("ld")
ud = Real("ud")
z = Real("z")
z1 = Real("z1")
z2 = Real("z2")
z3 = Real("z3")
z4 = Real("z4")
z5 = Real("z5")

s = Solver()
s.add(
    And(
        Exists([z], And(la < z, z < ua, lb < z, z < ub)),
        Exists([z1], And(la < z1, z1 < ua, lc < z1, z1 < uc)),
        Exists([z2], And(ld < z2, z2 < ud, lb < z2, z2 < ub)),
        Exists([z3], And(ld < z3, z3 < ud, lc < z3, z3 < uc)),
        Not(Exists([z4], And(la < z4, z4 < ua, ld < z4, z4 < ud))),
        Not(Exists([z5], And(lb < z5, z5 < ub, lc < z5, z5 < uc))),
    )
)
print(s.check())
