import pygame as pg
from OpenGL.GL import *

class App:
    def __init__(self):
            #initialize python
            pg.init()
            pg.display.set_mode(640,480),pg.OPENGL|pg.DOUBLEBUF)
            self.clock = pg.time.Clock()
            #initialize OpenGL
            glClearColor(0.1,0.2,0.2,1)
