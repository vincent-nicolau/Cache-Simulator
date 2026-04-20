from collections import deque

class Cache:
    CAPACITY = 32

    def __init__(self, blockSize):
        self.blockSize = blockSize

    def runSimulation(self, addressList, associativity):
        lineCount = Cache.CAPACITY // self.blockSize
        setCount = lineCount // associativity

        hits = 0
        coldMisses = 0
        conflictMisses = 0

        seen = set()
        sets = [deque(maxlen=associativity) for _ in range(setCount)]

        for address in addressList:
            block = address // self.blockSize
            setIndex = block % setCount
            currentSet = sets[setIndex]

            if block in currentSet:
                hits += 1
                currentSet.remove(block)
                currentSet.appendleft(block)
            else:
                if block not in seen:
                    coldMisses += 1
                    seen.add(block)
                else:
                    conflictMisses += 1

                currentSet.appendleft(block)

        totalAccesses = len(addressList)

        return totalAccesses, hits, coldMisses, conflictMisses