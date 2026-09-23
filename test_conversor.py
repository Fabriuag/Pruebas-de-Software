"""
Casos de prueba del conversor de unidades.
Autor: Fabrizio Galindo Ayala

Se usa pytest para automatizar la verificacion de las funciones de
conversor.py. Se incluyen markers y una prueba parametrizada, tal
como lo pide la actividad integradora.
"""

import pytest
from conversor import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    km_a_millas,
    millas_a_km,
    mxn_a_usd,
    usd_a_mxn,
)


# ---------------------------------------------------------------------
# CP01 - Conversion de Celsius a Fahrenheit (Requerimiento RF01)
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_celsius_a_fahrenheit():
    """CP01: 0 C debe convertirse en 32.0 F."""
    resultado = celsius_a_fahrenheit(0)
    assert resultado == 32.0


# ---------------------------------------------------------------------
# CP02 - Conversion de Fahrenheit a Celsius (Requerimiento RF01)
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_fahrenheit_a_celsius():
    """CP02: 212 F debe convertirse en 100.0 C."""
    resultado = fahrenheit_a_celsius(212)
    assert resultado == 100.0


# ---------------------------------------------------------------------
# CP03 - Conversion de Kilometros a Millas (Requerimiento RF02)
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_km_a_millas():
    """CP03: 10 km deben ser aproximadamente 6.21 millas."""
    resultado = km_a_millas(10)
    assert resultado == 6.21


# ---------------------------------------------------------------------
# CP04 - Conversion de Millas a Kilometros (Requerimiento RF02)
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_millas_a_km():
    """CP04: 10 millas deben ser aproximadamente 16.09 km."""
    resultado = millas_a_km(10)
    assert resultado == 16.09


# ---------------------------------------------------------------------
# CP05 - Conversion de Pesos Mexicanos a Dolares (Requerimiento RF03)
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_mxn_a_usd():
    """CP05: 185 MXN con tasa de 18.50 deben ser 10.0 USD."""
    resultado = mxn_a_usd(185)
    assert resultado == 10.0


# ---------------------------------------------------------------------
# CP06 - Conversion de Dolares a Pesos Mexicanos (Requerimiento RF03)
# ---------------------------------------------------------------------
@pytest.mark.unit
def test_usd_a_mxn():
    """CP06: 10 USD con tasa de 18.50 deben ser 185.0 MXN."""
    resultado = usd_a_mxn(10)
    assert resultado == 185.0


# ---------------------------------------------------------------------
# CP07 - Prueba parametrizada de Celsius a Fahrenheit
# (Requerimientos RF01 y RNF01: precision de al menos dos decimales)
# ---------------------------------------------------------------------
@pytest.mark.unit
@pytest.mark.parametrize(
    "celsius, esperado",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),
    ],
)
def test_celsius_a_fahrenheit_parametrizado(celsius, esperado):
    """CP07: valida varios valores de Celsius a Fahrenheit en una sola prueba."""
    assert celsius_a_fahrenheit(celsius) == esperado