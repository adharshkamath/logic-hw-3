from z3 import *

l1 = Real("l1")
l2 = Real("l2")
u1 = Real("u1")
u2 = Real("u2")
w = Real("w")
z = Real("z")

goal = Goal()
goal.add(
    ForAll(
        [z],
        Implies(
            And(l1 < z, z < u1, l2 < z, z < u2),
            Exists([w], And(l1 < w, w < u1, l2 < w, w < u2, w != z)),
        ),
    )
)

tactic = Tactic("qe")
result = tactic(goal)
print(result)
