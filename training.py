import csv
import matplotlib.pyplot as plt

mileage = []
price = []

theta0 = 0.0
theta1 = 0.0

learning_rate = 0.01
iterations = 10000

# Leer archivo
try: 
    with open('data.csv', mode='r') as file: 
        csvFile = csv.reader(file)
        next(csvFile)  # saltar cabecera
        for lines in csvFile:
            mileage.append(float(lines[0]))
            price.append(float(lines[1]))
except:
    print('No se ha podido leer el archivo')

m = len(mileage)

# Normalización simple por máximo
max_mileage = max(mileage)
max_price = max(price)

mileage_norm = [x / max_mileage for x in mileage]
price_norm = [x / max_price for x in price]

# Configuración inicial del gráfico
plt.ion()  # modo interactivo
fig, ax = plt.subplots()
ax.scatter(mileage, price, color="blue", label="Datos reales")

line, = ax.plot([], [], color="red", label="Recta entrenada")
ax.set_xlabel("Kilometraje (km)")
ax.set_ylabel("Precio ($)")
ax.set_title("Entrenamiento paso a paso")
ax.legend()

# Entrenamiento con descenso de gradiente
for it in range(iterations):
    predictions = [theta0 + theta1 * km for km in mileage_norm]
    errors = [predictions[i] - price_norm[i] for i in range(m)]

    grad0 = sum(errors) / m
    grad1 = sum(errors[i] * mileage_norm[i] for i in range(m)) / m

    theta0 -= learning_rate * grad0
    theta1 -= learning_rate * grad1

    # Mostrar cada 100 iteraciones
    if it % 100 == 0 or it == iterations - 1:
        a = theta0 * max_price
        b = theta1 * (max_price / max_mileage)

        x_line = [0, max_mileage]
        y_line = [a + b * x for x in x_line]

        line.set_xdata(x_line)
        line.set_ydata(y_line)

        ax.set_title(f"Iteración {it}")
        plt.pause(0.05)

plt.ioff()
plt.show()

# Al final mostrar los valores definitivos
a = theta0 * max_price
b = theta1 * (max_price / max_mileage)

print("Theta0 (normalizado):", theta0)
print("Theta1 (normalizado):", theta1)
print(f"Modelo en valores reales: price = {a:.2f} + {b:.2f} * mileage")

def predict(km):
    return a + b * km

print("Precio estimado para 240,000 km:", predict(240000))


# Guardar los parámetros
# Al final del entrenamiento, guardar parámetros + máximos
with open("model.txt", "w") as f:
    f.write(f"{theta0},{theta1},{max_mileage},{max_price}")
