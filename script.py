# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicado a una compra.

    Parámetros:
    - monto_total: float, el monto total de la compra.
    - porcentaje_descuento: float, el porcentaje de descuento (por defecto es 10).

    Retorna:
    - El monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Primera llamada: solo el monto (usa el descuento por defecto del 10%)
    monto1 = 500
    descuento1 = calcular_descuento(monto1)
    print(f"Compra 1: Monto original: ${monto1}")
    print(f"Descuento aplicado (10%): ${descuento1}")
    print(f"Total a pagar: ${monto1 - descuento1}\n")

    # Segunda llamada: monto y porcentaje personalizado
    monto2 = 1000
    porcentaje2 = 20
    descuento2 = calcular_descuento(monto2, porcentaje2)
    print(f"Compra 2: Monto original: ${monto2}")
    print(f"Descuento aplicado ({porcentaje2}%): ${descuento2}")
    print(f"Total a pagar: ${monto2 - descuento2}")
