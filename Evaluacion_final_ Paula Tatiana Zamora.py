# Nombre: Paula Tatiana Zamora Guchuvo
# Grupo: 213022-364
# Programa: Ingeniería Electrónica
# Código fuente: Autoría propia

#EVALUACIÓN FINAL POA

#PROGRAMA DE NIVEL DE COMPROMISO DE CLIENTES

#Matriz
sesiones = [
    [1001, 240, 10],
    [1002, 45, 2],
    [1003, 120, 6],
    [1004, 300, 15],
    [1005, 55, 7]
]
#Modulo cálculo de clasificación de compromiso
def clasificar_compromiso(duracion, clicks):
    if duracion > 180 and clicks > 8:
        return "Alto"
    elif duracion < 60 or clicks < 3:
        return "Bajo"
    else:
        return "Medio"

# GENERACIÓN DEL INFORME FINAL
print(" INFORME FINAL DE COMPROMISO DE CLIENTES ")

# Recorrer cada sesión de la matriz
for sesion in sesiones:
    # Extraer datos de la sesión
    id_cliente = sesion[0]
    duracion = sesion[1]
    clicks = sesion[2]
    # Llamar la función de clasificación
    nivel = clasificar_compromiso(duracion, clicks)

    # Mostrar resultados
    print(f"Cliente ID: {id_cliente}")
    print(f"Duración de sesión: {duracion} segundos")
    print(f"Cantidad de clics: {clicks}")
    print(f"Nivel de compromiso: {nivel}")
    print("------------------------------------------")