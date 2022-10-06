from sorteador import montar_boneco, sorteador_palavra, retira_acentos
import os
from sistema_usuarios import Sistema_Users


def jogo():

    palavra_sorteada = sorteador_palavra().upper()
    palavra_sorteada_s_acento = retira_acentos(palavra_sorteada)
    chances = 5
    contador = 0
    palavra_alterada = '_'*len(palavra_sorteada)
    palavra_alterada2 = ''
    lista_tentativas = []
    lista_letras_erradas = []
    contagem_erros = 0

    os.system('cls')

    while True:

        contador += 1

        if contagem_erros == 6:

            os.system('cls')

        if retira_acentos(palavra_sorteada) == palavra_alterada2:

            resultado = 'vitoria'

            print('\033[1;32mYOU WIN!\033[m\n')

            break

        resultado_boneco = montar_boneco(contagem_erros)

        if resultado_boneco == True:

            resultado = 'derrota'

            print('\033[1;31mGAME OVER!\033[m\n')

            break

        if contador == 1:

            print(f'\nPalavra: {palavra_alterada}\n')

        else:

            palavra_alterada2 = ''

            for letra in palavra_sorteada_s_acento:

                if letra in lista_tentativas or letra == '-' or letra == ' ':

                    palavra_alterada2 += letra

                else:

                    palavra_alterada2 += '_'

            print(f'{palavra_alterada2}\n')

        if palavra_alterada2.upper() == palavra_sorteada_s_acento.upper():

            resultado = 'vitoria'

            os.system('cls')

            print('\n\033[1;32mYOU WIN!\033[m\n')

            break

        tentativa_usuario = retira_acentos(input('Digite uma letra: ').upper())

        while True:

            if len(tentativa_usuario) > 1 or len(tentativa_usuario) < 1:

                tentativa_usuario = retira_acentos(input(
                    '\nDigite apenas uma letra: ').upper())

            if tentativa_usuario in lista_tentativas:

                print(f'\nLetras já usada antes. {lista_tentativas}')

                tentativa_usuario = retira_acentos(input(
                    '\nDigite uma letra não usada anteriormente: ').upper())

            if tentativa_usuario.isdigit():

                tentativa_usuario = retira_acentos(
                    input('Digite apenas letras: ').upper())

            if len(tentativa_usuario) == 1 and tentativa_usuario not in lista_tentativas and not tentativa_usuario.isdigit():

                break

        lista_tentativas.append(tentativa_usuario.upper())

        os.system('cls')

        if tentativa_usuario in palavra_sorteada_s_acento:

            print(f'Letras usadas: {lista_tentativas}\n')

            print(
                f'Letras usadas que não há na palavra: {lista_letras_erradas}\n')

        else:

            lista_letras_erradas.append(tentativa_usuario)

            contagem_erros += 1

            print(f'Letra "{tentativa_usuario}" não existe na palavra.\n')

            print(f'Letras usadas: {lista_tentativas}\n')

            print(
                f'Letras usadas que não há na palavra: {lista_letras_erradas}\n')

            chances -= 1

    print(f'A Palavra sorteada era {palavra_sorteada}\n')

    if resultado == 'vitoria':

        return True

    elif resultado == 'derrota':

        return False


def inicializacao():  # INICIA O PROGRAMA

    usuario = ''

    os.system('cls')

    while True:

        escolha_usuario = input("""
Escolha uma das opções abaixo.

[1] Cadastro
[2] Login

Escolha do Usuario: """)

        if escolha_usuario == '1':
            
            os.system('cls')

            usuario = Sistema_Users(nickname=input('\nNickname: ').lower(), email=input('Email: '), senha=input('Senha: '), repeticao_senha=input('Repita a Senha: '))

            verificacao_erro = usuario.cadastro()

            break

        elif escolha_usuario == '2':

            os.system('cls')
            
            usuario = Sistema_Users(nickname=input(
                '\nNickname: ').lower(), senha=input('Senha: '))

            verificacao_erro = usuario.login()

            break

        else:

            os.system('cls')

            print('\nEscolha uma alternativa valida.\n')


    if verificacao_erro == True:

        carregar_jogo(usuario, verificacao_erro)  # COMEÇA O JOGO

    else:

        print(verificacao_erro)


def carregar_jogo(usuario, verificacao_erro):

    os.system('cls')

    usuario.ranking()

    contador = 0

    while True:

        if contador > 0:

            resposta_usuario = input('Deseja continuar jogando: ').lower()

            if resposta_usuario != 'nao' and resposta_usuario != 'n' and \
                    resposta_usuario != 'no' and resposta_usuario != 'not' and \
                    resposta_usuario != 'parar' and resposta_usuario != 'não' and\
                    resposta_usuario != 'cancelar':

                pass

            else:

                break

        contador += 1

        resultado_jogo = jogo()

        if resultado_jogo == True:

            usuario.vitoria()

            usuario.status()

        elif resultado_jogo == False:

            usuario.derrota()

            usuario.status()

        else:

            print(verificacao_erro)
