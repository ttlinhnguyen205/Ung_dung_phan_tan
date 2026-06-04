from Pyro5.api import expose, Daemon, locate_ns

@expose
class Calculator:
    def add(self, a, b):
        return a + b

daemon = Daemon()
ns = locate_ns()

uri = daemon.register(Calculator)
ns.register("calculator", uri)

print("Server started")
daemon.requestLoop()