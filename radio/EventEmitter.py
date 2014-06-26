class EventEmitter:
    def __init__(self):
        self.observers = {}

    def add(self, event_name, observer):
        if event_name not in self.observers:
            self.observers[event_name] = []
        self.observers[event_name].append(observer)

    def emit(self, event_name):
        if event_name in self.observers:
            for observer in self.observers[event_name]:
                observer()