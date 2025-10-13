import csv
import matplotlib.pyplot as plt

def load_data(filename='data.csv'):
    """Carrega les dades del fitxer CSV"""
    mileage = []
    price = []
    
    try: 
        with open(filename, mode='r') as file: 
            csvFile = csv.reader(file)
            next(csvFile)  # saltar cabecera
            for lines in csvFile:
                mileage.append(float(lines[0]))
                price.append(float(lines[1]))
    except:
        print('No se ha podido leer el archivo')
        
    return mileage, price

def normalize_data(mileage, price):
    """Normalitza les dades dividint pel màxim"""
    max_mileage = max(mileage)
    max_price = max(price)
    
    mileage_norm = [x / max_mileage for x in mileage]
    price_norm = [x / max_price for x in price]
    
    return mileage_norm, price_norm, max_mileage, max_price

def setup_plot(mileage, price):
    """Configura el gràfic inicial"""
    plt.ion()  # modo interactivo
    fig, ax = plt.subplots()
    ax.scatter(mileage, price, color="blue", label="Datos reales")
    
    line, = ax.plot([], [], color="red", label="Recta entrenada")
    ax.set_xlabel("Kilometraje (km)")
    ax.set_ylabel("Precio ($)")
    ax.set_title("Entrenamiento paso a paso")
    ax.legend()
    
    return fig, ax, line

def gradient_descent(mileage_norm, price_norm, max_mileage, max_price, ax, line, learning_rate=0.01, iterations=10000):
    """Implementa l'algoritme de descens de gradient"""
    m = len(mileage_norm)
    theta0 = 0.0
    theta1 = 0.0
    
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
    
    return theta0, theta1

def save_model(theta0, theta1, max_mileage, max_price):
    """Guarda els paràmetres del model desnormalitzats"""
    # Desnormalitzar els paràmetres
    theta0_real = theta0 * max_price
    theta1_real = theta1 * (max_price / max_mileage)
    
    # Guardar theta0 i theta1 desnormalitzats
    with open("model.txt", "w") as f:
        f.write(f"{theta0_real},{theta1_real}")
    
    return theta0_real, theta1_real

def show_results(theta0_real, theta1_real, theta0_norm, theta1_norm):
    """Mostra els resultats finals"""
    print(f"Theta0 (normalizado): {theta0_norm}")
    print(f"Theta1 (normalizado): {theta1_norm}")
    print(f"Modelo en valores reales: price = {theta0_real:.2f} + {theta1_real:.2f} * mileage")

if __name__ == "__main__":
    # Cargar dades
    mileage, price = load_data()
    
    # Normalitzar dades
    mileage_norm, price_norm, max_mileage, max_price = normalize_data(mileage, price)
    
    # Configurar gràfic
    fig, ax, line = setup_plot(mileage, price)
    
    # Entrenar model
    theta0, theta1 = gradient_descent(mileage_norm, price_norm, max_mileage, max_price, ax, line)
    
    # Mostrar gràfic final
    plt.ioff()
    plt.show()
    
    # Guardar model i mostrar resultats
    theta0_real, theta1_real = save_model(theta0, theta1, max_mileage, max_price)
    show_results(theta0_real, theta1_real, theta0, theta1)
