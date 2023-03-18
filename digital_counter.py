class Counter:
    def __init__(self, current_value: int, min_value: int, max_value: int):
        self.current_value = current_value
        self.min_value = min_value
        self.max_value = max_value

    def increment(self):
        self.current_value += 1

    def get_current_value(self):
        return self.current_value


my_counter = Counter(1, 0, 100)
my_counter.increment()

print(my_counter.get_current_value())