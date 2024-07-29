def obtener_fraccion():
    while True:
        try:
            # Solicita la fracción al usuario
            fraccion = input("Ingrese la fracción en formato X/Y: ")
            # Divide la entrada en X e Y
            X, Y = fraccion.split('/')
            # Convierte X e Y a enteros
            X = int(X)
            Y = int(Y)

            # Verifica que X sea menor o igual a Y y que Y no sea 0
            if X > Y or Y == 0:
                raise ValueError("X debe ser menor o igual a Y y Y debe ser distinto de 0")

            # Calcula el porcentaje
            porcentaje = (X / Y) * 100

            # Redondea el porcentaje al entero más cercano
            porcentaje_redondeado = round(porcentaje)

            # Verifica los casos especiales y da el resultado
            if porcentaje < 1:
                return "E"
            elif porcentaje > 99:
                return "F"
            else:
                return f"{porcentaje_redondeado}%"
        
        except ValueError:
            print("Error. Asegúrese de ingresar una fracción en formato X/Y, donde X y Y son enteros y X <= Y, y Y != 0.")
        except ZeroDivisionError:
            print("Error. Y no puede ser 0.")

# Se invoca a la función para obtener el resultado
resultado = obtener_fraccion()
print("Nivel de combustible:", resultado)