from pathlib import Path
from ACache import ACache
from BCache import BCache

class Manager:
    def simulateCache(self, cacheChoice, parameter, addressList):
        if cacheChoice == "A":
            cache = ACache(parameter)
        else:
            cache = BCache(parameter)

        return cache.missCollector(addressList)

    def getFilePath(self):
        while True:
            try:
                filePath = input("Trace file: ")
                Path(filePath).read_text()  # test read
                return filePath
            except:
                print("Invalid file path.")

    def getCacheChoice(self):
        while True:
            choice = input("Cache type? (A, B): ").strip().upper()
            if choice in ["A", "B"]:
                return choice

    def getParameter(self, cacheChoice):
        while True:
            if cacheChoice == "A":
                param = input("Associativity? (1, 32): ").strip()
                if param in ["1", "32"]:
                    return int(param)
            else:
                param = input("Block size? (1, 4): ").strip()
                if param in ["1", "4"]:
                    return int(param)

def loadTrace(filePath):
    lines = Path(filePath).read_text().splitlines()
    addressList = []

    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            addressList.append(int(line))

    return addressList

def main():
    manager = Manager()

    filePath = manager.getFilePath()
    addressList = loadTrace(filePath)

    cacheChoice = manager.getCacheChoice()
    parameter = manager.getParameter(cacheChoice)

    total, hits, cold, conflict = manager.simulateCache(
        cacheChoice, parameter, addressList
    )

    print("Accesses:", total)
    print("Hits:", hits)
    print("Cold misses:", cold)
    print("Conflict misses:", conflict)

main()