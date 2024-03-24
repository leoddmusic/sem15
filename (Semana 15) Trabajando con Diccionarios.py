informacion_personal = {
    "Nombre": "Ariel",
    "Edad": 28,
    "Ciudad" : "Quito",
    "Profesion": "Ingeniero"
}

# Modificar la ciudad y Profesion
informacion_personal["Ciudad"] = "Esmeraldas"
informacion_personal["Profesion"] = "Desarrollador Web"

# Verificar y agregar "telefono" si no existe
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "123-456-7890"

# Eliminar la clave "Edad"
del informacion_personal["Edad"]

# Imprimir el diccionario actualizado
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")


