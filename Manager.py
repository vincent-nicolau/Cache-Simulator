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

    filePath = input("Trace file: ")
    addressList = loadTrace(filePath)

    cacheChoice = input("Cache type A/B: ").strip().upper()
    parameter = int(input("Parameter: "))

    total, hits, cold, conflict = manager.simulateCache(
        cacheChoice, parameter, addressList
    )

    print("Accesses:", total)
    print("Hits:", hits)
    print("Cold misses:", cold)
    print("Conflict misses:", conflict)

main()