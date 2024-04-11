import pygame


class Point:  # make object point (character)
    def __init__(self, x, y, radius, speed):  # initialize attributes
        self.x = x  # x coordinate
        self.y = y  # y coordinate
        self.radius = radius  # radius
        self.speed = speed  # speed


class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)


class Game:
    def __init__(self):
        self.point = Point(320, 240, 10, 5)
        self.screen = pygame.display.set_mode((640, 480))
        self.walls = [Wall(100, 100, 200, 10), Wall(300, 200, 10, 100)]

    def move_point(self, dx=0, dy=0):
        old_x, old_y = self.point.x, self.point.y
        self.point.x += dx
        self.point.y += dy
        if self.check_wall_collision() or not self.check_boundaries():
            self.point.x, self.point.y = old_x, old_y

    def check_wall_collision(self):
        point_rect = pygame.Rect(self.point.x - self.point.radius, self.point.y - self.point.radius, self.point.radius * 2, self.point.radius * 2)
        return any(wall.rect.colliderect(point_rect) for wall in self.walls)

    def check_boundaries(self):
        if self.point.x - self.point.radius < 0 or self.point.x + self.point.radius > 640:
            return False
        if self.point.y - self.point.radius < 0 or self.point.y + self.point.radius > 480:
            return False
        return True

    def actions(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_point(dx=-self.point.speed)
        if keys[pygame.K_RIGHT]:
            self.move_point(dx=self.point.speed)
        if keys[pygame.K_UP]:
            self.move_point(dy=-self.point.speed)
        if keys[pygame.K_DOWN]:
            self.move_point(dy=self.point.speed)

    def rendering(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.circle(self.screen, (255, 255, 255), (self.point.x, self.point.y), self.point.radius)
        for wall in self.walls:
            pygame.draw.rect(self.screen, (255, 0, 0), wall.rect)  # Рисуем стены красным
        pygame.display.flip()
        pygame.time.Clock().tick(120)


    def run(self):  # define the main game loop method
        running = True  # set the game to run
        while running:  # keep running the game loop until 'running' is False
            for event in pygame.event.get():  # process all events in the event queue
                if event.type == pygame.QUIT:  # if the window closure is triggered
                    running = False  # stop the game loop
            self.actions()  # call the 'actions' method to process keyboard inputs
            self.rendering()  # call the 'rendering' method to draw the game state on the screen
        pygame.quit()  # end all pygame modules


game = Game()  # create an instance of the 'Game' class
game.run()  # start the game loop by calling the 'run' method of the game instance
