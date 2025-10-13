def load_model():
    """Carrega els paràmetres del model"""
    try:
        with open("model.txt", "r") as f:
            line = f.readline()
            theta0, theta1 = map(float, line.strip().split(","))
    except:
        print('No se ha podido leer el archivo')
        print("Primero debes ejecutar: python3 training.py")
        exit(1)
    return theta0, theta1

def predict(km, theta0, theta1):
    """Prediu el preu basant-se en els quilòmetres"""
    return theta0 + theta1 * km

def get_valid_mileage():
    """Demana i valida els quilòmetres de l'usuari"""
    while True:
        try:
            user_input = input("Introduce los km del coche: ").strip()
            
            # Comprovar si està buit
            if not user_input:
                print("Error: No puedes dejar el campo vacío")
                continue
            
            # Convertir a float
            km_coche = float(user_input)
            
            # Comprovar si és negatiu
            if km_coche < 0:
                print("Error: Los kilómetros no pueden ser negativos")
                continue           
            return km_coche
            
        except ValueError:
            print("Error: Debes introducir un número válido")
        except KeyboardInterrupt:
            print("\nOperación cancelada")
            exit(0)

if __name__ == "__main__":
    # Carregar el model
    theta0, theta1 = load_model()
    
    # Demanar quilòmetres
    km_coche = get_valid_mileage()
    
    # Fer predicció
    precio_estimado = predict(km_coche, theta0, theta1)
    if (precio_estimado < 0):
        print("Tu coche tiene demasiado km. No se puede vender!")
    else:
        print(f"Precio estimado: {precio_estimado:.2f} €")
