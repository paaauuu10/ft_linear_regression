import csv

# Getting data from .csv
def load_data(filename='data.csv'):
    mileage = []
    price = []
    
    try: 
        with open(filename, mode='r') as file: 
            csvFile = csv.reader(file)
            next(csvFile)  # saltar cabecera
            for lines in csvFile:
                mileage.append(float(lines[0]))
                price.append(float(lines[1]))
            if (len(mileage) < 1):
                exit (1)
    except:
        print('No se ha podido leer el archivo')
        exit(1)
        
    return mileage, price

# Normalize to get values between 0-1
def normalize_data(mileage, price):
    max_mileage = max(mileage)
    max_price = max(price)
    
    mileage_norm = [x / max_mileage for x in mileage]
    price_norm = [x / max_price for x in price]
    
    return mileage_norm, price_norm, max_mileage, max_price

def gradient_descent(mileage_norm, price_norm, learning_rate=0.01, iterations=10000):
    m = len(mileage_norm)
    theta0 = 0.0
    theta1 = 0.0
    
    print("-" * 50)
    print("Iniciando entrenamiento...")

    
    # Gradient descent loop
    for it in range(iterations):
        predictions = [theta0 + theta1 * km for km in mileage_norm]
        errors = [predictions[i] - price_norm[i] for i in range(m)]

        grad0 = sum(errors) / m
        grad1 = sum(errors[i] * mileage_norm[i] for i in range(m)) / m

        theta0 -= learning_rate * grad0
        theta1 -= learning_rate * grad1
     
    return theta0, theta1

# Saves theta00 and theta01
def save_model(theta0, theta1, max_mileage, max_price):
    theta0 = theta0 * max_price
    theta1 = theta1 * (max_price / max_mileage)
    
    with open("model.txt", "w") as f:
        f.write(f"{theta0},{theta1}")
    
    return theta0, theta1


def show_results(theta0, theta1):

    print(f"Theta0: {theta0}")
    print(f"Theta1: {theta1}")
    print(f"Modelo en valores reales: price = {theta0:.2f} + {theta1:.2f} * mileage")
    print("¡Entrenamiento completado!")
    print("-" * 50)

if __name__ == "__main__":
    mileage, price = load_data()
    mileage_norm, price_norm, max_mileage, max_price = normalize_data(mileage, price)
    theta0, theta1 = gradient_descent(mileage_norm, price_norm)
    theta0, theta1 = save_model(theta0, theta1, max_mileage, max_price)
    show_results(theta0, theta1)
