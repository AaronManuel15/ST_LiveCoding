#!/usr/bin/env python3
import pygame

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} says 'Hello!'")

# Child class
class Bird(Animal):
    def __init__(self, name, image_file):
        super().__init__(name)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.bottom = window_height
        self.speed_walk = 3
        self.speed_fly = 5
        self.is_flying = False
        self.is_walking = True

    def walk(self):
        if self.is_walking:
            self.rect.x += self.speed_walk
            if self.rect.left > window_width:
                self.is_walking = False
                self.is_flying = True
                self.rect.left = -self.rect.width
                self.rect.bottom = window_height // 2

    def fly(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed_fly
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed_fly
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed_fly
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_fly

        # Wrap around the screen
        if self.rect.left > window_width:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = window_width
        if self.rect.top > window_height:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = window_height


    def draw(self, window):
        window.blit(self.image, self.rect)
    
    def talk(self):
        print(f"{self.name} says 'Hello!'")

# Child class
class RoadRunner(Bird):
    def __init__(self, name, image_file):
        super().__init__(name, image_file)
        self.speed_walk = 4
        self.speed_run = 7
        
    def talk(self):
        print(f"{self.name} says 'Beep Beep!'")
    
    def run(self):
        self.rect.x += self.speed_run
        if self.rect.left > window_width:
            self.rect.left = -self.rect.width
    
    def fly(self):
        pass

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Nostalgia Birds")

# Set up colors
white = (255, 255, 255)

# Create objects
bird = Bird("Flappy", "images/bird_1.png")
roadrunner = RoadRunner("Beep-Beep", "images/lilroadrunner.png")

# Game loop
running = True
clock = pygame.time.Clock()
bird.talk()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.is_flying = True
            elif event.key == pygame.K_LEFT:
                bird.rect.x -= bird.speed_walk
            elif event.key == pygame.K_RIGHT:
                bird.rect.x += bird.speed_walk

    # Clear the screen
    window.fill(white)

    # Perform actions
    bird.walk()
    bird.fly()
    bird.draw(window)
    
    roadrunner.run()
    roadrunner.draw(window)

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
