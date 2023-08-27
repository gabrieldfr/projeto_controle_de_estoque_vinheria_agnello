import time
#Definição de variávies globais
garrafas = {}
caixa_6_unidades = {}
caixa_12_unidades = {}
#Definindo funções
def menu_funcionario():
    print('Bem vindo ao controle de estoque da Vinheria Agnello')
    while True:
        choice = str(input('Você deseja adicionar uma:\n[1]Garrafa\n[2]Caixa\n')).strip()
        match choice:
            case '1':
                menu_garrafas()
                break
            case '2':
                menu_caixa()
                break
            case _:
                print('Valor inválido! Por favor digite 1 ou 2')


def menu_garrafas():
    if len(garrafas) > 0:
        print('Total de garrafas presentes no estoque:')
        for rotulo, quantidade in garrafas.items():
            print(f'- {rotulo} - quantidade: {quantidade}')
    else:
        print('Não há nenhuma garrafa cadastrada no estoque\n')

    rotulo = str(input('Rótulo da garrafa: '))
    while True:
        try:
            quantidade_garrafas = int(input('Quantidade de garrafas: '))
            garrafas[rotulo] = quantidade_garrafas
            break
        except ValueError:
            print('Erro! Por favor, digite apenas números inteiros')

    while True:
        choice = str(input('Deseja adicionar mais garrafas [S/N]? ')).strip().lower()
        match choice:
            case 's':
                menu_garrafas()
                break
            case 'n':
                while True:
                    choice = str(input('Você deseja\n[1]Voltar para o menu\n[2]Finalizar o programa\n')).strip()
                    match choice:
                        case '1':
                            menu_funcionario()
                            break
                        case '2':
                            print('<< Finalizando o Programa >>')
                            print('Até mais!')
                            time.sleep(3)
                            exit()
                        case _:
                            print('Valor inválido! Por favor, digite apenas 1 ou 2')
            case _:
                print('Valor inválido! Por favor, digite apenas S ou N')


def menu_caixa():
    while True:
        choice = str(input('Você deseja adicionar uma caixa contendo:\n[1]6 Unidades\n[2]12 Unidades\n')).strip()
        match choice:
            case '1':
                if len(caixa_6_unidades) > 0:
                    print('Total de caixas contendo 6 unidades presentes no estoque:')
                    for rotulo, quantidade in caixa_6_unidades.items():
                        print(f'- {rotulo} - quantidade de caixas: {quantidade}')
                else:
                    print('Não nenhuma caixa contendo 6 unidades presente no estoque')

                rotulo = str(input('Rótulo do vinho presente na caixa: '))
                while True:
                    try:
                        quantidade_caixas = int(input('Quantidade de caixas: '))
                        caixa_6_unidades[rotulo] = quantidade_caixas
                        break
                    except ValueError:
                        print('Erro! Por favor, digite apenas números inteiros')
                while True:
                    choice = str(input('Deseja adicionar mais caixas [S/N]? ')).strip().lower()
                    match choice:
                        case 's':
                            menu_caixa()
                            break
                        case 'n':
                            while True:
                                choice = str(input('Você deseja:\n[1]Voltar para o menu\n[2]Finalizar o programa\n')).strip()
                                match choice:
                                    case '1':
                                        menu_funcionario()
                                        break
                                    case '2':
                                        print('<< Finalizando o programa >>')
                                        print('Até mais!')
                                        time.sleep(3)
                                        exit()
                                    case _:
                                        print('Valor inválido! Por favor digite apenas 1 ou 2')
            case '2':
                if len(caixa_12_unidades) > 0:
                    print('Total de caixas contendo 12 unidades presentes no estoque')
#Início do código principal
print('Bem vindo a Vinheria Agnello')
while True:
    choice = str(input('Você é um:\n[1]Cliente\n[2]funcionário\n')).strip()
    match choice:
        case '2':
            menu_funcionario()
            break
        case _:
            print('Valor inválido! Por favor, digite apenas 1 ou 2')