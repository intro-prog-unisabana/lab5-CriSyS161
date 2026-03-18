import utils_calc as uc
ejecutando = True
while ejecutando: 
    a = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):")
    b = a.lower()
    if "add" == b:
        respuesta = uc.add(float(input("Enter the first number:\n")), float(input("Enter the second number:\n")))
        algo = print("The result is:", respuesta)
    elif "subtract" == b:
        respuesta = uc.sub(float(input("Enter the first number:\n")), float(input("Enter the second number:\n")))
        algo = print("The result is:", respuesta)
    elif "multiply" == b:
        respuesta = uc.multiply(input("Enter the first number:\n"), input("Enter the second number:\n"))
        algo = print("The result is:", respuesta)
    elif "divide" == b:
        respuesta = uc.divide(input("Enter the first number:\n"), input("Enter the second number:\n"))
        if type(respuesta) == str:
            print(respuesta)
        else:
            print("The result is:", respuesta)
    elif "exponent" == b:
        respuesta = uc.exponent(input("Enter the first number:\n"), input("Enter the second number:\n"))
        algo = print("The result is:", respuesta)
    elif "modulo" == b:
        respuesta = uc.modulo(float(input("Enter the first number:\n")), float(input("Enter the second number:\n")))
        if type(respuesta) == str:
            print(respuesta)
        else:
           print("The result is:", respuesta)
    elif "floor_divide"== b:
        respuesta = uc.floor_divide(input("Enter the first number:\n"), input("Enter the second number:\n"))
        algo = print("The result is:", respuesta)
    elif "absolute" == b:
        respuesta = uc.absolute(input("Enter the number:\n"))
        algo = print("The result is:", respuesta)
    elif "exit" == b:
        ejecutando = False
    else:
        algo = print("Invalid option!")
    