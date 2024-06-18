class Fancy:
    def __init__(self):
        self.sequence = []
        self.add = 0
        self.mult = 1
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        # To append, we need to inverse the cumulative operations for this value.
        adjusted_val = (val - self.add) * pow(self.mult, self.MOD - 2, self.MOD) % self.MOD
        self.sequence.append(adjusted_val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.add = self.add * m % self.MOD
        self.mult = self.mult * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        return (self.sequence[idx] * self.mult + self.add) % self.MOD

# Example usage:
fancy = Fancy()
fancy.append(2)      # fancy sequence: [2]
fancy.addAll(3)      # fancy sequence: [2+3] -> [5]
fancy.append(7)      # fancy sequence: [5, 7]
fancy.multAll(2)     # fancy sequence: [5*2, 7*2] -> [10, 14]
print(fancy.getIndex(0))  # return 10
fancy.addAll(3)      # fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10)     # fancy sequence: [13, 17, 10]
fancy.multAll(2)     # fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
print(fancy.getIndex(0))  # return 26
print(fancy.getIndex(1))  # return 34
print(fancy.getIndex(2))  # return 20