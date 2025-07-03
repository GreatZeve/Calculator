def add(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("Los argumentos deben ser números.")
    return a + b

# Suma multiple en el mismo script.
def add_multiple(*args):
    if not args:
        raise ValueError("Debe proporcionar al menos un número.")
    try:
        numbers = [float(arg) for arg in args]
    except ValueError:
        raise TypeError("Todos los argumentos deben ser números.")
    return sum(numbers)