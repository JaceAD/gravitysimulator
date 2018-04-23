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
def calculateCollision(pl1, pl2):
    
    if(pl1.center.get_distance(pl2.center) < pl1.radius + pl2.radius):
        m1 = pl1.mass
        m2 = pl2.mass
        e = 0
        r = pl2.center - pl1.center
        
        u = 1/((1/m1) + (1/m2))
        
        v1 = pl1.vel
        v2 = pl2.vel
        
        w1 = pl1.angvel
        w2 = pl2.angvel
        theta1 = pl1.angle
        theta2 = pl2.angle
        
        
        
        n = (pl2.center - pl1.center).normalized()
        d = pl1.radius + pl2.radius - (pl1.center - pl2.center).mag()
        L = u*r.cross(v2 - v1)
        Jang = -d * L/(r.mag()*(r.mag()+d)) * n.perpendicular()
        pl1.mom -= Jang
        pl2.mom += Jang
        pl1.center = pl1.center - (u/m1)*d*n
        pl2.center = pl2.center + (u/m2)*d*n
        
        pl1.update_vel()
        pl2.update_vel()
        
        
        
        t = n.perpendicular()
        vt = (v1 - v2).dot(t) - (pl1.radius*w1) - (pl2.radius * w2)
        
        Jn = -(1+e)*u*((v1 - v2).dot(n))
        if (Jn > 0):
            rj = pl1.center - pl1.radius*n
            mt = 1/((1/m1) + (pl1.radius**2 / pl1.moment) + (1/m2) + (pl2.radius**2 / pl2.moment))
            Jt = -mt*vt
            mu = 0.2
            
            
            
            if (abs(Jt) > mu * abs(Jn)):
                Jt *= (mu * abs(Jn))/abs(Jt) 
            
            J = Jn*n + Jt*t
            
            pl1.impulse(J, rj)
            pl2.impulse(J * -1, rj)
            
#            pl1.mom += J * n
#            pl2.mom -= J * n
#            pl1.update_vel()
#            pl2.update_vel()
            
def calculateWallCollision(obj, wall):
    R = obj.radius;
    n = wall.normal;
    d = R - (n.dot(obj.center - wall.end1))
    tangent = n.perpendicular_normal()
    if (d > 0):
        m = obj.mass
        u = m
        v1 = obj.vel
        J = 1.6*u*((v1).dot(n))
        obj.center = obj.center + (u/m)*d*n
        if(J < 0):
            obj.mom -= J*n
        Fric = -obj.mass * obj.vel.dot(tangent)
        cf = 0.75
        if(abs(Fric) > cf * J):
            ratio = cf * J/abs(Fric)
            Fric *= ratio
        else:
            ratio = 1
        
        ratio *= obj.vel.dot(tangent)/obj.vel.dot(n)
        
        obj.mom -= Fric * tangent
