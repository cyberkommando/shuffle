# importar o pygame
import pygame
import pygame.freetype

#definir a funçao principal
def main():
    #inicializar o pygame
    pygame.init()
    #criar uma janela com uma resoluçao
    res = (900, 600)
    #criar uma janela e uma superficie a partir da resoluçao anterior
    screen = pygame.display.set_mode(res)
    #carregar a imagem do shuffle
    image = pygame.image.load("shuffle.png")
    #loop do funcionamento do jogo
    while (True):
        #processa os eventos do jogo
        for event in pygame.event.get():
             #verifica se o utilizador fechou a janela
            if (event.type == pygame.QUIT):
                 #sai do shuffle
                exit()
                #preenche a janela com a cor azul escuro
        screen.fill((0, 0, 20))
        
        screen.blit(image, (400, 600))
        #criar rectangulos para as escolhada dificuldade
        pygame.draw.rect(screen, (255, 255, 0), (400, 500, 100, 50), 0)
        pygame.draw.rect(screen, (255, 255, 0), (400, 440, 100, 50), 0)
        pygame.draw.rect(screen, (255, 255, 0), (400, 380, 100, 50), 0)
        pygame.draw.rect(screen, (255, 255, 0), (400, 320, 100, 50), 0)
        pygame.draw.rect(screen, (255, 255, 0), (400, 260, 100, 50), 0)
        pygame.draw.rect(screen, (255, 255, 0), (400, 150, 100, 50), 0)
        
        #escrever em cada rectangulo o grau de dificuldade
        my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
        my_font.render_to(screen, (400, 500), "4 X 3", (255, 255, 0))
        my_font.render_to(screen, (400, 440), "4 X 4", (255, 255, 0))
        my_font.render_to(screen, (400, 380), "5 X 4", (255, 255, 0))
        my_font.render_to(screen, (400, 320), "6 X 5", (255, 255, 0))
        my_font.render_to(screen, (400, 260), "6 X 6", (255, 255, 0))
        my_font.render_to(screen, (400, 150), "EXIT", (255, 255, 0))
        
        #colocar musica
        pygame.mixer.music.load('Free Background Music For Gaming Videos - No Copyright.mp3')
        pygame.mixer.music.play(-1)


