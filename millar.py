#millor Rabin algorithm
import random

def miller_rabin_test(n, k=5):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

# Example usage:
num_to_check = 99999999977
if miller_rabin_test(num_to_check):
    print(f"{num_to_check} is probably prime.")
else:
    print(f"{num_to_check} is composite.")
