def potencia(base, exponente):
    """
    Calcula una base elevada a un exponente entero.

    Args:
        base (int o float): Número que se elevará.
        exponente (int): Exponente positivo, negativo o cero.

    Returns:
        int o float: Resultado de la potencia.

    Raises:
        TypeError: Si la base no es numérica o el exponente no es entero.
        ValueError: Si la base es cero y el exponente es negativo.

    Examples:
        >>> potencia(2, 3)
        8
        >>> potencia(2, -2)
        0.25

    Se adopta la convención de Python: cero elevado a cero devuelve 1.
    """
    if isinstance(base, bool) or not isinstance(base, (int, float)):
        raise TypeError("La base debe ser un número.")

    if isinstance(exponente, bool) or not isinstance(exponente, int):
        raise TypeError("El exponente debe ser un número entero.")

    if base == 0 and exponente < 0:
        raise ValueError("Cero no puede elevarse a un exponente negativo.")

    return base ** exponente