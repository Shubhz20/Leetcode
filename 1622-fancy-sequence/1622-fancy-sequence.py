class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.seq = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        inv = pow(self.mul, self.MOD - 2, self.MOD)
        normalized = (val - self.add) % self.MOD
        normalized = (normalized * inv) % self.MOD
        self.seq.append(normalized)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        
        val = self.seq[idx]
        return (val * self.mul + self.add) % self.MOD