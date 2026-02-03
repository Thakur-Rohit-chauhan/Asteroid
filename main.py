import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)
    p1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    af1 = AsteroidField()
    while (True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill("black")
        updatable.update(dt)
        for a in asteroids:
            for s in shots:
                if (s.collides_with(a)):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()
        for a in asteroids:
            if (a.collides_with(p1)):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(dt)

if __name__ == "__main__":
    main()
