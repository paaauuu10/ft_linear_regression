import csv

# Getting data from .csv
def load_data():
    mileage = []
    price = []
    
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Omitir el encabezado si existe
        
        for row in reader:
            try:
                km = float(row[0])
                price = float(row[1])
                
                # Omitir líneas con valores negativos
                if km < 0 or price < 0:
                    print(f"Omitiendo línea con valores negativos: {row}")
                    continue                
                mileage.append(km)
                price.append(price)
            except ValueError:
                print(f"Omitiendo línea con datos inválidos: {row}")
                continue
    
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

if __name__ == "__main__":
    mileage, price = load_data()
    mileage_norm, price_norm, max_mileage, max_price = normalize_data(mileage, price)
    theta0, theta1 = gradient_descent(mileage_norm, price_norm)
    theta0, theta1 = save_model(theta0, theta1, max_mileage, max_price)
    show_results(theta0, theta1)
