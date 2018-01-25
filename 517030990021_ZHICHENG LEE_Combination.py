def recursive(n,k): #recursive method
    if k == 1:
        return n
    elif n < k:
        return 0

    else:
        return recursive(n-1,k-1) + recursive(n-1,k)

def fac(n): #factorial function in iteratiive way
    ans = 1
    for i in range(1,n+1):
        ans = ans * i
    return ans


def iterative(n,k): #iterative method to do combination
    combination = fac(n) / (fac(k) * fac(n-k))
    return combination

def main():
    print recursive(27,18)
    print iterative(27,18)
main()

#comment out either one function and run it.
#recursive take much longer time than iterative.
#therefore, iterative is more effective than recursive method.
