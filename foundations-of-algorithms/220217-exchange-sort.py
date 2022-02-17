def exchange (S):
    n = len(S) - 1
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if(S[i] > S[j]):
                S[i], S[j] = S[j], S[i] #swap

S = [-1, 10, 7, 11, 5, 13, 8]
print("Before: ", S)
exchange(S)
print("After: ", S)