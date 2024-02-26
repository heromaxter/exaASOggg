import os

for i in range(1, 6):
    carpeta = f"folder{i}"
    os.makedirs(carpeta)
    for j in range(1, 11):
        nombre_fichero = f"{carpeta}/fichero{j}.txt"
        with open(nombre_fichero, 'w') as f:
            f.write(f"Este es el contenido del fichero {j}\n")
