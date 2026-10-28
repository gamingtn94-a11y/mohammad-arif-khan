# Prime Number Checker

A simple Python program that checks whether an integer entered by the user is prime.

## Requirements

- Python 3

## How to Run

Open a terminal in the project directory and run:

```bash
python ai_ass.py
```

Enter an integer when prompted.

## Example

```text
Enter a number: 17
17 is a prime number.
```

```text
Enter a number: 12
12 is not a prime number.
```

## How It Works

1. Reads an integer from the user.
2. Numbers less than or equal to `1` are not prime.
3. Tests divisors from `2` through the square root of the number.
4. If a divisor is found, the number is not prime.
5. Otherwise, the number is prime.

The divisor range is limited to the square root because any composite number has at least one factor no greater than its square root.

## Complexity

- Time: `O(sqrt(n))`
- Auxiliary space: `O(1)`
