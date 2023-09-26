from scripts.default.object import *

class Player(Object):

    def __init__(self, screenSize: tuple = ..., size: tuple = ..., imagePaths=..., surfaceSize: tuple = None, screenPosition: tuple = None, show=True):

        self.screenSize = screenSize
        self.movSpeed = 5
        self.velocity = pygame.math.Vector2()

        position = (screenSize[0] - size[0]) / 2, (screenSize[1] - size[1]) / 2

        super().__init__(position, size, imagePaths, surfaceSize, screenPosition, show)

    def HandleEvents(self, event, mousePosition):

        pass

    def MoveMap(self, map):

        velocity = self.GetVelocity()
        self.playerVelocity = pygame.math.Vector2()
        mapVelocity = pygame.math.Vector2()

        if velocity.x > 0:

            if map.rect.x < 0:

                mapVelocity.x = velocity.x

            else:

                map.rect.x = 0

                if self.rect.x > 0:

                    self.playerVelocity.x = -velocity.x

                else:

                    self.rect.x = 0

        elif velocity.x < 0:

            if map.rect.x > -map.width + self.screenSize[0]:

                mapVelocity.x = velocity.x

            else:

                map.rect.x = -map.width + self.screenSize[0]

                if self.rect.x < self.screenSize[0]:

                    self.playerVelocity.x = -velocity.x

                else:

                    self.rect.x = self.screenSize[0]

        if velocity.y > 0:

            if map.rect.y < 0:

                mapVelocity.y = velocity.y

            else:

                map.rect.y = 0

                if self.rect.y > 0:

                    self.playerVelocity.y = -velocity.y

                else:

                    self.rect.y = 0

        elif velocity.y < 0:

            if map.rect.y > -map.height + self.screenSize[1]:

                mapVelocity.y = velocity.y

            else:

                map.rect.y = -map.height + self.screenSize[1]

                if self.rect.y < self.screenSize[1]:

                    self.playerVelocity.y = -velocity.y
                
                else:

                    self.rect.y = self.screenSize[1]

        map.rect.center += mapVelocity
        self.rect.center += self.playerVelocity

    def GetVelocity(self):

        keys = pygame.key.get_pressed()

        self.direction = pygame.math.Vector2()

        if keys[pygame.K_d]:

            self.direction.x = -1

        elif keys[pygame.K_a]:

            self.direction.x = 1

        else:

            self.direction.x = 0

        if keys[pygame.K_w]:

            self.direction.y = 1

        elif keys[pygame.K_s]:

            self.direction.y = -1

        else:

            self.direction.y = 0

        if self.direction.magnitude() != 0:

            self.direction = self.direction.normalize()

        return self.direction * self.movSpeed


