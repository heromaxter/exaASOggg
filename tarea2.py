import psutil

def obtener_particiones_fisicas():
    particiones_fisicas = []
    particiones = psutil.disk_partitions(all=True)
    for particion in particiones:
        if particion.device.startswith('/dev/sd'):
            particiones_fisicas.append(particion)
    return particiones_fisicas

def mostrar_porcentaje_uso(particiones):
    for particion in particiones:
        try:
            uso = psutil.disk_usage(particion.mountpoint)
            porcentaje = uso.percent
            print(f"{particion.device} {porcentaje:.1f}%")
        except Exception as e:
            print(f"No se pudo obtener información de la partición {particion.mountpoint}: {e}")

particiones_fisicas = obtener_particiones_fisicas()
mostrar_porcentaje_uso(particiones_fisicas)

