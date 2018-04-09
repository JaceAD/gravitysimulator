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
                density = 1
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

class Wall(Matter):
    def __init__(self, center, angle, length, thickness):
        Matter.__init__(self, 2000000, center, Vec2d(0,0))
        self.angle = math.radians(angle)
        self.thickness = thickness
        self.length = length
        self.color = WHITE
        self.end1 = Vec2d(0,0)
        self.end2 = Vec2d(0,0)
        self.normal = Vec2d(0,0)
        self.setEndpoints()
        
        
    def setEndpoints(self):
        x1 = self.center.x + self.length * math.cos(self.angle)
        x2 = self.center.x - self.length * math.cos(self.angle)
        y1 = self.center.y + self.length * math.sin(self.angle)
        y2 = self.center.y - self.length * math.sin(self.angle)
        self.end1 = Vec2d(x1, y1)
        self.end2 = Vec2d(x2, y2)
        dx = x2 - x1
        dy = y2 - y1
        self.normal = Vec2d(-dy, dx)
        
    def getEndpoints(self):
        return [self.end1, self.end2]
    
    def draw(self, screen, coords):
        pygame.draw.line(screen, self.color, coords.pos_to_screen(self.getEndpoints()[0]),
                         coords.pos_to_screen(self.getEndpoints()[1]),
                         self.thickness)    
        