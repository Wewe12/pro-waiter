import pygame,sys
from pygame.locals import *
import random

import Sprite
import Player
import Tilemap

class Game():
    #konstruktor gry
    def __init__(self,tilemap,player,objectList):
        self.tilemap = tilemap                              #mapa
        self.player = player                                #gracz
        self.objectList = objectList                        #lista obiektow
        self.inventory = [ 0,0,0 ]                          #[0]mop #[1]puszka #[2]cos
        
        #rozpocznij gre
        pygame.init()
        #wyswietl okno gry
        self.DISPLAYSURF = pygame.display.set_mode((tilemap.mapwidth*tilemap.tilesize + 400,tilemap.mapheight*tilemap.tilesize))
      
           
    #wyswietlanie i odswiezanie okna gry  
    def display(self):
        #rysowanie mapy
        for row in range(self.tilemap.mapheight):
            for column in range(self.tilemap.mapwidth):
                #rysuj w okreslonym miejscu okreslony typ kafelka/obiektu
                self.DISPLAYSURF.blit(self.tilemap.textures[self.tilemap.matrix[row][column]],(column*self.tilemap.tilesize,row*self.tilemap.tilesize))

        #rysowanie gracza
        icon = pygame.image.load(self.player.image).convert_alpha()
        self.DISPLAYSURF.blit(icon,(self.player.x*self.tilemap.tilesize,self.player.y*self.tilemap.tilesize))

        #rysowanie wszystkich obiektow
        for i in range(len(self.objectList)):
            icon = pygame.image.load(self.objectList[i].image).convert_alpha()
            #rysuj w okreslonym miejscu okreslony obiekt z listy
            self.DISPLAYSURF.blit(icon,(self.objectList[i].x*self.tilemap.tilesize,self.objectList[i].y*self.tilemap.tilesize))
        
        #odswiezanie widoku
        pygame.display.update()

    #funkcja obslugujaca zdarzenia w grze
    # def handle_events(self,message):
    #         #reakcja na zdarzenia
    #         if message == 'prawo':
    #             self.player.image = self.player.texture_right
    #             if (self.player.collision(self.tilemap,'right')):
    #                 #zmiana pozycji x gracza
    #                 self.player.move('right')
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aMove)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aMove[number] + ' w prawo'
    #             else:
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aMoveF)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aMoveF[number]
                    
    #         #poruszanie w lewo
    #         elif message == 'lewo':
    #             self.player.image = self.player.texture_left
    #             if (self.player.collision(self.tilemap,'left')):
    #                 #zmiana pozycji x gracza
    #                 self.player.move('left')
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aMove)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aMove[number] + ' w lewo'
    #             else:
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aMoveF)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aMoveF[number]
                                     
    #         #poruszenie w dol
    #         elif message == 'dol':
    #             self.player.image = self.player.texture_down
    #             if (self.player.collision(self.tilemap,'down')):
    #                 #zmiana pozycji y gracza
    #                 self.player.move('down')
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aMove)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aMove[number] + ' w dol'
    #             else:
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aMoveF)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aMoveF[number]
                                       
    #         #poruszenie w gore
    #         elif message == 'gora':
    #             self.player.image = self.player.texture_up
    #             if (self.player.collision(self.tilemap,'up')):
    #                 #zmiana pozycji y gracza
    #                 self.player.move('up')
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aMove)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aMove[number] + ' w gore'
    #             else:
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aMoveF)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aMoveF[number]

    #         #szybko do kosza
    #         elif message == 'kosz':
    #             while self.player.x > 1 or self.player.y > 5:
    #                 if self.player.x > 1:
    #                     if (self.player.collision(self.tilemap,'left')):
    #                         self.player.image = self.player.texture_left
    #                         self.player.move('left')
    #                 elif self.player.y > 5:
    #                     if (self.player.collision(self.tilemap,'up')):
    #                         self.player.image = self.player.texture_up
    #                         self.player.move('up')
    #             self.clear_text()
    #             output = 'Juz biegne do kosza!'

    #         #rozgladanie sie
    #         elif message == 'rozejrzwsz':
    #             objectsFound = self.player.lookaround(self.tilemap,'everywhere')
    #             self.clear_text()
    #             if not (objectsFound):
    #                 output = 'Nie, dookola nic nie ma. Jedzmy w inne miejsce.'
    #             else:
    #                 output = 'Widze '
    #                 for i in objectsFound:
    #                     output += i + ', '
    #                 output[-1]="."

    #         elif message == 'rozejrzdol':
    #             objectsFound = self.player.lookaround(self.tilemap,'down')
    #             self.clear_text()
    #             if not (objectsFound):
    #                 output = 'Nie znalazlem niczego! Poszukajmy w innym miejscu.'
    #             else:
    #                 output = 'Widze '
    #                 for i in objectsFound:
    #                     output += i + ', '
    #                 output[-1]="."

    #         elif message == 'rozejrzgora':
    #             objectsFound = self.player.lookaround(self.tilemap,'up')
    #             self.clear_text()
    #             if not (objectsFound):
    #                 output = 'Dookola jest czysto! Nie ma zadnych smieci.'
    #             else:
    #                 output = 'Widze '
    #                 for i in objectsFound:
    #                     output += i + ', '
    #                 output[-1]="."

    #         elif message == 'rozejrzlewo':
    #             objectsFound = self.player.lookaround(self.tilemap,'left')
    #             self.clear_text()
    #             if  not (objectsFound):
    #                 output = 'Nic tu nie ma! Moze poszukamy gdzies indziej?'
    #             else:
    #                 output = 'Widze '
    #                 for i in objectsFound:
    #                     output += i + ', '
    #                 output[-1]="."

    #         elif message == 'rozejrzprawo':
    #             objectsFound = self.player.lookaround(self.tilemap,'right')
    #             self.clear_text()
    #             if not (objectsFound):
    #                 output = 'Nic tu nie ma! Jedzmy gdzies dalej!'
    #             else:
    #                 output = 'Widze '
    #                 for i in objectsFound:
    #                     output += i + ', '
    #                 output[-1]="."
                
    #         #sprzatanie
    #         elif message == 'posprzataj':
    #             #sprzatanie plam
    #             if (self.tilemap.matrix[self.player.y][self.player.x] == 11 and self.inventory[0]==1):
    #                 self.tilemap.matrix[self.player.y][self.player.x] = 1
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aCleanS)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aCleanS[number]
    #                 self.inventory[2]+=1
    #             elif (self.tilemap.matrix[self.player.y][self.player.x] == 11 and self.inventory[0]!=1):
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aCleanNE)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aCleanNE[number]

    #             #sprzatanie puszek
    #             elif self.tilemap.matrix[self.player.y][self.player.x] == 13 and self.inventory[1]==0:
    #                 self.inventory[1]=1
    #                 self.tilemap.matrix[self.player.y][self.player.x] = 1
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aCleanC)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aCleanC[number]
    #             elif(self.tilemap.matrix[self.player.y][self.player.x] == 13 and self.inventory[1]!=0):
    #                 self.clear_text()
    #                 output = 'Nie uniose juz nic wiecej. Moze czas isc do kosza?'
                       
    #             #sprzatanie kurzu
    #             elif self.tilemap.matrix[self.player.y][self.player.x] == 12:
    #                 self.tilemap.matrix[self.player.y][self.player.x] = 1
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aCleanT)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aCleanT[number]
    #                 self.inventory[2]+=1
    #             else:
    #                 #losowanie odpowiedzi
    #                 number = random.randint(0,len(self.player.aCleanF)-1)
    #                 #czyszczenie ekranu + nowy komunikat
    #                 self.clear_text()
    #                 output = self.player.aCleanF[number]

    #         #wyrzucanie puszek
    #         elif message == 'wyrzuc':
    #             if (self.tilemap.matrix[self.player.y][self.player.x] == 14 and self.inventory[1]>0):
    #                 self.inventory[1]=0;
    #                 self.clear_text()
    #                 output='Uff, pozbylem sie tego ciezaru. Puszka jest w koszu!'
    #                 self.inventory[2]+=1
    #             elif(self.tilemap.matrix[self.player.y][self.player.x] == 14 and self.inventory[1]==0):
    #                 self.clear_text()
    #                 output='Tutaj wyrzucamy puszki.'
    #             elif(self.tilemap.matrix[self.player.y][self.player.x] != 14 and self.inventory[1]>0):
    #                 self.clear_text()
    #                 output='Nie chce smiecic! Lepiej isc do kosza.'            
    #             else:
    #                 self.clear_text()
    #                 output='Nie mam nic do wyrzucenia. Moge wyrzucac tylko puszki.'
                                  
    #         #podnoszenie mopa
    #         elif message == 'mop':
    #             if self.tilemap.matrix[self.player.y][self.player.x] == 15:
    #                 self.tilemap.matrix[self.player.y][self.player.x] = 1
    #                 self.inventory[0]=1
    #                 self.clear_text()
    #                 output = 'Moge juz sprzatac plamy.'
    #             else:
    #                 self.clear_text()
    #                 output = 'Nie ma tutaj nic do podniesienia. Poszukaj gdzies indziej.'

    #         #powitanie
    #         elif message == 'powitaj':
    #             self.clear_text()
    #             output = 'Czesc!'

    #         #przedstawienie
    #         elif message == 'przedstaw':
    #             self.clear_text()
    #             output = 'Jestem Super Odkurzaczem! Zaraz zrobimy tutaj porzadek!'

    #         #pomoc
    #         elif message == 'pomoc':
    #             self.clear_text()
    #             output = 'Musisz uzyc jakiegos czasownika. Inaczej Cie nie zrozumiem.'
    #         else:
    #             self.clear_text()
    #             output = 'Nie rozumiem! Musisz inaczej sformulowac polecenie!'

    #         #sprawdzanie czy zakonczyc gre
    #         if self.inventory[2] >= 12:
    #             self.clear_text()
    #             output = "Wygrales! Gratulacje!"
    #         return output

    #funkcja czyszczaca ekran z tekstu
    # def clear_text(self):
    #     self.DISPLAYSURF.fill((0,0,0))
       
