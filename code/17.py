class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
            return self.value
        else:
            return self.value

cal = MaxLimitCalculator()

print(cal.add(60))
print(cal.add(30))
print(cal.add(20))
print(cal.add(50))
