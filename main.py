#exemplo qye causa typeerror

try:
    resultado = len(1)
    print(resultado)
except TypeError as e:
    print(e)
else:
    print("tudo ocorreu bem")