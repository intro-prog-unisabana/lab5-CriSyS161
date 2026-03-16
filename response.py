def input_response(generate_value, user_imput):
    if user_imput > generate_value:
        mensaje = "Too high! Try a lower number."
        correcto = False
    elif user_imput < generate_value:
        mensaje = "Too low! Try a higher number."
        correcto = False
    else:
        mensaje = "Correct! You guessed the number."
        correcto = True

    return mensaje, correcto

print(input_response(50, 50))
