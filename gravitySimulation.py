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
    
    #Strength of arrow shot. Will be divided by 60, adding roughly 1 to force per second
    powerMeter = 0
    planetMass = 0
    originalThrustVector = Vec2d(0,0)

    frame_rate = 60
    playback_speed = 4
    dt = playback_speed/frame_rate
    done = False
    while not done:
        gameMouse = pygame.mouse
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
#                if(not arrow.getActive()):
#                    #Click and hold for power. Release to shoot
#                    arrow.setCharging(True)
                print("Will get the vector for the planet to move on")
            if event.type == pygame.MOUSEBUTTONUP:
                print("Have to send planet in vector from center to mouse")
#                if(not arrow.getActive()):
#                    arrow.setActive(True)
#                    arrow.setCharging(False)
#                    arrowShootingStart = True
#                    originalThrustVector = ForceCalculator.calculateThrust(arrow.center, arrow.tip, powerMeter)
#                    arrow.update_force(originalThrustVector)
                    
        if(planet.getActive()):
            #calculate all forces that would apply to arrow here
            forces = []
            for planet in planets:
                forces.append(ForceCalculator.calculateGravity(planet.center, planet.mass, planet.center, planet.mass, -10))
            if(arrowShootingTime > 0): #will have to set a boolean that will change to initialize this step
                forces.append(originalThrustVector)
            else:
                #powerMeter = 0 GET the vector from center to mouse.
            forceSum = ForceCalculator.sumForces(forces)
            for obj in planets:
                obj.update_forcew(dt)
            arrow.update_force(forceSum)
            print("Arrow is active")
        else:
            #Aim input here
            mouseTup = gameMouse.get_pos()
            mouseVec = Vec2d(mouseTup[0]-1200, mouseTup[1])
            coordMouseVec = coords.pos_to_screen(mouseVec).int()
            if(arrow.getCharging()):
                powerMeter += 2
            print("Arrow is deactive")

        print("Power Meter:", powerMeter)
            # Drawing
        screen.fill(BLACK) # wipe the screen
        for obj in planets:
            obj.draw(screen, coords) # draw object to screen
            obj.update(dt)
        
        #mouseTup = gameMouse.get_pos()
        #mouseVec = Vec2d(mouseTup[0] - 1200, mouseTup[1])
        #coordMouseVec = coords.pos_to_screen(mouseVec).int()
        #arrow.rotateByMouse(coordMouseVec)
        #mousePosSurface = textFont.render("x: " + str(coordMouseVec[0]) + " y: " + str(coordMouseVec[1]), 0, WHITE)
        #screen.blit(mousePosSurface, (500,500))
        #print("Arrow is deactive")
        
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