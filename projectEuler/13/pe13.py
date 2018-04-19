def inputNums():
    arr = []
    file = open("projectEuler\\13\\input.txt")

    for i in range(100):
        arr.append(file.readline())
        arr[i] = arr[i][:15]

    return arr

def addNums(arr):
    total = 0
    for num in arr:
        total += int(num)

    return str(total)[:10]

def main():
    arr = inputNums()
    total = addNums(arr)
    print(total)

if __name__ == "__main__":
    main()