def print_prime(n):
    for i in range(n+1):
        if prime(i) is True:
            print i


def prime(n):
    if n == 0:
        return False
    elif n == 1:
        return False
    else:
        j = 2
        while j < n:
            if n % j == 0:
                return False
            else:
                j = j + 1
        return True

print_prime(100)
