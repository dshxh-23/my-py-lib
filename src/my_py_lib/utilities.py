import time
import random

def print_ellipsis(s: str = "", n: int = 3, delay: float = 0.8) -> None:
    """
    Prints a string followed by a specified number of periods (ellipsis), 
    printing each period at a specified interval.
    
    Args:
        s (str): The string to print before the ellipsis.
        n (int): Number of periods to print. If 0, a random number (3-8) is used.
                 Must be between 1 and 99 (inclusive), or 0 for random.
        delay (float): Time in seconds to wait between printing each period. Default is 0.8 seconds.
    Raises:
        ValueError: If n is not 0 or not in the range 1-99.
    """
    
    if n == 0:
        n = random.randint(3, 8)
    if not (1 <= n < 100):
        raise ValueError("n should be between 1 - 99, or 0 for random.")

    print(s, end="", flush=True)
    for i in range(n):
        print(".", end="", flush=True)
        time.sleep(delay)
    print()  # Move to next line after ellipsis