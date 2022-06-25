from email import message


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    print("Quieres (e)ncriptar o (d)esencriptar")
    respose = input("> ").lower()
    if respose.startswith('e'):
        mode = "encrypt"
        break
    if respose.startswith("d"):
        mode = "decrypt"
        break

    print("Por favor ingresa la letra e o d")

while True:
    max_key = len(SYMBOLS) -1
    print(f"Por favor ingresa la llave que este entre (0 y {max_key})")
    response = input("> ")
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key =int(response)
        break

print(f"Ingresa el mensage a {mode}")
message = input("> ").upper()


for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol) 
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num <0:
            num = num +len(SYMBOLS)
        
        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)
        
