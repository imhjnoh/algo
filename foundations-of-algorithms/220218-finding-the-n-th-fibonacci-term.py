def fib (n):
    if ( 0 <= n and n <= 1 ):
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print("recursive : ", end="")
# for i in range(101):
#     print(fib(i), end=" ")  

# the recursive way is too inefficient

# the iterative way
def fib_itr (n):
    f = [0] * (n + 1)
    if(n > 0):
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i -2]
    return f[n]

print("\niterative : ", end="")
for i in range(101):
    print(fib_itr(i), end=" ")

# without f list
def fib_no_list (n):
    first = 0
    second = 1
    out = 1
    if(n >= 0 and n <= 1):
        return n
    else:
        for i in range(2, n + 1):
            out = first + second
            first = second
            second = out
    return out

print("\nno list : ", end="")
for i in range(101):
    print(fib_no_list(i), end=" ")
