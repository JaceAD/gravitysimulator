# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:03:33 2018

@author: Student
"""
from vec2d import Vec2d

#calculates the force of gravity that an object applies on the subject
def calculateGravity(subjectCenter, subjectMass, objectCenter, objectMass, gravitationalConstant):
    
    distanceFrom = objectCenter.get_dist_sqrd(subjectCenter)
    
    distVec = objectCenter - subjectCenter
    normalizedVec = distVec.normalized()
    
    gravityForce = (((-1 * gravitationalConstant) * subjectMass * objectMass) / (distanceFrom)) * normalizedVec
    
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