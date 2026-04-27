def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms and return the list.
    
    Args:
        n: Number of terms in the Fibonacci sequence
        
    Returns:
        List of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib


def print_fibonacci(n):
    """
    Print Fibonacci sequence up to n terms.
    
    Args:
        n: Number of terms to print
    """
    fib_sequence = fibonacci(n)
    print(f"Fibonacci sequence ({n} terms): {fib_sequence}")


def main():
    """Main function to demonstrate Fibonacci printing."""
    # Call the function with different values
    print_fibonacci(5)
    print_fibonacci(10)
    print_fibonacci(1)
    print_fibonacci(0)


if __name__ == "__main__":
    main()
