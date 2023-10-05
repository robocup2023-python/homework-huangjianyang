import numpy as np
from math import *
def count(a,b,c):
    return a**2+b**2+c**2

class Point:
    def __init__(self,x,y,z=0) -> None:
        self.x=x
        self.y=y
        self.z=z
        self.getClass='Point'
        print(f'创建了类Point({x},{y},{z})')
    def __del__(self):
        print(f'销毁了类Point({self.x},{self.y},{self.z})')
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})"
    def __add__(self, other):
        if other.getClass=='Point':
            return 'error'
        if other.getClass=='Vector':
            return Point(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other):
        if other.getClass=='Point':
            return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
        if other.getClass=='Vector':
            return Point(self.x-other.x, self.y-other.y, self.z-other.z)
    def __eq__(self, other):
        if other.getClass=='Vector':
            if self.x==other.x and self.y==other.y and self.z==other.z:
                return True
            else:
                return False
        if other.getClass=='Point':
            if count(self.x, self.y, self.z)==count(other.x, other.y, other.z):
                return True
            else:
                return False
    def __lt__(self, other):
        if other.getClass=='Vector':
            return False
        if other.getClass=='Point':
            if count(self.x, self.y, self.z)<count(other.x, other.y, other.z):
                return True
            else:
                return False
    def __mt__(self, other):
        if other.getClass=='Vector':
            return False
        if other.getClass=='Point':
            if count(self.x, self.y, self.z)>count(other.x, other.y, other.z):
                return True
            else:
                return False
    
class Vector:
    def __init__(self,x,y,z=0) -> None:
        self.x=x
        self.y=y
        self.z=z
        self.getClass='Vector'
        print(f'创建了类Vector({x},{y},{z})')
    def __del__(self):
        print(f'销毁了类Vector({self.x},{self.y},{self.z})')
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"
    def __add__(self, other):
        if other.getClass=='Point':
            return Point(self.x+other.x, self.y+other.y, self.z+other.z)
        if other.getClass=='Vector':
            return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other):
        if other.getClass=='Point':
            return Point(self.x-other.x, self.y-other.y, self.z-other.z)
        if other.getClass=='Vector':
            return Vector(self.x-other.x, self.y-other.y, self.z-other.y)
    def __mul__(self, arg):
        a=np.array([self.x, self.y, self.z])
        x=np.array([[1,0,0],[0,cos(arg),sin(arg)],[0,-sin(arg),cos(arg)]])
        y=np.array([[cos(arg),0,-sin(arg)],[0,1,0],[sin(arg),0,cos(arg)]])
        z=np.array([[cos(arg),sin(arg),0],[-sin(arg),cos(arg),0],[0,0,1]])
        a=np.dot(z,a)
        a=np.dot(y,a)
        a=np.dot(x,a)
        return Vector(a[0],a[1],a[2])
    def __truediv__(self, arg):
        a=np.array([self.x, self.y, self.z])
        x=np.array([[1,0,0],[0,cos(arg),-sin(arg)],[0,sin(arg),cos(arg)]])
        y=np.array([[cos(arg),0,sin(arg)],[0,1,0],[-sin(arg),0,cos(arg)]])
        z=np.array([[cos(arg),-sin(arg),0],[sin(arg),cos(arg),0],[0,0,1]])
        a=np.dot(z,a)
        a=np.dot(y,a)
        a=np.dot(x,a)
        return Vector(a[0],a[1],a[2])
    def __eq__(self, other):
        if other.getClass=='Point':
            if self.x==other.x and self.y==other.y and self.z==other.z:
                return True
            else:
                return False
        if other.getClass=='Vector':
            if count(self.x, self.y, self.z)==count(other.x, other.y, other.z):
                return True
            else:
                return False
    def __lt__(self, other):
        if other.getClass=='Point':
            return False
        if other.getClass=='Vector':
            if count(self.x, self.y, self.z)<count(other.x, other.y, other.z):
                return True
            else:
                return False
    def __mt__(self, other):
        if other.getClass=='Point':
            return False
        if other.getClass=='Vector':
            if count(self.x, self.y, self.z)>count(other.x, other.y, other.z):
                return True
            else:
                return False

a=Point(1,2,3)
b=Vector(1,2,3)
print(a+b)
print(a==b)
print(b*0.1)