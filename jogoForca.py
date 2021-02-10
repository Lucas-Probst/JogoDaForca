import PySimpleGUI as sg
import random

# OBS: E PRECISO INSTALAR NO WINDOWS A FONTE "LED Calculator"

def gerar_palavra():
    global palavraAuxiliar
    arquivo = open("palavras.txt", "r", encoding="utf8")  # abre o arquivo palavras.txt que está localizado na mesma pasta do jogo
    palavrasArquivo = []
    for linha in arquivo:  # lê todas as linhas, cada linha no arquivo é uma palavra
        palavrasArquivo.append(linha)  # adiciona no vetor todas as palavras

    i = random.randrange(0, len(palavrasArquivo))  # variavel "i" recebe um valor aleatorio de 0 a quantidade total de palavras no arquivo - 1
    arquivo.close()  # fecha o arquivo
    palavra = palavrasArquivo[i]  # pega uma palavra aleatório no vetor e atribui para variavel palavra
    palavra = palavra.upper()  # deixa todas as letras em maiúsculo
    letras = []
    letrasAux = []

    # no arquivo txt, a cada quebra de linha ele cria um "\n", para eliminar esse \n fazemos "len(palavra)-1"
    for i in range(0, len(palavra)-1):  # vai de 0 até o tamanho da palavra - 2,
        letras.append(palavra[i])  # pega cada letra da String palavra e adiciona nos vetores letras e letrasAux
        letrasAux.append(palavra[i])
        # se não for feito "len(palavra)-1", ele irá adicionar o "\n" nesses vetores

    palavraAuxiliar = letrasAux
    return letras


palavraAuxiliar = []
palavraSecreta = gerar_palavra()
# print(palavraSecreta)
acertos = []
erros = []
palavraTela = ""
telaAcertos = ""
telaErros = ""
forca = "+----+\n" \
        "|    :\n" \
        "|\n" \
        "|\n" \
        "|\n" \
        "|\n" \

while True:
    for i in range(0, len(palavraAuxiliar)):  # vai de 0 até o tamanho da palavra - 1
        # lê cada caracter do vetor palavraAuxiliar, faz a substituição e concatena na String palavraTela
        if palavraAuxiliar[i] == " ":  # verifica se tem espaço
            palavraTela = palavraTela + " " + palavraAuxiliar[i]  # atribui o espaço para palavraTela
        elif palavraAuxiliar[i] == "-":  # verifica se tem hifen
            palavraTela = palavraTela + " " + palavraAuxiliar[i]  # atribui hifen para palavraTela
        else:
            palavraAuxiliar[i] = "_"  # se tiver qualquer letra em palavraAuxiliar, é atribuido o underscore
            palavraTela = palavraTela + " " + palavraAuxiliar[i]  # atribui o underscore para palavraTela
    break

# configuração dos botões
bw: dict = {'size': (2, 1), 'font': ('LED Calculator', 16), 'button_color': ("black", "#d6d5da")}

layout: list = [
    # Tela Forca
    [sg.Text(forca, size=(8, 6), background_color='#c9d2a8', text_color='#595e4d',
             font=('LED Calculator', 22), relief='sunken', key="_TELAFORCA_")],
    # Tela Acertos
    [sg.Text(" ACERTOS: "+telaAcertos, size=(30, 1), background_color='#c9d2a8', text_color='#595e4d',
             font=('LED Calculator', 18), relief='sunken', key="_TELAACERTOS_")],
    # Tela Erros
    [sg.Text(" ERROS: "+telaErros, size=(30, 1), background_color='#c9d2a8', text_color='#595e4d',
             font=('LED Calculator', 18), relief='sunken', key="_TELAERROS_")],
    # Tela Palavra
    [sg.Text(palavraTela, size=(30, 1), justification='center', background_color='#c9d2a8', text_color='#595e4d',
             font=('LED Calculator', 18), relief='sunken', key="_TELAPALAVRA_")],

    [sg.Button('Q', **bw), sg.Button('W', **bw), sg.Button('E', **bw), sg.Button("R", **bw), sg.Button('T', **bw),
     sg.Button('Y', **bw), sg.Button('U', **bw), sg.Button('I', **bw), sg.Button('O', **bw), sg.Button('P', **bw)],

    [sg.Button('A', **bw), sg.Button('S', **bw), sg.Button('D', **bw), sg.Button("F", **bw), sg.Button('G', **bw),
     sg.Button('H', **bw), sg.Button('J', **bw), sg.Button('K', **bw), sg.Button('L', **bw), sg.Button('Ç', **bw)],

    [sg.Button('Z', **bw), sg.Button('X', **bw), sg.Button('C', **bw), sg.Button("V", **bw), sg.Button('B', **bw),
     sg.Button('N', **bw), sg.Button('M', **bw)]
]

window: object = sg.Window('Jogo da Forca', layout=layout, background_color="#292a21", size=(460, 550),
                           return_keyboard_events=True)

