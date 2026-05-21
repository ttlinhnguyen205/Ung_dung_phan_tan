from xmlrpc.server import SimpleXMLRPCServer


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


server = SimpleXMLRPCServer(("localhost", 8000))
print("XML-RPC Server is running on port 8000...")

server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

server.serve_forever()