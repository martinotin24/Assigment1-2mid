#!/usr/bin/env python3
import os
import sys
import urllib.parse

# Obligatorio para que CGI funcione correctamente
print("Content-Type: text/html")
print()  # Línea en blanco requerida por CGI

# Obtener datos desde QUERY_STRING
query_string = os.getenv("QUERY_STRING", "")
params = urllib.parse.parse_qs(query_string)

# Extraer valores y convertirlos a enteros
try:
    numbers = [int(params[key][0]) for key in ['a', 'b', 'c', 'd', 'e'] if key in params]
except (ValueError, TypeError, KeyError):
    print("<h2>Error: Todos los valores deben ser números enteros.</h2>")
    sys.exit()

# Verificar si hay números negativos
negative_numbers = [num for num in numbers if num < 0]

# Calcular promedio
average = sum(numbers) / len(numbers)

# Determinar si el promedio es mayor a 50
average_check = "Sí" if average > 50 else "No"

# Contar números positivos y determinar paridad
positive_count = sum(1 for num in numbers if num > 0)
parity = "Par" if (positive_count & 1) == 0 else "Impar"

# Crear una lista con valores mayores a 10 y ordenarla
filtered_list = sorted([num for num in numbers if num > 10])

# Formatear salida en HTML
print(f"<h2>Resultados</h2>")
print(f"<p>Valores ingresados: {numbers}</p>")
print(f"<p>Números negativos: {negative_numbers if negative_numbers else 'Ninguno'}</p>")
print(f"<p>Promedio: {average}</p>")
print(f"<p>¿El promedio es mayor a 50? {average_check}</p>")
print(f"<p>Cantidad de positivos: {positive_count} (Paridad: {parity})</p>")
print(f"<p>Lista filtrada (>10): {filtered_list}</p>")
