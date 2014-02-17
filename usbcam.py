#!/usr/bin/python

import pygame
import pygame.camera
from pygame.locals import *

import time

from datetime import datetime


class PyImage:
   def __init__(self):
      pygame.init()
      pygame.camera.init()
      self.cam = pygame.camera.Camera("/dev/video0",(1024 ,768))

   def make_title(self):
      now = datetime.now()
      timeStamp = now.strftime('%Y-%m-%d-%H-%M-%S')
      self.title = 'pyImage_%s.jpg' % timeStamp

   def make_image(self):
      self.make_title()
      self.cam.start()
      image = self.cam.get_image()
      pygame.image.save(image, self.title)
      self.cam.stop()

pim = PyImage()

pim.make_image()
