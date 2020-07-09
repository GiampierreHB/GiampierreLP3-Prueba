# Ejercico que determine si un estudiante esta aprobado o no.
# Autor :Giampierre Huaman Berru


def determinaraprobado(promedio):
    if promedio>=11:
        resultado="Aprobado"
    else:
        resultado="Desaprobado"
    return resultado
promedio =int(input("Promedio: "))
print(determinaraprobado(promedio))