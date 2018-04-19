def generateSequence(n):
    arr = [n]
    while (n > 1):
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        arr.append(n)
    
    return arr

def main():
    MaxChain = []
    startingNum = 0

    for i in range(1000000):
        arr = generateSequence(i)
        if len(arr) > len(MaxChain):
            MaxChain = arr
            startingNum = i
            print(startingNum, ": ", len(MaxChain))

if __name__ == "__main__":
    main()
        