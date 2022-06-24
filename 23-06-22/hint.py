import random
NUM_DIGITS = 3
MAX_GUESSES = 10

intro_text = f"""
Este es un juego de logica.
Estoy pensando un numero de {NUM_DIGITS} digitos
Cuando yo diga:

    **Pico** tiene un dígito correcto pero en el lugar equivocado.

    **Fermi** tiene un digito dígito en el lugar correcto 

    **Bagels** no tiene dígitos correctos.
    
Por ejemplo si el numero secreto es 248
y tu intento fue 843 las pistas que obtendrias serian
Fermi - Pico
"""
print(intro_text)
numbers = list('0123456789')
while True:
    random.shuffle(numbers)
    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])

    print("He pensado el numero")
    print(f"Tines {MAX_GUESSES} intentos para adivinarlo")

    num_guesses = 1
    while num_guesses <= MAX_GUESSES:
        guess = ""
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print(f"Intento numero {num_guesses}")
            guess = input("> ")
        if guess == secret_num:
            print("Lo lograste")
            break
        clues = []

        for i in range(len(guess)):
            if guess[i] == secret_num[i]:
                print(guess[i], secret_num[i], "FERMI")
                clues.append("Fermi")
            elif guess[i] in secret_num:
                print(guess[i], secret_num[i], "PICO")
                clues.append("Pico")
        if len(clues)==0:
            print("Bagels")
        else:
            clues.sort()
            value_clues = " ".join(clues)
            print(value_clues)

        if guess == secret_num:
            print("Acertaste")
            break

        num_guesses += 1
        if num_guesses > MAX_GUESSES:
            print("Te quedaste sin intetos")
            print(f"La respuesta correcta es {secret_num}")

    print("Quieres jugar denuevo (s o n)")
    if not input('> ').lower().startswith('s'):
        break
print("Gracias por jugar")
