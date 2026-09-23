"""
Conversor de unidades
Autor: Fabrizio Galindo Ayala

Programa de consola que convierte:
    - Celsius <-> Fahrenheit
    - Kilometros <-> Millas
    - Pesos Mexicanos <-> Dolares (tasa fija)

Todas las funciones de conversion estan separadas del menu de consola
para poder importarlas y probarlas facilmente con pytest.
"""

# Tasa de cambio fija definida en el programa (pesos mexicanos por dolar)
TASA_MXN_USD = 18.50


def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


def fahrenheit_a_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)


def km_a_millas(km):
    """Convierte kilometros a millas."""
    millas = km * 0.621371
    return round(millas, 2)


def millas_a_km(millas):
    """Convierte millas a kilometros."""
    km = millas / 0.621371
    return round(km, 2)


def mxn_a_usd(mxn, tasa=TASA_MXN_USD):
    """Convierte pesos mexicanos a dolares usando una tasa fija."""
    usd = mxn / tasa
    return round(usd, 2)


def usd_a_mxn(usd, tasa=TASA_MXN_USD):
    """Convierte dolares a pesos mexicanos usando una tasa fija."""
    mxn = usd * tasa
    return round(mxn, 2)


def pedir_valor_numerico(mensaje):
    """Solicita un valor numerico al usuario y valida que sea correcto."""
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Por favor ingresa un valor numerico valido.")


def mostrar_menu():
    print("\n===== CONVERSOR DE UNIDADES =====")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Kilometros a Millas")
    print("4. Millas a Kilometros")
    print("5. Pesos Mexicanos a Dolares")
    print("6. Dolares a Pesos Mexicanos")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "0":
            print("Programa finalizado.")
            break
        elif opcion == "1":
            valor = pedir_valor_numerico("Ingresa el valor en Celsius: ")
            print(f"Resultado: {celsius_a_fahrenheit(valor)} F")
        elif opcion == "2":
            valor = pedir_valor_numerico("Ingresa el valor en Fahrenheit: ")
            print(f"Resultado: {fahrenheit_a_celsius(valor)} C")
        elif opcion == "3":
            valor = pedir_valor_numerico("Ingresa el valor en kilometros: ")
            print(f"Resultado: {km_a_millas(valor)} millas")
        elif opcion == "4":
            valor = pedir_valor_numerico("Ingresa el valor en millas: ")
            print(f"Resultado: {millas_a_km(valor)} km")
        elif opcion == "5":
            valor = pedir_valor_numerico("Ingresa el valor en pesos mexicanos: ")
            print(f"Resultado: {mxn_a_usd(valor)} USD")
        elif opcion == "6":
            valor = pedir_valor_numerico("Ingresa el valor en dolares: ")
            print(f"Resultado: {usd_a_mxn(valor)} MXN")
        else:
            print("Opcion no valida, intenta de nuevo.")


if __name__ == "__main__":
    main()