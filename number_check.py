# Helper functions
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d**length for d in digits) == n

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))

