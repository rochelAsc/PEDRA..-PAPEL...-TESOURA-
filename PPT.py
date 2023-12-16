import os
import sys
import pygame
import random

dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

pygame.init()

'#CONSTANTES'
tela_altura = 500
tela_largura = 500
claro = (223, 247, 242)  # PALETA DE COR
cinza = (204, 222, 227)  # PALETA DE COR
preto = (0, 0, 0)  # PALETA DE COR
branco = (255, 255, 255)  # PALETA DE COR
mercurio = (196, 222, 255)  # PALETA DE COR
prata = (182, 207, 222)  # PALETA DE COR
opcoes = ['pedra', 'papel', 'tesoura', 'pedra', 'papel', 'tesoura', 'pedra', 'papel', 'tesoura', 'pedra', 'papel', 'tesoura']
escolha_jogador = []  # LISTA, A OPÇÃO DO JOGADOR É INCREMENTADA AO ESCOLHER
resultado = None  # FLAG PARA IDENTIFICAR SE VOCÊ VENCEU, PERDEU OU DEU EMPATE
score = 0  # RECORDE, HIGHSCORE, SCORE, ETC
'#MAIN//DATA'
gamelogo = pygame.image.load("data/gamelogo2.png")  # LOGO
pygame.display.set_icon(gamelogo)
TELA_DISPLAY = pygame.display.set_mode([tela_altura, tela_largura])
pygame.display.set_caption("PEDRA.. PAPEL... TESOURA!!!")  # NOME
fps = pygame.time.Clock()
pygame.font.init()


def message_display(texto, fonte, tamanho, cor, x, y, antialias=True):
    """CRIA UMA MENSAGEM, DADO O TEXTO, A FONTE, TAMANHO, COR E COORDENADAS"""
    # ANTILIAS É O 'MODO' DE RENDERIZAÇÃO DO TEXTO
    pptfont = pygame.font.SysFont(fonte, tamanho)
    frase = pptfont.render(texto, antialias, cor)
    TELA_DISPLAY.blit(frase, (x, y))
    # pygame.display.update()


def musica(som, loops):
    """PARA A MUSICA ANTERIOR, SE HOUVER, CARREGA O SOM RECEBIDO E TOCA O SOM O NUMERO ESPECIFICADO POR 'LOOPS'"""
    pygame.mixer.music.load(som)
    pygame.mixer.music.play(loops)


def icone(arquivo, x, y):
    """CRIA UM 'ICONE' DADAS AS COORDENADAS E O RESPECTIVO ARQUIVO"""
    '''AS DIMENSÕES DO ICONE GERADO SÃO AS MESMAS DA IMAGEM RECEBIDA PELA FUNÇÃO'''
    imagem = pygame.image.load(arquivo)
    TELA_DISPLAY.blit(imagem, (x, y))


def button(arquivo, arquivo2, largura, altura, x, y, act):
    """CRIA UM 'BOTÃO' DADAS AS COORDENADAS E O RESPECTIVO ICONE (VISITAR FUNÇÃO 'ICONE()')"""
    clique = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if mouse[0] in range(x, x + largura) and mouse[1] in range(y, y + altura):
        icone(arquivo2, x, y)
        if clique[0] == 1:
            act()
    else:
        icone(arquivo, x, y)


def playerbutton(arquivo, arquivo2, largura, altura, x, y, palavra, act=None):
    """CRIA O BOTÃO DO JOGADOR QUE DESAFIO O COMPUTADOR PARA O JOGO"""
    clique = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    escolha_jogador.append(palavra)
    if x + largura > mouse[0] > x and y + altura > mouse[1] > y:
        icone(arquivo2, x, y)
        if clique[0] == 1:
            act()
    else:
        icone(arquivo, x, y)


def empate():
    global score, resultado
    """TELA DE EMPATE"""
    musica("data/cinemasins.wav", 1)
    delay = pygame.time.get_ticks() + 750
    gameloop_empate = True
    while gameloop_empate:
        taxa = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        TELA_DISPLAY.fill(cinza)
        if taxa >= delay - 400:
            icone("data/tie.png", 122, 215)
            resultado = 'empate'
        if taxa >= delay + (750 * 4):
            homepage()
        pygame.display.update()
        fps.tick(30)


