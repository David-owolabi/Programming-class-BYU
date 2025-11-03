# weather.py
# weather.py
def cels_from_fahr(fahr):
    """Convert Fahrenheit to Celsius."""
    return (fahr - 32) * 5 / 9

if __name__ == '__main__': 
    # Example usage
    print(cels_from_fahr(100))