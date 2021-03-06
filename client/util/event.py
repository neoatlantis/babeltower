class Event:

    def __init__(self):
        self.__list = []

    def append(self, what):
        self.__list.append(what)

    def trigger(self, *args):
        self.__call__(*args)

    def __call__(self, *args):
        build = lambda func, args: lambda: func(*args)
        for func in self.__list:
            l = build(func, args)
            setTimeout(l, 1)
