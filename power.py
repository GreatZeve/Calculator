def power(base, exponent):
    try:
        base = float(base)
        exponent = float(exponent)
    except ValueError:
        raise TypeError("Los argumentos deben ser números.")
    return base ** exponent
