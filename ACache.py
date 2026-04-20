from Cache import Cache

class ACache(Cache):
    def __init__(self, associativity, blockSize=1):
        super().__init__(blockSize)
        self.associativity = associativity

    def missCollector(self, addressList):
        lineCount = Cache.CAPACITY // self.blockSize

        if self.associativity <= 1:
            return self.runSimulation(addressList, 1)

        if self.associativity >= lineCount:
            return self.runSimulation(addressList, lineCount)

        return self.runSimulation(addressList, self.associativity)