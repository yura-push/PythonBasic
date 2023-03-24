class Buffer:
    def __init__(self):
        self.list_num = []

    def add(self, *a):
        for num in a:
            self.list_num.append(num)
            if len(self.list_num) == 5:
                yield sum(self.list_num)
                self.list_num = []

    def get_current_part(self):
        if len(self.list_num) == 5:
            print(sum(self.list_num))
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