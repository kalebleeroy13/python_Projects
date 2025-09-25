import math
import sys
from typing import List

def find_factors(n: int) -> List[int]:
    """Return the sorted list of factors of n."""
    factors = set()
    root = int(math.isqrt(n))
    for i in range(1, root + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)

def is_prime(n: int) -> bool:
    """Return True if n is prime, else False."""
    return len(find_factors(n)) == 2

def main() -> None:
    """Main loop for user interaction."""
    banner = (
        "Factor Finder, by Al Sweigart al@inventwithpython.com\n\n"
        "A number's factors are two numbers that multiply to the number.\n"
        "Prime numbers have exactly two factors: 1 and themselves.\n"
    )
    print(banner)

    while True:
        response = input("Enter a positive whole number to factor (or QUIT): ").strip()
        if response.upper() == "QUIT":
            sys.exit()

        if not (response.isdecimal() and int(response) > 0):
            print("Please enter a valid positive integer.")
            continue

        number = int(response)
        factors = find_factors(number)
        print(f"\nFactors of {number}: {', '.join(map(str, factors))}")
        print("This number is", "prime." if is_prime(number) else "composite.", "\n")

if __name__ == "__main__":
    main()
