import pygame
import sys

from configs import WIDTH, HEIGHT
from node import Node
from runner import main


# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pathfinding Algorithms Visualization')

main(screen, WIDTH)
