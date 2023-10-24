import os

lista = []

while True:
    acoes = input('Digite o que deseja fazer com a lista: 1- adicionar 2- deletar 3- mostrar 4- Limpar lista 5- encerrar: ')
    
    try:
        if acoes == '1':
            adicionar = input('Digite o que deseja adicionar: ')
            lista.append(adicionar)
            os.system('cls')

        elif acoes == '2':
            for i, item in enumerate(lista):
                    print(i, item)
            remover = int(input('Digite qual item você deseja deletar da lista: '))
            lista.pop(remover)
            os.system('cls')
            for i, item in enumerate(lista):
                    print(i, item)
            tecla = input('Pressione ENTER para continuar: ')
            os.system('cls')

        elif acoes == '3':
            if len(lista) == 0:
                nada_para_mostrar = input('Nada para mostrar, aperte ENTER para continuar: ')
                os.system('cls')

            elif lista:
                for i, item in enumerate(lista):
                    print(i, item)
                tecla = input('Pressione ENTER para continuar: ')
                os.system('cls')

        elif acoes == '4':
            limpar = input('Tem certeza que deseja limpar a lista? [S]im [N]não: ')
            limpar_low = limpar.lower()
        
            if limpar_low == 's':
                os.system('cls')
                lista.clear()
            elif limpar_low == 'n':
                os.system('cls')
                continue
            else:
                continuar = input('Opção incorreta, aperte ENTER para continuar: ')
                os.system('cls')
                continue
                
        elif acoes == '5':
            os.system('cls')
            print('Lista encerrada.')
            break
        else:
            continuar = input('Opção incorreta, aperte ENTER para continuar: ')
            os.system('cls')
            continue
    except:
        continuar = input('Opção incorreta, aperte ENTER para continuar: ')
        continue
    
for i, item in enumerate(lista):
    print(i, item)
    
