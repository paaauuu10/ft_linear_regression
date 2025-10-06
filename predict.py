# predecir.py
import csv

# Leer θ0 y θ1 del archivo
with open("model.txt", "r") as f:
    line = f.readline()
    theta0, theta1, max_mileage, max_price = map(float, line.strip().split(","))

# Convertir a escala real
a = theta0 * max_price
b = theta1 * (max_price / max_mileage)

# Convertir θ a escala real
a = theta0 * max_price
b = theta1 * (max_price / max_mileage)

# Función para predecir
def predict(km):
    return a + b * km

# Ejemplo de uso
km_coche = float(input("Introduce los km del coche: "))
precio_estimado = predict(km_coche)
print(f"Precio estimado: {precio_estimado:.2f} €")
