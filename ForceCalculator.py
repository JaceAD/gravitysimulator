# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:03:33 2018

@author: Student
"""
from vec2d import Vec2d
import Matter

#calculates the force of gravity that an object applies on the subject
def calculateGravity(subjectCenter, subjectMass, objectCenter, objectMass, gravitationalConstant):
    
    distanceFrom = objectCenter.get_dist_sqrd(subjectCenter)
    
    distVec = objectCenter - subjectCenter
    normalizedVec = distVec.normalized()
    
    gravityForce = (((gravitationalConstant) * subjectMass * objectMass) / (distanceFrom)) * normalizedVec
    
    #calculate gravitational force here and return as a vec2d
    return gravityForce

def calculateThrust(arrowCenter, arrowTip, thrustAmount):
    
        arrowVec = arrowTip - arrowCenter
        normalizedArrowVec = arrowVec.normalized() 
        thrustForce = normalizedArrowVec * thrustAmount
        
        return thrustForce

def sumForces(forceList):
    vecSum = Vec2d(0,0)
    for force in forceList:
        vecSum = vecSum + force
    return vecSum

def calculateCOM(planets):
    if(len(planets) == 0):
        return Vec2d(0,0)
    else:
        totalMass = 0
        massPos = Vec2d(0,0)
        for planet in planets:
            totalMass += planet.mass
            massPos += planet.mass * planet.center
        return massPos/totalMass
def calculateCOMVel(planets):
    if(len(planets) == 0):
        return Vec2d(0,0)
    else:
        totalMass = 0
        massVel = Vec2d(0,0)
        for planet in planets:
            totalMass += planet.mass
            massVel += planet.mass * planet.vel
        return massVel/totalMass
    
#calculates the force an object planet applies to the subject planet when they are in contact
def calculateCollision(subjectPlanetCenter, subjectPlanetMass, SubjectPlanetVelocity, subjectPlanetRadius, objectPlanetCenter, objectPlanetRadius):
    differenceVec = objectPlanetCenter - subjectPlanetCenter #Vector from subject to object
    lengthOfDifference = differenceVec.get_length()
    if(lengthOfDifference >= subjectPlanetRadius + objectPlanetRadius):
        print("placeholder")
        #Calculate force for collision when they are in contact