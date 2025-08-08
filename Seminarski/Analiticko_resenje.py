from sympy import *
from sympy.abc import t
from sympy.abc import g
from sympy.abc import u

v = Function('v')
dsolve(Derivative(v(t),t)+g+g/u*v(t),v(t))