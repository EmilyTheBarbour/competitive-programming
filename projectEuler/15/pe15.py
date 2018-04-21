totalPaths = 0

def generatePaths(x, y, size):
    global totalPaths
    if x < size:
        generatePaths(x + 1, y, size)
    if y < size:
        generatePaths(x, y + 1, size)
    if x == size and y == size:
        totalPaths += 1
        if totalPaths % 10000 == 0:
            print(totalPaths)


def main():
    generatePaths(0, 0, 20)
    print(totalPaths)

if __name__ == "__main__":
    main()