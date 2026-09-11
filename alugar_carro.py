import os 

def limpar_tela():
    os.system('cls')

portifolio = [
     {'indice': '[0] Chevrolet Tracker', 'valor': 120},
     {'indice': '[1] Chevrolet Onix', 'valor': 80},
     {'indice': '[2] Renault Kwid', 'valor': 50},
     {'indice': '[3] Renault Sandero', 'valor': 80},
     {'indice': '[4] Honda Civic', 'valor': 120},
     {'indice': '[5] Toyota Etios', 'valor': 50},
     {'indice': '[6] Volkswagen Gol', 'valor': 80},
     {'indice': '[7] Volkswagen Jetta', 'valor': 120},
     {'indice': '[8] Jeep Renegade', 'valor': 150},
     {'indice': '[9] Porshe Cayenne', 'valor': 300}
]

devolver = []

def port():  
    for chave in portifolio:
        print(f'{chave['indice']} / {chave['valor']} R$ p/dia')



while True:
    print('=========')
    print('BEM-VINDO A LOCADORA DE CARROS')
    print('=========')
    print('O QUE DESEJA FAZER \n 0 - MOSTRAR PORTIFOLIO | 1 - ALUGAR UM CARRO | 2 - DEVOLVER UM CARRO')
    
    try:
     op = int(input())

    except ValueError:
        limpar_tela()
        print('Opção invalida, tente novamente')
        continue
    
    if op == 0:   
        limpar_tela()
        print('========= PAINEL DE PORTIFOLIO =========')
        port()
        print('0 - CONTINUAR | 1 - SAIR')
        op1 = int(input())
        if op1 == 0:
            limpar_tela()
            continue
        elif op1 == 1:
            limpar_tela()
            break
    
    elif op == 1:
        limpar_tela()
        print('[ALUGAR]--- Dê uma olhada no portifolio\n\n\n')
        port()
        print('\n\n\n===============')

        try:
            print('Escolha o codigo do carro:')
            escolha = int(input())
            print('Por quantos dias deseja alugar ?')
            dias = int(input())
        except ValueError:
            print('Opção invalida, tente novamente')
            continue
        carro_encontrado = None
        for i, carro in enumerate(portifolio):
            if carro ['indice'].startswith(f'[{escolha}]'):
                carro_encontrado = portifolio.pop(i)
                total = carro_encontrado['valor'] * dias
                carro_encontrado['dias'] = dias
                carro_encontrado['total'] = total
                devolver.append(carro_encontrado)
                limpar_tela()
                print(f'Voce escolheu {carro_encontrado['indice']} por {dias} dias')
                print(f'O aluguel vai ficar: {total}')
                print('Deseja alugar ? 0 - Sim |1- Não ')
                op2 = int(input())
                if op2 == 0:
                    print(f'Parabens você alugou {carro_encontrado} por {dias} dias ')
                    limpar_tela()
                    print('============')
                    print('0 - Continuar | 1 - Sair')
                    op3 = int(input())
                    if op3 == 0:
                        limpar_tela()
                        continue
                    elif op3 == 1:
                        limpar_tela()
                        break
                elif op2 == 1:
                    limpar_tela() 
                    break
        if not carro_encontrado:
            print('Carro não encontrado, tente novamente')
                
    elif op == 2:
        limpar_tela()
        print('Segue a lista de carros alugados, qual desejaria devolver ?')
        if not devolver:
            print('Nenhum carro alugado novamente')
            limpar_tela()
            continue

        for carro in devolver:
            print(f'{carro['indice']}')

        try:
            print('Escolha o codigo do carro:')
            deployed = int(input())
            
        except ValueError:
            print('Opção invalida, tente novamente')
            limpar_tela()
            continue

        devolvido = None
        for i, carro in enumerate(devolver):
            if carro ['indice'].startswith(f'[{deployed}]'):
                devolvido = devolver.pop(i)

                

                portifolio.append(devolvido)
                print(f'\n\n\nObrigado por devolver{devolvido['indice']}')

                print('\n\n\n============')
                print('0 - Continuar | 1 - Sair')
                op4 = int(input())
                if op4 == 0:
                    limpar_tela()
                    continue
                elif op4 == 1:
                    limpar_tela()
                    break
        if not devolvido:
                print('Carro não encontrado')
                
                    
                    
                
        

        


    
        
        
    
        
    
