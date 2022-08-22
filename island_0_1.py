#IMPORTS
import numpy as np
import scipy, random, pyglet, math
import matplotlib.pyplot as plt
from PIL import Image

#CONSTANTS

BLACK = (0.0, 0.0, 0.0, 0.0)

#CLASSES

#FUNCTIONS

def gen_circle_points(N = 100, r = 1000, edge = 8):
    pts = np.zeros((N+edge,2))
    for i in range(edge):
        pts[i][0] = r*1.25*np.cos(2*math.pi*i/edge)
        pts[i][1] = r*1.25*np.sin(2*math.pi*i/edge)
    for i in range(N):
        rad = random.random()*r
        arc = random.random()*2*math.pi
        pts[i+edge][0] = rad*np.cos(arc)
        pts[i+edge][1] = rad*np.sin(arc)
    return pts

#MAIN

def main():
    

if __name__ == "__main__":
    main()
