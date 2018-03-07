# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:04:47 2018

@author: Student
"""
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GRAY     = ( 127, 127, 127)
BROWN    = ( 165,  42,  42)

import pygame
import math
from vec2d import Vec2d

class Matter:
    def __init__(self, mass, center, vel):
        self.vel = vel
        self.mass = mass
        self.center = center
        self.mom = self.vel * self.mass
        self.force = Vec2d(0,0)
        self.color = GRAY
    
    def update_force(self, force):
        self.force = force
        #print("ForceX", self.force.x, "ForceY", self.force.y)
    def remove_force(self, force):
        self.force -= force
    
    def update_mom(self, dt):
        self.mom += self.force*dt
    def update_vel(self):
        self.vel.copy_in(self.mom/self.mass)
    def update_pos(self, dt):
        self.center += self.vel*dt
    def update(self, dt):
        self.update_mom(dt)
        self.update_vel()
        self.update_pos(dt)
        
        
class Planet(Matter):
    def __init__(self, vel, center, radius, density = None, mass = None):
        #Ensure mass, radius, and density are constraining each other properly.
        if density is None:
            if mass is None:
                density = 100
                mass = density * (math.pi*radius**2)
            else:
                density = mass / (math.pi * radius**2)
        else:
            if mass is None:
                mass = density * (math.pi * radius**2)
            else:
                if(not mass == density * (math.pi * radius**2)):
                    mass == density * (math.pi * radius**2)

        Matter.__init__(self, mass, center, vel)    #Call parent constructor
        self.radius = radius
       
        self.density = density
        self.color = RED
        
    def setColor(self, color):
        self.color = color
    
    def draw(self, screen, coords):
        pygame.draw.circle(screen, self.color, 
                           coords.pos_to_screen(self.center).int(), 
                           int(coords.scalar_to_screen(self.radius)), 0)
        