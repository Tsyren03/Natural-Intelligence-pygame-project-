class CounterManager:
    def __init__(self):
        self.counters = {"human": 0, "non_human": 0, "deviator": 0}

    def increment_counter(self, counter_type):
        if counter_type in self.counters:
            self.counters[counter_type] += 1

    def get_counter(self, counter_type):
        return self.counters.get(counter_type, 0)
