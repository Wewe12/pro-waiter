import random
from random import shuffle

class Tilemap:

    # map's constructor

    def __init__(self,textures,matrix,mapwidth,mapheight):
        self.textures = textures  # list of textures
        self.matrix = matrix  # list which represents map
        self.tilesize = 23  # singe tile's size
        self.mapwidth = mapwidth  # map's width
        self.mapheight = mapheight  # map's height
