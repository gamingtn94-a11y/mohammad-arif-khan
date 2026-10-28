def is_prime(number: int) -> bool:
    """Return True when number is prime, and False otherwise."""
    if number < 2:
        return False

    divisor = 2
    while divisor <= number // divisor:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def main() -> None:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")


if __name__ == "__main__":
    main()
