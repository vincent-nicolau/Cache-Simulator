from Cache import Cache

class BCache(Cache):
    def __init__(self, blockSize=1):
        super().__init__(blockSize)

    def missCollector(self, addressList):
        return self.runSimulation(addressList, 1)