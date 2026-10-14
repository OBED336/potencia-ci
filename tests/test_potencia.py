import pytest

from potencia import potencia


def test_potencia_positiva():
    assert potencia(2, 3) == 8


def test_exponente_cero():
    assert potencia(5, 0) == 1


def test_base_cero():
    assert potencia(0, 4) == 0


def test_cero_elevado_a_cero():
    assert potencia(0, 0) == 1


def test_exponente_negativo():
    assert potencia(2, -2) == pytest.approx(0.25)


def test_base_negativa():
    assert potencia(-2, 3) == -8


def test_base_incorrecta():
    with pytest.raises(TypeError):
        potencia("dos", 3)


def test_exponente_incorrecto():
    with pytest.raises(TypeError):
        potencia(2, 1.5)


def test_cero_con_exponente_negativo():
    with pytest.raises(ValueError):
        potencia(0, -1)