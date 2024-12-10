if __name__ == '__main__':
    n = int(input())
    
list = [i for i in range(n) if i >= 0]

quadrados = [i**2 for i in list]

for quadrado in quadrados:
    print(quadrado)
