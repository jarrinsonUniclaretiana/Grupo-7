def calcular_liquidacion():
    print("LIQUIDACION JARCO SAS")

    nombre = input("Ingrese nombre del vendedor: ")
    salario_base = float(input("Ingrese salario base: "))
    ventas = float(input("Ingrese total de ventas del mes: "))
    horas_extras = int(input("Ingrese cantidad de horas extras: "))

    wp = int(input("Cantidad proyectos WordPress: "))
    woo = int(input("Cantidad proyectos WooCommerce: "))
    custom = int(input("Cantidad proyectos Custom: "))

    comisiones = ventas * 0.07

    if 41 <= horas_extras <= 50:
        pago_extras = horas_extras * 18000
    elif 51 <= horas_extras <= 60:
        pago_extras = horas_extras * 25000
    else:
        pago_extras = 0

    total_proyectos = wp + woo + custom

    if ventas > 3000000 and total_proyectos >= 5:
        bono_objetivo = 250000
    else:
        bono_objetivo = 0

    puntos = (wp * 1) + (woo * 2) + (custom * 3)

    total = salario_base + comisiones + pago_extras + bono_objetivo

    print("\nDESGLOSE")
    print("Nombre:", nombre)
    print("Salario base:", salario_base)
    print("Comisiones:", comisiones)
    print("Horas extras:", pago_extras)
    print("Bono por objetivo:", bono_objetivo)
    print("Puntos por proyectos:", puntos)
    print("TOTAL FINAL:", total)

    if total > 4200000:
        print("Vendedor Estrella con dia libre adicional")

calcular_liquidacion()
