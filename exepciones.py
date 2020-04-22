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
    #except:
    #Si se pone solamente el except solo sin ningun error , es decir que hay un error general detecta un error pero no sabe cual  es el tipo de error.
    #finally:
    #se pone finally para que lo ejecute si o si despues del except, se va a ejecutar siempre
    #tambien se puede poner otro except y otro tipo de error por si se equivoca de otra forma, poniendo letras por ejemlpo
"""esto sirve para que el resto del programa no se caiga por un error que esta antes"""
while True:
    try:
        op1 = (int(input("Introduce el primer n�mero: ")))

        op2 = (int(input("Introduce el segundo n�mero: ")))
        break #usamos el while para que valide los dos valores y si son validados sigue con el programa
    except ValueError:
        print("Los valores introducidos no son correctos. intentelo denuevo")

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