import pygame, sys
from pygame.locals import *

import Sprite
import Player
import Tilemap
import Game

#lista tekstur
textures = {
              0 : pygame.image.load('textures/tile1.png'),
              1 : pygame.image.load('textures/tile1.png'),
              2 : pygame.image.load('textures/tile2.png'),
              3 : pygame.image.load('textures/wall_up2.png'),
              4 : pygame.image.load('textures/wall_up.png'),
              5 : pygame.image.load('textures/wall_low.png'),
              11 : pygame.image.load('textures/stain.png'),
              12 : pygame.image.load('textures/dirt.png'),
              13 : pygame.image.load('textures/can.png'),
              14 : pygame.image.load('textures/tile1.png'),
              15 : pygame.image.load('textures/mop.png')
              #16 : pygame.image.load('textures/')
           }

#lista reprezentujaca mape
# tilemap1 = [
             # [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
             # [2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2],
             # [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
             # [2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2],
             # [2,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,2],
             # [2,14,1,1,1,1,1,1,1,1,1,1,1,1,1,0,2],
             # [2,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,2],
             # [2,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,2],
             # [2,1,1,1,1,1,1,1,1,1,1,1,1,1,15,1,2],
             # [2,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,2],
             # [2,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,2],
             # [2,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,2],
             # [2,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,2],
             # [2,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,2],
             # [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             # [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             # [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
           # ]
tilemap1 = [
             [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
             [2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2],
             [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
             [2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             
             [2,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
			 [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
			 [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
           ]                   

def main():

        #deklaracja mapy,gracza i obiektow
        map1 = Tilemap.Tilemap(textures,tilemap1,34,20)
        player = Player.Player(2,4,'textures/kelDn.png','textures/kelUp.png','textures/kelLt.png','textures/kelRt.png',map1)
        # A = Sprite.Sprite(7,6,'textures/tvset.png')
        # B = Sprite.Sprite(11,2,'textures/bookshelf1.png')
        # B1 = Sprite.Sprite(13,2,'textures/bookshelf1.png')
        # C = Sprite.Sprite(15,2,'textures/bookshelf2.png')
        # D = Sprite.Sprite(2,3,'textures/shelf1.png')
        # E = Sprite.Sprite(4,3,'textures/flower.png')
        # F = Sprite.Sprite(15,9,'textures/flower2.png')
        # F1 = Sprite.Sprite(15,10,'textures/flower2.png')
        # F2 = Sprite.Sprite(15,11,'textures/flower2.png')
        # G = Sprite.Sprite(3,9,'textures/sofa.png')
        A = Sprite.Sprite(3,6,'textures/table.png')
        B = Sprite.Sprite(3,9,'textures/table.png')
        C = Sprite.Sprite(3,12,'textures/table.png')
        D = Sprite.Sprite(3,15,'textures/table.png')
        E = Sprite.Sprite(9,6,'textures/table.png')
        F = Sprite.Sprite(9,9,'textures/table.png')
        G = Sprite.Sprite(9,12,'textures/table.png')
        H = Sprite.Sprite(9,15,'textures/table.png')
        #KWIATKI
        I = Sprite.Sprite(15,6,'textures/flower2.png')
        J = Sprite.Sprite(15,9,'textures/flower2.png')
        K = Sprite.Sprite(15,12,'textures/flower2.png')
        L = Sprite.Sprite(15,15,'textures/flower2.png')
        
        # I = Sprite.Sprite(1,4,'textures/kosz2.png')

        #tablica obiektow
        # objectList = [ A,B,B1,C,D,E,F,F1,F2,G,H,I ]
        objectList = [ A,B,C,D,E,F,G,H,I,J,K,L ]
        #czcionka
        # pygame.font.init()
        # font = pygame.font.Font('xxx.ttf', 18)
        
        #rozpocznij gre
        game = Game.Game(map1,player,objectList)
        while True:
                game.display()
                for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()
                            sys.exit()
                        if event.type == KEYDOWN:
                                if event.key == K_x:
                                    exit()
                                    sys.exit()
                                if event.key == K_UP:
                                        player.move('up')
                                if event.key == K_DOWN:
                                        player.move('down')
                                if event.key == K_RIGHT:
                                        player.move('right')
                                if event.key == K_LEFT:
                                        player.move('left')


                

if __name__ == "__main__":
    main()
