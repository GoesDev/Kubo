from core.models import Conta
import os

nova_conta = Conta('Nubank', 1000, 0)

nova_conta.conta()

cond = True

while cond:
    os.system('cls')

    print('Vamos criar uma Conta')
    resposta = input('s ou n\n-- ')
    if resposta == 's':
        pass
    elif resposta == 'n':
        cond = False
    else:
        print('Resposta Inválida')


