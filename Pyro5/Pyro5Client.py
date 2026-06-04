from Pyro5.api import Proxy

calc = Proxy("PYRONAME:calculator")

result = calc.add(10, 5)

print("10 + 5 =", result)