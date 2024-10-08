def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    """Test the is_prime function."""
    assert is_prime(2) is True, "Test case 1 failed"
    assert is_prime(3) is True, "Test case 2 failed"
    assert is_prime(4) is False, "Test case 3 failed"
    assert is_prime(17) is True, "Test case 4 failed"
    assert is_prime(20) is False, "Test case 5 failed"
    assert is_prime(1) is False, "Test case 6 failed"
    assert is_prime(0) is False, "Test case 7 failed"
    assert is_prime(-5) is False, "Test case 8 failed"
    
    print("All test cases passed!")
