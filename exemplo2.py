# Função para calcular o dobro de um numero inteiro positivo
# Gerar exceção se o parametro da função não for inteiro e positivo
numero = int(input('Insira um numero: '))

def dobro(numero):
    if type(numero) != int:
        raise TypeError
    if numero < 0:
        raise ValueError
    
    # calcula o dobro do número
    resultado = numero * 2
    print(resultado)
    return resultado

dobro(numero)
try:
    r = resultado
    print('Dobro do numero: ', r)
except Exception:
    print('Ocorreu um Erro')