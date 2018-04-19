

def InputWeights():
    file = open("input.txt")
    n = file.readline()
    weight_string = file.readline()
    weights = map(int, weight_string.split(' '))
    return int(n), weights

def main():
    n, weights = InputWeights()
    print(n)


if __name__ == "__main__":
    main()