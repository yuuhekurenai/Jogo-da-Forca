import random

import forca

nomes = ['gabriel', 'raissa', 'juliana', 'fabio']
fimdejogo = False

slc_item = random.choice(nomes)
vida = 6
troca_letra = []
for palavra in slc_item:
    troca_letra += "_"
while not fimdejogo:
    player_choice = str(input("Escolha uma letra.")).lower()
    for posicao in range(len(slc_item)):
        letra = slc_item[posicao]
        if letra == player_choice:
            troca_letra[posicao] = letra
            print(troca_letra)
        if player_choice not in troca_letra:
            vida -= 1
            if vida == 0:
                fimdejogo = True
                print("Você perdeu!")
                print(forca.boneco[vida])

            if "_" not in troca_letra:
                fimdejogo = True
                print("Você venceu")
