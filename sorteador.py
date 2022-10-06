from random import choice


def sorteador_palavra():

    palavras = ['Acender', 'Afilhado', 'Ardiloso', 'Assombração',
                'característica', 'Asterisco', 'Champanhe', 'extraordinário',
                'demasiadamente', 'sadomasoquismo', 'Convivência', 'irrepreensível',
                'Gororoba', 'Independência', 'preponderância', 'arbitrariedade',
                'Modernidade', 'Quarentena', 'especificidade', 'posteriormente',
                'Campeonato', 'Nitrogênio', 'contextualizar', 'empreendimento',
                'entretenimento', 'ancestralidade', 'revolucionário', 'infraestrutura',
                'Cálcio', 'Oxigênio', 'queixo', 'atenciosamente', 'mandíbula',
                'relacionamento', 'tornozelo', 'periodicamente', 'arrependimento',
                'transcendência', 'imparcialidade', 'ponto de vista', 'democratização',
                'reconhecimento', 'dedo', 'insignificante', 'personificação',
                'inconsistência', 'despretensioso', 'espontaneidade', 'Lionel Messi']

    return choice(palavras)


def retira_acentos(palavra):

    palavra = palavra.replace('Á', 'A')
    palavra = palavra.replace('Ã', 'A')
    palavra = palavra.replace('À', 'A')
    palavra = palavra.replace('Â', 'A')
    palavra = palavra.replace('Ä', 'A')
    palavra = palavra.replace('É', 'E')
    palavra = palavra.replace('Ê', 'E')
    palavra = palavra.replace('È', 'E')
    palavra = palavra.replace('Ë', 'E')
    palavra = palavra.replace('Í', 'I')
    palavra = palavra.replace('Ì', 'I')
    palavra = palavra.replace('Ï', 'I')
    palavra = palavra.replace('Î', 'I')
    palavra = palavra.replace('Õ', 'O')
    palavra = palavra.replace('Ó', 'O')
    palavra = palavra.replace('Ò', 'O')
    palavra = palavra.replace('Ô', 'O')
    palavra = palavra.replace('Ö', 'O')
    palavra = palavra.replace('Ú', 'U')
    palavra = palavra.replace('Û', 'U')
    palavra = palavra.replace('Ü', 'U')
    palavra = palavra.replace('Ù', 'U')
    palavra = palavra.replace('Ç', 'C')

    return palavra


def montar_boneco(erros):

    cabeca = ' '
    tronco = ' '
    troncoo = ' '
    bracesq = '   '
    bracdir = '   '
    pernesq = ' '
    perndir = ' '
    cabeca2 = 'Ô'
    tronco2 = '|'
    bracesq2 = '\_ '
    bracdir2 = ' _/'
    pernesq2 = '/'
    perndir2 = '\\'

    if erros >= 1:

        cabeca = cabeca2

    if erros >= 2:

        tronco = tronco2
        troncoo = tronco2

    if erros >= 3:

        bracesq = bracesq2

    if erros >= 4:

        bracdir = bracdir2

    if erros >= 5:

        pernesq = pernesq2

    if erros == 6:

        perndir = perndir2

    print(f" _________      \n")
    print(f" |/      |      \n")
    print(f" |       {cabeca}\n")
    print(f" |    {bracesq}{tronco}{bracdir} \n")
    print(f" |       {troncoo}    \n")
    print(f" |      {pernesq} {perndir}   \n")
    print(f" |              \n")
    print(f"_|___           \n")
    print(f"")

    if erros == 6:

        return True
