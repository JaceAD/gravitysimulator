# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 12:48:17 2018

@author: Student
"""
import pygame
from vec2d import Vec2d
from coords import Coords
import ForceCalculator
from Matter import Planet

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GRAY     = ( 127, 127, 127)

def main():
    pygame.init()
 
    width = 1200
    height = 800
    
    screen = pygame.display.set_mode([width,height])
    screen_center = Vec2d(width/2, height/2)
    coords = Coords(screen_center.copy(), 1, True)
    # ^ Center of window is (0,0), scale is 1:1, and +y is up
     
    coords.zoom_at_coords(Vec2d(0,0), 20)
    # ^Sets camera center
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    planets = [];

    frame_rate = 60
    playback_speed = 4
    dt = playback_speed/frame_rate
    paused = False
    done = False
    while not done:
        gameMouse = pygame.mouse
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Will get the vector for the planet to move on")
            if event.type == pygame.MOUSEBUTTONUP:
                print("Have to send planet in vector from center to mouse")
        
        #If the game is not paused, update the objects in it
        if(not paused):            
            for obj in planets:
                obj.update_force(dt)
        
        screen.fill(BLACK) # wipe the screen
        for obj in planets:
            obj.draw(screen, coords) # draw object to screen
            obj.update(dt)
        
        # --- Update the screen with what we've drawn.
        pygame.display.update()

        # This limits the loop to 60 frames per second
        clock.tick(frame_rate)

    pygame.quit()
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        raise e