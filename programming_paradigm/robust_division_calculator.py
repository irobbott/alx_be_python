def safe_divide(numerator, denominator):
    """Perform division with error handling for zero division and non-numeric inputs."""
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            return "Error: Cannot divide by zero."
        result = num / den
        return f"The result of the division is {result:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."
