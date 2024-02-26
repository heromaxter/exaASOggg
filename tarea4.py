import psutil
import logging

logging.basicConfig(filename='/home/ggg/logs/espacio.log', level=logging.INFO)

def analizar_espacio():
    espacio = psutil.disk_usage('/')
    espacio_ocupado = espacio.percent
    if espacio_ocupado > 80:
        logging.error("El espacio ocupado en la partición raíz es mayor que 80%")
    elif espacio_ocupado > 60:
        logging.warning("El espacio ocupado en la partición raíz es mayor que 60% pero menor que 80%")
    else:
        logging.info("El espacio ocupado en la partición raíz es menor que 60%")

if __name__ == "__main__":
    analizar_espacio()
