def inputNums():
    arr = []
    file = open("input.txt")

    for i in range(100):
        arr.append(int(file.readline))

    return arr

def main():
    arr = inputNums()

if __name__ == "__main__":
    main()