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


def powers_of_two(limit=512):
    """
    Generate powers of 2 up to the specified limit.
    
    Args:
        limit: Maximum value for powers of 2 (default: 512)
        
    Returns:
        List of powers of 2 up to the limit
    """
    result = []
    power = 1
    while power <= limit:
        result.append(power)
        power *= 2
    return result


def print_powers_of_two(limit=512):
    """
    Print powers of 2 up to the specified limit.
    
    Args:
        limit: Maximum value for powers of 2 (default: 512)
    """
    powers = powers_of_two(limit)
    print(f"Powers of 2 up to {limit}: {powers}")


def main():
    """Main function to demonstrate Fibonacci and powers of 2 printing."""
    # Call Fibonacci functions
    print_fibonacci(5)
    print_fibonacci(10)
    print_fibonacci(1)
    print_fibonacci(0)
    
    # Call powers of 2 function
    print_powers_of_two(512)


if __name__ == "__main__":
    main()
