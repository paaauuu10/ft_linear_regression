import csv
import matplotlib.pyplot as plt
import os

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
        print('Error: No se ha podido leer el archivo data.csv')
        return None, None
        
    return mileage, price

def load_model(filename="model.txt"):
    """Carrega els paràmetres del model"""
    if not os.path.exists(filename):
        print("Error: No se encontró el archivo model.txt")
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

def plot_data_and_model():
    """Mostra les dades i la línia de regressió"""
    # Carregar dades
    mileage, price = load_data()
    if mileage is None:
        return
    
    # Carregar model
    theta0, theta1 = load_model()
    if theta0 is None:
        return
    
    # Crear el gràfic
    plt.figure(figsize=(10, 6))
    
    # Punts de les dades reals
    plt.scatter(mileage, price, color="blue", alpha=0.6, s=50, label="Datos reales")
    
    # Línia de regressió
    min_km = min(mileage)
    max_km = max(mileage)
    x_line = [min_km, max_km]
    y_line = [theta0 + theta1 * x for x in x_line]
    
    plt.plot(x_line, y_line, color="red", linewidth=2, label="Línea de regresión")
    
    # Configuració del gràfic
    plt.xlabel("Kilometraje (km)")
    plt.ylabel("Precio (€)")
    plt.title("Regresión Lineal: Precio vs Kilometraje")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Mostrar la fórmula
    plt.figtext(0.15, 0.02, f"Fórmula: precio = {theta0:.2f} + ({theta1:.6f}) * km", 
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
    
    plt.tight_layout()
    plt.show()

def plot_interactive():
    """Gràfic interactiu que mostra prediccions quan cliques"""
    # Carregar dades
    mileage, price = load_data()
    if mileage is None:
        return
    
    # Carregar model
    theta0, theta1 = load_model()
    if theta0 is None:
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Punts de les dades reals
    scatter = ax.scatter(mileage, price, color="blue", alpha=0.6, s=50, label="Datos reales")
    
    # Línia de regressió
    min_km = min(mileage)
    max_km = max(mileage)
    x_line = [min_km, max_km]
    y_line = [theta0 + theta1 * x for x in x_line]
    
    ax.plot(x_line, y_line, color="red", linewidth=2, label="Línea de regresión")
    
    # Configuració del gràfic
    ax.set_xlabel("Kilometraje (km)")
    ax.set_ylabel("Precio (€)")
    ax.set_title("Regresión Lineal Interactiva\n(Haz clic en cualquier lugar para ver predicción)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Text per mostrar prediccions
    prediction_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=10,
                             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7),
                             verticalalignment='top')
    
    def on_click(event):
        if event.inaxes != ax:
            return
        
        km_clicked = event.xdata
        if km_clicked is not None:
            precio_predicho = theta0 + theta1 * km_clicked
            prediction_text.set_text(f"Predicción:\n{km_clicked:.0f} km → {precio_predicho:.2f} €")
            plt.draw()
    
    fig.canvas.mpl_connect('button_press_event', on_click)
    
    # Mostrar la fórmula
    plt.figtext(0.15, 0.02, f"Fórmula: precio = {theta0:.2f} + ({theta1:.6f}) * km", 
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
    
    plt.tight_layout()
    plt.show()

def show_precision():
    """Mostra estadístiques del model i les dades"""
    # Carregar dades
    mileage, price = load_data()
    if mileage is None:
        return
    
    # Carregar model
    theta0, theta1 = load_model()
    if theta0 is None:
        return
    
    # Calcular estadístiques
    n_samples = len(mileage)
    min_km, max_km = min(mileage), max(mileage)
    min_price, max_price = min(price), max(price)
    avg_km, avg_price = sum(mileage)/n_samples, sum(price)/n_samples
    
    # Calcular R² (coeficient de determinació)
    predictions = [theta0 + theta1 * km for km in mileage]
    ss_res = sum((price[i] - predictions[i])**2 for i in range(n_samples))
    ss_tot = sum((price[i] - avg_price)**2 for i in range(n_samples))
    r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
    
    print("=" * 60)
    print("ESTADÍSTIQUES DEL MODEL DE REGRESSIÓ LINEAL")
    print("-" * 60)
    print("PARÁMETROS DEL MODELO:")
    print(f"θ₀ (interceptación): {theta0:,.2f} €")
    print(f"θ₁ (pendent): {theta1:.6f} €/km")
    print("-" * 60)
    print("INTERPRETACIÓN:")
    print(f"• Coeficiente de determinación (R²): {r_squared:.4f}")
    if r_squared > 0.8:
        print("  → Excelente ajuste del modelo")
    elif r_squared > 0.6:
        print("  → Buen ajuste del modelo")
    elif r_squared > 0.4:
        print("  → Ajuste moderado del modelo")
    else:
        print("  → Ajuste pobre del modelo")
    print("=" * 60)

def menu():
    """Mostra un menú d'opcions"""
    while True:
        print("\n" + "="*50)
        print("VISUALIZACIÓN DE REGRESIÓN LINEAL")
        print("="*50)
        print("1. Ver gráfico básico (datos + línea de regresión)")
        print("2. Ver gráfico interactivo (clic para predicción)")
        print("3. Ver estadísticas del modelo")
        print("4. Salir")
        print("-"*50)
        
        try:
            choice = input("Selecciona una opción (1-4): ")
            
            if choice == '1':
                plot_data_and_model()
            elif choice == '2':
                plot_interactive()
            elif choice == '3':
                show_precision()
            elif choice == '4':
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor selecciona 1, 2, 3 o 4.")
                
        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()
