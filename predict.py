def load_model():
    """Carrega els paràmetres del model"""
    with open("model.txt", "r") as f:
        line = f.readline()
        theta0, theta1 = map(float, line.strip().split(","))
    return theta0, theta1

def predict(km, theta0, theta1):
    """Prediu el preu basant-se en els quilòmetres"""
    return theta0 + theta1 * km

if __name__ == "__main__":
    # Carregar el model
    theta0, theta1 = load_model()
    
    # Demanar quilòmetres
    km_coche = float(input("Introduce los km del coche: "))
    
    # Fer predicció
    precio_estimado = predict(km_coche, theta0, theta1)
    
    # Mostrar resultat
    print(f"Precio estimado: {precio_estimado:.2f} €")
