from util.event import Event

class GenericInterface:

    def event(self, name):
        if name not in self.events:
            raise Exception("Accessing unknown event: {}".format(name))
        return self.events[name]

    def __init__(self, options):
        # Events: are binding sites for other classes sharing GenericInterface.
        # One class may in this way share its status with another class.
        events = getattr(options, "events", [])
        self.events = {}
        for each in events:
            self.events[each] = Event()
            self.events[each].append((lambda a,b: lambda *c: console.log(
                "Event [{}] triggered by {}".format(a,b), c
            ))(each, self.__class__.__name__))
