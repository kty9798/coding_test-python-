D = [0] * 100

def pibo(x):
    print('f(' + str(x) + ")" , end = " ")
    if x ==1 or x ==2:
        return 1
    if D[x] !=0:
        return D[x]
    

    return D[x]

if __name__ == "__main__":
    pibo(6)