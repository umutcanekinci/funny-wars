#-# Importing Packages #-#
from scripts.default.application import Application
from scripts.default.color import *

#-# Game Class #-#
class Game(Application):

    def __init__(self) -> None:
        
        super().__init__("Game", (640, 480), Gray)
