#Son errores que ocurren durante la ejecucion del programa,
#la sintaxis del codigo es correcta pero durante la ejecucion
#ha ocurrido algo inesperado

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try: #intente realizar esta instruccion y si no lo consigue que se ejecute lo que esta dentro del except
        return num1 / num2
    except ZeroDivisionError:  #se ejecuta solo si esta mal lo que esta lo del try"
        print("No se puede dividir entre 0")
        return "Operacion erronea"
"""esto sirve para que el resto del programa no se caiga por un error que esta antes"""
op1 = (int(input("Introduce el primer n�mero: ")))

op2 = (int(input("Introduce el segundo n�mero: ")))

operacion = input("Introduce la operaci�n a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operaci�n no contemplada")

print("Operaci�n ejecutada. Continuaci�n de ejec�ci�n del programa ")