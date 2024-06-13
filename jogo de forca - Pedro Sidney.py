import random


def escolher_palavra():
    palavras = ['desenvolvimento', 'tecnologia', 'logica', 'programacao', 'tendencias'] 
    return random.choice(palavras)


def exibir_forca(tentativas):
    estagios = [
        '''
           -----
           |   |
               |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        '''
    ]
    print(estagios[tentativas])

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_' for _ in palavra]
    letras_tentadas = []
    tentativas = 0

    
    while tentativas < 6:
        print(' '.join(palavra_oculta))
        letra = input("Digite uma letra: ")

        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1
            exibir_forca(tentativas)

        letras_tentadas.append(letra)

        
        if '_' not in palavra_oculta:
            print("Parabéns, você ganhou!")
            break
        elif tentativas == 6:
            print("Você perdeu. A palavra era " + palavra + ".")

    
    print("Obrigado por jogar!")


jogar()