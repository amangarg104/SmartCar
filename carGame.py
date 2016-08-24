# -*- coding: utf-8 -*-
# @Author: Amar Prakash Pandey
# @Date:  
# @Email: amar.om1994@gmail.com  
# @Github username: @amarlearning
# @Last Modified date:  
# MIT License. You can find a copy of the License
# @http://amarlearning.mit-license.org

# import library here
import pygame
import time
import random
from os import path

# Pygame module initialised 
pygame.init()

# constants are defined
display_width = 700
display_height = 600

grass_width = 170
grass_height = 600

border_width = 30
border_height = 600

# Material color init
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
grey = (211,211,211)

# Folder path init
assets = path.join(path.dirname(__file__), 'assets')
extras = path.join(path.dirname(__file__), 'extras')

# Init images & sounds
gameIcon = pygame.image.load(path.join(assets + '/gameicon.png'))

# Game windown, caption initialised
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SmartCar')

pygame.display.update()

# Game icon init
pygame.display.set_icon(gameIcon)
gameplay = True

# Heart starts beating, Don't stop it!
while gameplay:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameplay = False
		else:
			print event

	# Game basic design init [Left side]
	pygame.draw.rect(gameDisplay, green, (0, 0, grass_width, grass_height))
	pygame.draw.rect(gameDisplay, grey, (grass_width, 0, border_width, border_height))

	# Game basic design init [Right side]
	pygame.draw.rect(gameDisplay, green, (display_width - grass_width, 0, grass_width, grass_height))
	pygame.draw.rect(gameDisplay, grey, (display_width - grass_width - border_width, 0, border_width, border_height))

	pygame.display.update()


# You will win, try one more time. Don't Quit.
pygame.quit()

# you can signoff now, everything looks good!
quit()