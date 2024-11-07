# main.py
import csv
from vehiculo import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

def main():
    vehiculos = []
    cantidad = int(input("Cuantos Vehiculos desea insertar: "))

    for i in range(1, cantidad + 1):
        print(f"\nDatos del automóvil {i}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        vehiculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        vehiculos.append(vehiculo)

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(f"Datos del automóvil {i}: {vehiculo}")

if __name__ == "__main__":
    main()

# añadir las funciones de guardar y recuperar



def guardar_datos_csv(vehiculos):
    try:
        with open("vehiculos.csv", "w", newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                archivo_csv.writerow([vehiculo.__class__.__name__, vehiculo.__dict__])
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def leer_datos_csv():
    try:
        with open("vehiculos.csv", "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for fila in archivo_csv:
                print(fila)
    except Exception as e:
        print(f"Error al leer los datos: {e}")

# Ejemplo de uso


vehiculos = [
    Particular("Ford", "Fiesta", 4, 180, 500, 5),
    Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000),
    Bicicleta("Shimano", "MT Ranger", 2, "Carrera"),
    Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
]

guardar_datos_csv(vehiculos)
leer_datos_csv()
