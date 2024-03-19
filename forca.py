import random

# Lista de palavras
palavras = {
    "frutas": ["banana", "uva", "morango", "abacaxi", "laranja"],
    "carros": ["fusca", "mustang", "camaro", "gol", "corolla"],
    "objetos": ["cadeira", "mesa", "computador", "telefone", "copo"]
}

# Função para escolher uma palavra aleatória de uma categoria
def escolher_palavra(categoria):
    lista_palavras = palavras.get(categoria, [])
    if lista_palavras:
        return random.choice(lista_palavras)
    else:
        return None

# Função para inicializar a lista de palavras a serem adivinhadas
def iniciar_palavra_escondida(palavra):
    return ["_" for _ in palavra]

# Função para verificar se uma letra está na palavra e atualizar a lista de adivinhação
def checa_letra(hidden, guess, letter):
    is_letter = False
    for i, char in enumerate(hidden):
        if char == letter:
            guess[i] = letter
            is_letter = True
    return guess, is_letter

# Função para verificar se todas as letras foram adivinhadas
def todas_letras_adivinhadas(guess):
    return "_" not in guess

# Função para desenhar o enforcado
def desenhar_enforcado(erros):
    partes_corpo = ["0", "/", "|", "\\", "/", "\\"]
    return partes_corpo[:erros]

# Função para mostrar letras já escolhidas
def letras_escolhidas(letras):
    return ", ".join(letras)

# Fluxograma:
# Iniciar
# Escolher uma categoria
# Escolher palavra aleatória dessa categoria
# Inicializar lista de adivinhação
# Enquanto erros < 6 e "_" in guess:
#     Mostrar lista de letras escolhidas
#     Pedir uma letra
#     Se letra já foi escolhida, pedir outra
#     Verificar se a letra está na palavra
#     Se sim, atualizar a lista de adivinhação
#     Se não, incrementar os erros e desenhar o enforcado
# Mostrar resultado (ganhou ou perdeu)

# Função principal do jogo
def jogo_forca():
    erros = 0
    letras_escolhidas_lista = []
    categoria = input("Escolha uma categoria (frutas, carros, objetos): ").lower()
    palavra = escolher_palavra(categoria)
    if palavra is None:
        print("Categoria inválida!")
        return

    hidden = iniciar_palavra_escondida(palavra)
    print("Adivinhe a palavra:", " ".join(hidden))

    while erros < 6 and not todas_letras_adivinhadas(hidden):
        print("Letras escolhidas:", letras_escolhidas(letras_escolhidas_lista))
        letra = input("Escolha uma letra: ").lower()
        if letra in letras_escolhidas_lista:
            print("Você já escolheu essa letra. Escolha outra.")
            continue

        letras_escolhidas_lista.append(letra)

        guess, is_letter = checa_letra(palavra, hidden, letra)
        if is_letter:
            print("Letra correta!")
        else:
            erros += 1
            print("Letra errada! Você cometeu {} erros.".format(erros))
            print("Desenho do enforcado:", " ".join(desenhar_enforcado(erros)))

        print("Adivinhe a palavra:", " ".join(guess))

    if todas_letras_adivinhadas(hidden):
        print("Parabéns! Você adivinhou a palavra:", palavra)
    else:
        print("Você perdeu! A palavra era:", palavra)

# Teste do código para cinco rodadas do jogo
for _ in range(5):
    print("\n*** Nova Rodada ***\n")
    jogo_forca()