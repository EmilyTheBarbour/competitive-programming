def toys(weights):
    crates = []
    weights = bubbleSort(weights)

    while (len(weights) > 0):
        maxWeight = weights[0] + 4
        crate = []
        while(weights[0] <= maxWeight):
            crate.append(weights.pop(0))
            if (len(weights) == 0):
                break
        crates.append(crate)
    
    return crates

def bubbleSort(arr):
    sort = False
    temp = 0
    numpairs = len(arr) - 1

    while (not sort):
        sort = True
        for i in range(numpairs):
            if (arr[i] > arr[i + 1]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                sort = False
        numpairs -= 1

    return arr

def InputWeights():
    file = open("HackerRank\\input.txt")
    n = file.readline()
    weights = [int (n) for n in file.readline().split()]
    return int(n), weights

def main():
    n, weights = InputWeights()
    crates = toys(weights)

    for crate in crates:
        print (crate)
    
    print(len(crates))

if __name__ == "__main__":
    main()
