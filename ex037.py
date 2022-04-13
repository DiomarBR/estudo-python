def loop():
    
    numero = int(input('Digite um numero inteiro:'))
    opcao = int(input(
    'Escolha uma das bases para coversão:\n'
    '[1] para binário\n'
    '[2] para octal\n'
    '[3] para hexadecimal\n'
))
    match opcao:
        case 1:
            print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)))
        case 2:
            print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)))
        case 3:
            print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)))
def finalizar():
    entry2 = int(input("1-Fechar \n"
                       "2-Novamente \n"
                       ": "))
    match entry2:
        case 1:
            print("Finalizado")
        case 2:
            loop();
            finalizar()
loop()
finalizar()