#abrir e reproduzir um audio mp3

import pygame

import pygame
import time

'''def reproduzir_audio(nome_arquivo):
    pygame.mixer.init()
    pygame.mixer.music.load(nome_arquivo)
    pygame.mixer.music.play()

    # Aguarda a reprodução terminar
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Exemplo de uso
nome_arquivo_audio = "/home/cpe-3/Downloads/mpthreetest.mp3"  # Substitua pelo caminho do seu arquivo de áudio
reproduzir_audio(nome_arquivo_audio)'''

pygame.init()
pygame.mixer.music.load('021music.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
        time.sleep(1)

