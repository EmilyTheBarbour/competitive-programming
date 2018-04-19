def generatePath(n):
    arr = []
    for i in range (n):
        arr.append(1)
    for i in range (n):
        arr.append(0)

    return arr

def printPath(path):
    for num in path:
        if num == 1:
            print("---")
        if num == 0:
            print("|")

def main():
    arr = generatePath(2)
    printPath(arr)

if __name__ == "__main__":
    main()