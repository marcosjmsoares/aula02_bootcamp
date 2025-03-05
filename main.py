#exemplo qye causa typeerror

# try:
#     resultado = len("teste teste 123")
#     print(resultado)
# except TypeError as e:
#     print(e)
# else:
#     print("tudo ocorreu bem")
# finally:
#     print("bom estudo")

# numero = int(input("Insira um numero: "))
# if isinstance(numero,int):
#     print("A variavel e um inteiro")
# else:
#     print("A variavel nao e um inteiro")


idade = 18
idade_minima = 18
idade_tirar_carteira = 18

if idade < idade_minima:
    print("Nao pode dirigir")
elif idade == idade_tirar_carteira:
    print("Pode tirar a carteira esse ano")
else:
    print("Pode tirar carteira")