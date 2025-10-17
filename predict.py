# Loading model
def load_model():
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
    return theta0 + theta1 * km

# Validating milage input
def get_valid_mileage():
    while True:
        try:
            user_input = input("Introduce los km del coche: ").strip()
            
            if not user_input:
                print("No puedes dejar el campo vacío")
                continue
            
            # Convert to float
            km_coche = float(user_input)

            if km_coche < 0:
                print("Como vas a tener km negativos?")
                continue           
            return km_coche
            
        except ValueError:
            print("Debes introducir un número válido")
        except KeyboardInterrupt:
            print("\nCiao")
            exit(0)
        except EOFError:
            print("\nEntrada finalizada (Ctrl+D detectado). Ciao")
            exit(0)

if __name__ == "__main__":
 
    theta0, theta1 = load_model()
    km_coche = get_valid_mileage()
    precio_estimado = predict(km_coche, theta0, theta1)
    if (precio_estimado < 0):
        print("Tu coche tiene demasiado km. No se puede vender!")
    else:
        print(f"Precio estimado: {precio_estimado:.2f} €")
