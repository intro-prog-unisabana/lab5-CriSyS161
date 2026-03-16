import utils_calc as uc
ejecutando = True
while ejecutando: 
    a = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):")
    b = a.lower()
    if "add" == b:
        respuesta = uc.add(input("Enter the firt number"),input("Enter the second number"))
        algo = print("The result is:",respuesta)
    elif "substract" == b:
        respuesta = uc.subs(input("Enter the firt number"),input("Enter the second number"))
        algo = print("The result is:",respuesta)
    elif "multiply" == b:
        respuesta = uc.multiply(input("Enter the firt number"),input("Enter the second number"))
        algo = print("The result is:",respuesta)
    elif "divide" == b:
        respuesta = uc.divide(input("Enter the firt number"),input("Enter the second number"))
        if type(respuesta) != str:
            a = print("The result is:",respuesta)
        else:
            a = respuesta
            algo = a
    elif "exponent" == b:
        respuesta = uc.exponent(input("Enter the firt number"),input("Enter the second number"))
        algo = print("The result is:",respuesta)
    elif "modulo" == b:
        respuesta = uc.modulo("Enter the firt number"),input(("Enter the second number"))
        if type(respuesta) != str:
            a = print("The result is:",respuesta)
        else:
            a = respuesta
            algo = a
    elif "floor_divide"== b:
        respuesta = uc.floor_divide(input("Enter the firt number"),input("Enter the second number"))
        algo = print("The result is:",respuesta)
    elif "absolute" == b:
        respuesta = uc.absolute(input("Enter the number"))
        algo = print("The result is:",respuesta)
    elif "exit" == b:
        ejecutando = False
    else:
        algo = print("Invalid option!")
    