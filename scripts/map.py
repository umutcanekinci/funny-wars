#region #-# Import Packages #-#

import pygame
from scripts.default.object import Object
from scripts.default.image import GetImage
from scripts.default.path import *

#endregion


class Tile(Object):

    def __init__(self, rowNumber, columnNumber, size, imagePaths):
        
        self.position = columnNumber * size[0], rowNumber * size[1]

        super().__init__(self.position, size, imagePaths)


class Map(list[list[Tile]]):

    def __init__(self, mapData, tileSize, tileTypes):

        super().__init__()

        self.data, self.tileSize = mapData, tileSize
        self.rowCount, self.columnCount = len(self.data), len(self.data[0])
        self.size = self.width, self.height = self.columnCount * tileSize[0], self.rowCount * tileSize[1]

        for rowNumber, row in enumerate(self.data):

            newRow = []

            for columnNumber, column in enumerate(row):

                newTile = Tile(rowNumber, columnNumber, self.tileSize, {"Normal" : ImagePath(tileTypes[column])})
                
                newRow.append(newTile)

            self.append(newRow)

        self.Render()

    def HandleEvents(self, event, mousePosition):

        pass

    def Render(self):

        self.surface = pygame.Surface(self.size)
        self.rect = self.surface.get_rect(topleft = (0, 0))

        for row in self:

            for column in row:

                column.Draw(self.surface)

    def Draw(self, surface):


        surface.blit(self.surface, self.rect)