def vitoria():
    global score, resultado
    """TELA DE VITORIA"""
    musica("data/success.wav", 2)
    delay = pygame.time.get_ticks() + 750
    gameloop_vitoria = True
    while gameloop_vitoria:
        taxa = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        TELA_DISPLAY.fill(branco)
        if taxa >= delay:
            icone("data/VITORIA.png", 122, 215)
            resultado = 'vitoria'
        if taxa >= delay + (750 * 2):
            icone("data/score.png", 347, 210)
            icone("data/score.png", (347 + 19), 210)
            icone("data/score.png", (347 + (19 * 2)), 210)
        if taxa >= delay + (750 * 5):
            homepage()
        pygame.display.update()
        fps.tick(30)


def derrota():
    global score, resultado
    """TELA DE DERROTA"""
    musica("data/wasted.wav", 1)
    delay = pygame.time.get_ticks() + 750
    gameloop_derrota = True
    while gameloop_derrota:
        taxa = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        TELA_DISPLAY.fill(preto)
        if taxa >= delay + 1530:
            icone("data/DERROTA.png", 125, 230)
            resultado = 'derrota'
        if taxa >= delay + (1175 * 2):
            icone("data/dot.png", 360, 270)
        if taxa >= delay + (1175 * 3):
            icone("data/dot.png", 360 + 14, 270)
        if taxa >= delay + (1175 * 4):
            icone("data/dot.png", 360 + (14 * 2), 270)
        if taxa >= delay + (1225 * 5):
            homepage()
        pygame.display.update()
        fps.tick(30)


def main():
    """FUNÇÃO PRINCIPAL"""


while main:

    def frontpage():
        """TELA INICIAL"""
        musica("data/menuiniciar.wav", -1)
        while frontpage:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            TELA_DISPLAY.fill(cinza)
            icone("data/NAME.png", 72, 40)
            button("data/SAIR.png", "data/SAIR_H.png", 52, 19, 220, 315, sys.exit)
            button("data/JOGAR.png", "data/JOGAR_H.png", 134, 35, 180, 250, homepage)
            pygame.display.update()
            fps.tick(30)


    def homepage():
        global score, resultado
        """PAGINA PRINCIPAL"""
        # score = 0
        if resultado == 'vitoria':
            score += 1
        elif resultado == 'derrota':
            score = 0
        elif resultado == 'empate':
            score += 0
        musica("data/menujogar.wav", -1)
        while homepage:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            TELA_DISPLAY.fill(cinza)
            icone("data/e_sab.png", 92, 340)
            button("data/VOLTAR.png", "data/VOLTAR2.png", 78, 17, 15, 30, frontpage)
            playerbutton("data/PEDRA_01.png", "data/PEDRA_02.png", 74, 78, 55, 120, "pedra", adversario)
            playerbutton("data/TESOURA_01.png", "data/TESOURA_02.png", 39, 62, 395, 124, "tesoura", adversario)
            playerbutton("data/PAPEL_01.png", "data/PAPEL_02.png", 74, 74, 215, 120, "papel", adversario)
            message_display(f"Highscore: {score}", 'arial', 22, preto, 205, 50, antialias=True)
            pygame.display.update()
            fps.tick(30)


    def adversario():
        """ESCOLHA DO COMPUTADOR"""
        escolha_adversario = random.choice(opcoes)
        if escolha_adversario == escolha_jogador[0]:
            empate()
        elif (escolha_jogador[0] == 'pedra' and escolha_adversario == 'tesoura' or
              escolha_jogador[0] == 'papel' and escolha_adversario == 'pedra' or
              escolha_jogador[0] == 'tesoura' and escolha_adversario == 'papel'):
            vitoria()
        elif (escolha_jogador[0] == 'pedra' and escolha_adversario == 'papel' or
              escolha_jogador[0] == 'papel' and escolha_adversario == 'tesoura' or
              escolha_jogador[0] == 'tesoura' and escolha_adversario == 'pedra'):
            derrota()


    frontpage()
    homepage()

main()
