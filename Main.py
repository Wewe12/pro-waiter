import pygame, sys
from pygame.locals import *

import Sprite
import Player
import Tilemap
import Game

# list which represents textures

textures = {
              0 : pygame.image.load('textures/tile1.png'),
              1 : pygame.image.load('textures/tile1.png'),
              2 : pygame.image.load('textures/tile2.png'),
              3 : pygame.image.load('textures/wall_up2.png'),
              4 : pygame.image.load('textures/wall_up.png'),
              5 : pygame.image.load('textures/wall_low.png'),

           }


# list which represents map

tilemap1 = [
             [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
             [2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2],
             [2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2],
             [2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
	     [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
	     [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
             [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
           ]      

def main():

        # declaration of map, player and objects

        map1 = Tilemap.Tilemap(textures,tilemap1,34,20)

        player = Player.Player(2,4,'textures/kelDn.png','textures/kelUp.png','textures/kelLt.png','textures/kelRt.png',map1)
        
        # tables

        tbl1 = [Sprite.Sprite(3,6,'textures/tableSmall.png'),2,2]
        tbl2 = [Sprite.Sprite(3,12,'textures/tableSmall.png'),2,2]
        tbl3 = [Sprite.Sprite(12,6,'textures/tableSmall.png'),2,2]
        tbl4 = [Sprite.Sprite(12,12,'textures/tableSmall.png'),2,2]
        
        # plants

        pl1 = [Sprite.Sprite(18,6,'textures/flower2.png'),1,1]
        pl2 = [Sprite.Sprite(18,9,'textures/flower2.png'),1,1]
        pl3 = [Sprite.Sprite(18,12,'textures/flower2.png'),1,1]
        pl4 = [Sprite.Sprite(18,15,'textures/flower2.png'),1,1]

        # chairs

        ch1 = [Sprite.Sprite(2,6,'textures/chairRt.png'),1,1]    
        ch2 = [Sprite.Sprite(2,12,'textures/chairRt.png'),1,1]
        
        # door
        
        door = Sprite.Sprite(15,2,'textures/door.png')
        
        objectList = [tbl1,tbl2,tbl3,tbl4,pl1,pl2,pl3,pl4,ch1,ch2]
        
        # some text-window display settings

        # font

        pygame.font.init()
        font = pygame.font.Font(None, 30)
        
        # game clock

        clock = pygame.time.Clock()
        frame_rate = 60
        frame_count = 0

        # let the game begin

        game = Game.Game(map1,player)
        
        # add objects to game

        for element in objectList:
            game.addObject(element[0],element[1],element[2])
        
        game.addObjectOnWall(door)

        # main game loop

        while True:
                # event handling
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
                
                # time counting

                # calculate total seconds
                total_seconds = frame_count // frame_rate

                # divide by 60 to get total minutes
                minutes = total_seconds // 60
 
                # use modulus (remainder) to get seconds
                seconds = total_seconds % 60

                # use python string formatting to format in leading zeros
                output_string = "{0:02}:{1:02}".format(minutes, seconds)
 
                # prepare to blit to the screen
                text = font.render(output_string, True, (255,255,255))

                # update the screen with what we've drawn
                game.display(text)

                # take the next frame
                frame_count += 1

                # limit frames per second
                clock.tick(60)


                

if __name__ == "__main__":
    main()
