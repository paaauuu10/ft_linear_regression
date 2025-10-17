import csv
import matplotlib.pyplot as plt
import os

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
                pr = float(row[1])
                
                # Omitir líneas con valores negativos
                if km < 0 or pr < 0:
                    print(f"Omitiendo línea con valores negativos: {row}")
                    continue
                
                mileage.append(km)
                price.append(pr)
            except ValueError:
                print(f"Omitiendo línea con datos inválidos: {row}")
                continue
    
    return mileage, price


#Carrega els paràmetres del model
def load_model(filename="model.txt"):
    
    if not os.path.exists(filename):
        print("No se encontró el archivo model.txt")
        print("Primero debes ejecutar: python3 training.py")
        return None, None
    
    try:
        with open(filename, "r") as f:
            line = f.readline()
            theta0, theta1 = map(float, line.strip().split(","))
        return theta0, theta1
    except:
        print("Error: No se pudo cargar el modelo")
        return None, None

# Show data and line

def plot_data_and_model():
    # Loading data
    mileage, price = load_data()
    if mileage is None:
        return
    
    # Loading model
    theta0, theta1 = load_model()
    if theta0 is None:
        return
    
    # Creating graph
    plt.figure(figsize=(10, 6))
    
    # Dots
    plt.scatter(mileage, price, color="blue", alpha=0.6, s=50)
    
    # Line
    min_km = min(mileage)
    max_km = max(mileage)
    x_line = [min_km, max_km]
    y_line = [theta0 + theta1 * x for x in x_line]
    
    plt.plot(x_line, y_line, color="red", linewidth=2, label="Línea de regresión")
    
    # Graph details
    plt.xlabel("Kilometraje (km)")
    plt.ylabel("Precio (€)")
    plt.title("Regresión Lineal: Precio vs Kilometraje")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.show()

if __name__ == "__main__":
    try:
        plot_data_and_model()
    except KeyboardInterrupt:
        print("\nCiao")
