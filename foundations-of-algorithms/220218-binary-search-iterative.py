S = [-1, 10, 7, 11, 5, 13, 8]
S.sort()

def binary_search (n, S, x):
    low = 1
    high = n
    location = 0
    while(low <= high and location == 0):
        mid = (low + high) // 2
        print("curr mid: ", mid)
        if(x == S[mid]):
            location = mid
        elif(x < S[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return location

print(binary_search(6, S, 5))

