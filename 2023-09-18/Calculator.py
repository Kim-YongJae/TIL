class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, value):
        self.value += value
        return self

    def subtract(self, value):
        self.value -= value
        return self

    def divide(self, value):
        if value == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        self.value /= value
        return self

    def end(self):
        return self.value