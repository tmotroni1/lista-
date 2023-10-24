import os

lista = []

while True:
    acoes = input('Digite o que deseja fazer com a lista: 1- adicionar 2- deletar 3- mostrar 4- encerrar: ')
    
    try:
        if acoes == '1':
            adicionar = input('Digite o que deseja adicionar: ')
            lista.append(adicionar)
            os.system('cls')

        elif acoes == '2':
            print(lista)
            remover = int(input('Digite qual item você deseja deletar da lista: '))
            lista.pop(remover)
            os.system('cls')
            print(lista)

        elif acoes == '3':
            if len(lista) == 0:
                nada_para_mostrar = input('Nada para mostrar, aperte qualquer tecla para continuar: ')
                os.system('cls')

            elif lista:
                for i in lista:
                    print(i)

        elif acoes == '4':
            print('Encerrando lista...')
            break
    except:
        continuar = input('Opção incorreta, aperte qualquer botão para continuar: ')
        continue
    
print(lista)    
    