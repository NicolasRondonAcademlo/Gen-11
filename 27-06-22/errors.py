
def safe_divide(a,b):
    try:
        result = a / b
    except ConnectionError:
        result = 0
    except ZeroDivisionError:
        result = "No puedes dividir por 0"
    else:
       print( "No hubo ninguna exception")
    finally:
        print("Esto siempre se ejecuta")
    return result

print(safe_divide(10,0))
def safe_divide(a,b):
    try:
        result = a / b
    except Exception as e :
        result  = f" No pudiste efectuar la operacion por {str(e)}"
    return result