# Atualiza a palavra na Tela Palavra
def atualiza_tela_palavra(palavraTela):
    window['_TELAPALAVRA_'].update(value=palavraTela)


# Atualiza a Tela Forca
def atualiza_tela_forca(erros):
    if len(erros) == 1:
        window['_TELAFORCA_'].update(value="+----+\n" \
                                           "|    :\n" \
                                           "|    O\n" \
                                           "|\n" \
                                           "|\n" \
                                           "|\n")
    if len(erros) == 2:
        window['_TELAFORCA_'].update(value="+----+\n" \
                                           "|    :\n" \
                                           "|    O\n" \
                                           "|    |\n" \
                                           "|\n" \
                                           "|\n")
    if len(erros) == 3:
        window['_TELAFORCA_'].update(value="+----+\n" \
                                           "|    :\n" \
                                           "|   _O\n" \
                                           "|    |\n" \
                                           "|\n" \
                                           "|\n")
    if len(erros) == 4:
        window['_TELAFORCA_'].update(value="+----+\n" \
                                           "|    :\n" \
                                           "|   _O_\n" \
                                           "|    |\n" \
                                           "|\n" \
                                           "|\n")
    if len(erros) == 5:
        window['_TELAFORCA_'].update(value="+----+\n" \
                                           "|    :\n" \
                                           "|   _O_\n" \
                                           "|    |\n" \
                                           "|   /\n" \
                                           "|\n")
    if len(erros) == 6:
        window['_TELAFORCA_'].update(value="+----+\n" \
                                           "|    :\n" \
                                           "|   _O_\n" \
                                           "|    |\n" \
                                           "|   / \\\n" \
                                           "|\n")


# Atualiza a Tela Acertos
def atualiza_tela_acertos(acertos):
    global telaAcertos
    telaAcertos = " ACERTOS: "
    for i in range(0, len(acertos)):
        telaAcertos = telaAcertos + " " + acertos[i]
    window['_TELAACERTOS_'].update(value=telaAcertos)


# Atualiza a Tela Erros
def atualiza_tela_erros(erros):
    global telaErros
    telaErros = " ERROS: "
    for i in range(0, len(erros)):
        telaErros = telaErros + " " + erros[i]
    window['_TELAERROS_'].update(value=telaErros)


# Verifica a letra
def verifica_letra(event):
    global palavraAuxiliar, palavraSecreta, palavraTela, erros, acertos, telaAcertos, telaErros

    if event in palavraSecreta:  # Verifica se a letra digitada está na palavra secreta
        if not event in acertos:  # Verifica se essa letra já não foi digitada
            # Se a letra está na palavra secreta, e não foi digitada ainda, o vetor acertos recebe essa letra
            acertos.append(event)
            atualiza_tela_acertos(acertos)  # Chama a função para atualizar a tela acertos

            for i in range(0, len(palavraSecreta)):
                if event == palavraSecreta[i]:  # Verifica no vetor onde está a letra
                    palavraAuxiliar[i] = palavraSecreta[i]
            palavraTela = ""

            for i in range(0, len(palavraAuxiliar)):
                # Palavra Tela só recebe as letras certas que foram digitas, sem revelar as que ainda não foram
                palavraTela = palavraTela + " " + palavraAuxiliar[i]
            atualiza_tela_palavra(palavraTela)  # Chama a função para atualziar a tela palavra

    else:  # Se a letra digitada não estiver na palavra secreta então...
        if not event in erros:  # Verifica se essa letra já não foi digitada
            # Se a letra não está na palavra secreta, e não foi digitada ainda, o vetor erros recebe essa letra
            erros.append(event)
            # Chama as funções para atualizar a tela forca e tela erros
            atualiza_tela_forca(erros)
            atualiza_tela_erros(erros)


while True:
    event, values = window.read()
    print(event)  # Printa no console a letra digitada

    # Se a janela do jogo fechar, encerra o programa
    if event is None:
        break

    if event in ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ç",
                 "Z", "X", "C", "V", "B", "N", "M"]:
        verifica_letra(event)

    # Se tiver 6 erros no vetor, então fim de jogo, você perdeu
    if len(erros) == 6:
        palavraTela = ""
        for i in range(0, len(palavraSecreta)):
            palavraTela = palavraTela + palavraSecreta[i]
        sg.popup("============VOCÊ PERDEU============\nPalavra correta era: " + palavraTela, title="DERROTA",
                 line_width=60, background_color="#292a21")
        break

    # Se todas as letras digitadas formarem a palavra secreta, então fim de jogo, você venceu
    if palavraAuxiliar == palavraSecreta:
        palavraTela = ""
        for i in range(0, len(palavraSecreta)):
            palavraTela = palavraTela + palavraSecreta[i]
        sg.popup("============VOCÊ VENCEU============\t\t\nPalavra correta é: " + palavraTela, title="VITÓRIA",
                 line_width=60, background_color="#292a21")
        break
