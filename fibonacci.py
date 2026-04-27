def print_fibona(n):
    """
    Print Fibonacci sequence up to n terms.
    
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


def print_fibona(n):
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
    print_fibona(5)
    print_fibona(10)
    print_fibona(1)
    print_fibona(0)


if __name__ == "__main__":
    main()
