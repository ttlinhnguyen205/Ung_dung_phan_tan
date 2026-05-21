import xmlrpc.client


proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("Calling remote procedures from XML-RPC Server...")

result_add = proxy.add(10, 5)
result_subtract = proxy.subtract(10, 5)
result_multiply = proxy.multiply(10, 5)
result_divide = proxy.divide(10, 5)

print("10 + 5 =", result_add)
print("10 - 5 =", result_subtract)
print("10 * 5 =", result_multiply)
print("10 / 5 =", result_divide)