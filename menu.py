from gameloop import *




class Iniciar_jogo(pygame.sprite.Sprite,fisica):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = fisica.load_png('novojogo.png')
        self.screen = pygame.display.get_surface()
        self.rect.center = self.screen.get_rect().center
        self.valor=1
        self.screen.blit(self.image,(self.screen.get_rect().centerx - self.image.get_rect()[2]/2,self.screen.get_rect().centery - self.image.get_rect()[3]/2))
        

    def update(self, a):

        if((a==True) and (self.valor==1)):
            self.image, self.rect = fisica.load_png('Novojogoclickado.png')
            self.screen = pygame.display.get_surface()
            self.rect.center = self.screen.get_rect().center
            self.area = self.screen.get_rect()
            self.valor=2
            self.screen.blit(self.image,(self.screen.get_rect().centerx - self.image.get_rect()[2]/2,self.screen.get_rect().centery - self.image.get_rect()[3]/2))
          
        else:
            if(self.valor==2 and a ==False):
                self.image, self.rect = fisica.load_png('novojogo.png')
                self.screen = pygame.display.get_surface()
                self.rect.center = self.screen.get_rect().center
                self.area = self.screen.get_rect()
                self.valor=1
                self.screen.blit(self.image,(self.screen.get_rect().centerx - self.image.get_rect()[2]/2,self.screen.get_rect().centery - self.image.get_rect()[3]/2))

class instancia_mapa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = fisica.load_png('mapaWar.png')
        self.screen = pygame.display.get_surface()
        self.rect.center = self.screen.get_rect().center
        self.valor=1
        self.screen.blit(self.image,(0,0))


    def update(self, a):
        pass


class Menu:

    def button(screen, position, text):
        font = pygame.font.SysFont("Comic Sans MS", 50)
        text_render = font.render(text, 1, (255, 0, 0))
        x, y, w, h = text_render.get_rect()
        x, y = position
        pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
        pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
        pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
        return screen.blit(text_render, (x, y))



    def __init__(self):

        pygame.init()
        pygame.font.init()
        Fonte = pygame.font.SysFont('Comic Sans MS', 30)


        #criação da tela
        size = width, height = 1600 ,  900
        speed = [2, 2]
        black = 0, 0, 0
        screen = pygame.display.set_mode(size)

        #pixelando o plano de fundo
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0 ))

        screen.blit(background, (0, 0))

        map= None
        novo_jogo= Iniciar_jogo()
        botoes=None
        while True:
            for event in pygame.event.get():
                if(novo_jogo != None):
                    if(pygame.Rect.collidepoint(novo_jogo.rect, pygame.mouse.get_pos())):
                        novo_jogo.update(True)
                        if(pygame.mouse.get_pressed(num_buttons=3)[0]== True):
                            map = instancia_mapa()
                            pygame.display.flip()
                            novo_jogo = None
                            quad1=Menu.button (screen,(1096,0), "1 Jogador")
                            quad2=Menu.button (screen,(1296,0), "2 Jogadores")
                            pygame.display.flip()


                    else:
                        novo_jogo.update(False)
                else:
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        if quad1.collidepoint(pygame.mouse.get_pos()):
                            game = GameLoop(1)
                            game.start()
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        if quad2.collidepoint(pygame.mouse.get_pos()):
                            game = GameLoop(2)
                            game.start()

                if event.type == QUIT:
                    return
            pygame.display.flip()
Menu()
        

