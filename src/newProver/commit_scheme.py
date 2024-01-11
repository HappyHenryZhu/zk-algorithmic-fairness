from py_ecc.bn128 import bn128_curve, bn128_pairing
from py_ecc.fields import (
    bn128_FQ as FQ,
    bn128_FQ2 as FQ2,
    bn128_FQ12 as FQ12,
    bn128_FQP as FQP,
)
from experiment_dt import KZGBatchCommitment, PrimeField


order = bn128_curve.curve_order
field = PrimeField(order)
size = 4
srsX = 12
srsAlpha = 10
n = 2000
g_max = n*6
cmScheme = KZGBatchCommitment(n, srsX, srsAlpha, field)

poly_dict = {1:2, 3:5, 5:-2}

print(field.sparse(poly_dict))



r = [[1,2,3],1]

c = cmScheme.commita([r[0]], [r[1]], g_max)
o = cmScheme.openC(c, [[4]], [r[0]], [r[1]], g_max)
# multiple polinomials single point:
# o = cmScheme.openC([c, c, c], [[4],[4],[4]], [r[0], r[0], r[0]], [r[1], r[1], r[1]], 0)
v = cmScheme.verify(c, *o)

print(v)