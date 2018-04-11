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
from Matter import Wall

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GRAY     = ( 127, 127, 127)

newPlanet = None

def main():
    pygame.init()
 
    width = 1200
    height = 800
    
    screen = pygame.display.set_mode([width,height])
    screen_center = Vec2d(width/2, height/2)
    coords = Coords(screen_center.copy(), 1, True)
    # ^ Center of window is (0,0), scale is 1:1, and +y is up
     
    coords.zoom_at_coords(Vec2d(0,0), 2)
    # ^Sets camera center
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    planets = [];

    frame_rate = 60
    playback_speed = 1
    dt = playback_speed/frame_rate
    paused = False
    done = False
    
    mouseClicked = False
    mousePosDown = Vec2d(0,0)
    mousePosUp = Vec2d(0,0)
    
    wall1 = Wall(Vec2d(150, 0), 45, 212, 4)
    wall2 = Wall(Vec2d(-150,0), 315, 212, 4)
    
    print(wall1.normal)
    print(wall2.normal)
    
    while not done:
        gameMouse = pygame.mouse                                #Mouse obj
        mousePosTup = gameMouse.get_pos()                       #Mouse pos in default coordinates as list
        mousePosVec = Vec2d(mousePosTup[0], mousePosTup[1])     #Mouse pos in default coordinates as vec2d
        mouseCoordPos = coords.pos_to_coords(mousePosVec)       #Mouse pos in standardized coords as vec2d
        
        
        
        initVelocity = 0
        
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                paused = True
                if mouseClicked == False:
                    mouseClicked = True
                    mousePosDown = mouseCoordPos    #wiil get the pos of Mouse at first click location
                    print("setting planet")
                    global newPlanet
                    newPlanet = Planet(Vec2d(0,0), mousePosDown, 15)
                
                if mouseClicked == True:
                    mousePosUp = mouseCoordPos  #For drawing initial velocity vector
                    #draw a vector on screen here
                 
            if event.type == pygame.MOUSEBUTTONUP:
                mouseClicked = False
                mousePosUp = mouseCoordPos
                
                initVelocity = mousePosUp - mousePosDown
                print("Vel", initVelocity.x, initVelocity.y)
                initVelocity*= 0.1
                print("Vel", initVelocity.x, initVelocity.y)
                
                initMom = initVelocity * newPlanet.mass
                newPlanet.vel = initVelocity
                newPlanet.mom = initMom
                planets.append(newPlanet)
                #will add new planet to the array of planets with vector of mouse up and mouse click
                paused = False

                print("Have to send planet in vector from center to mouse")
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_0 or pygame.K_KP0:
                    com = ForceCalculator.calculateCOM(planets)
                    comVel = ForceCalculator.calculateCOMVel(planets)
                    for obj in planets:
                        obj.center -= com
                        obj.vel -= comVel
                        obj.mom = obj.vel * obj.mass
        #If the game is not paused, update the objects in it
        if(not paused):
            objLen = len(planets)
            for i in range(0, objLen):
#                forces = []
#                for j in range(0, objLen):
#                    #Calculate a force that each object has on this object and append it to the list of foces acting on it
#                    if(not i==j):
#                        forces.append(ForceCalculator.calculateGravity(planets[i].center, planets[i].mass, planets[j].center, planets[j].mass, 10))
#                    
#                summationForce = ForceCalculator.sumForces(forces)  #Currently result of all gravitational forces from other planets
                summationForce = ForceCalculator.calculateGravity(planets[i].center, planets[i].mass, Vec2d(0, -1000000000), 600000000000000000, 10) #Gravity of "Earth" acting on this "ball"
                planets[i].update_force(summationForce)
            
            for i in range(0, objLen):
                planets[i].update(dt)
            
            #goes through the array of planets to see if they are colliding and if they are then, caclulate the collision
            for i in range(0, objLen):
                for j in range(0, objLen):
                    if(not i==j):
                        ForceCalculator.calculateCollision(planets[i], planets[j])
                ForceCalculator.calculateWallCollision(planets[i], wall1)
                ForceCalculator.calculateWallCollision(planets[i], wall2)
                        
            for i in range(0, objLen):
                planets[i].update(dt)
                     
        screen.fill(BLACK) # wipe the screen
        for obj in planets:
            obj.draw(screen, coords) # draw object to screen
        wall1.draw(screen, coords)
        wall2.draw(screen, coords)
        
        textFont = pygame.font.Font(None,72)
        mousePosSurface = textFont.render("x: " + str(mouseCoordPos.x) + " y: " + str(mouseCoordPos.y), 0, WHITE)
        screen.blit(mousePosSurface, (500,500))
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