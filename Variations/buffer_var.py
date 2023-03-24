class Buffer:
    def __init__(self):
        self.buffer = []
        self.sum_of_5 = 0

    def add(self, *a):
        for num in a:
            self.buffer.append(num)
            if len(self.buffer) == 5:
                self.sum_of_5 = sum(self.buffer[:5])
                self.buffer = self.buffer[5:]

    def get_current_part(self):
        if len(self.buffer) == 5:
            print(self.sum_of_5)
        else:
            print(0)


if __name__ == "__main__":
    buf = Buffer()
    buf.add(5, 5, 6)
    buf.get_current_part()
    buf.add(1, 11, 5, 8, 6, 4)
    buf.get_current_part()
    buf.add(1, 2)
    buf.get_current_part()
    buf.add(1, 2, 3, 4)
    buf.get_current_part()
    buf.add(15, 24, 45, 89)
    buf.get_current_part()
