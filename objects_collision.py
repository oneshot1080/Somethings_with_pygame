import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Create a clock
clock = pygame.time.Clock()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Simulation")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define object properties
object1_rect = pygame.Rect(100, 300, 100, 100)
object2_rect = pygame.Rect(600, 300, 100, 100)
object1_color = WHITE
object2_color = WHITE

# Define object velocities
object1_velocity = [2, 0]  # Moving right
object2_velocity = [-2, 0] # Moving left

# Define object masses
object1_mass = 2  
object2_mass = 1  

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update object positions
    object1_rect = object1_rect.move(object1_velocity)
    object2_rect = object2_rect.move(object2_velocity)

    # Check for collision with window boundaries and handle bouncing
    if object1_rect.left < 0 or object1_rect.right > WIDTH:
        object1_velocity[0] *= -1
    if object1_rect.top < 0 or object1_rect.bottom > HEIGHT:
        object1_velocity[1] *= -1
    if object2_rect.left < 0 or object2_rect.right > WIDTH:
        object2_velocity[0] *= -1
    if object2_rect.top < 0 or object2_rect.bottom > HEIGHT:
        object2_velocity[1] *= -1

    # Check for collision between objects
    if object1_rect.colliderect(object2_rect):
        # Calculate new velocities based on elastic collision formula
        v1x = object1_velocity[0]
        v1y = object1_velocity[1]
        v2x = object2_velocity[0]
        v2y = object2_velocity[1]

        m1 = object1_mass  # Mass of object 1
        m2 = object2_mass  # Mass of object 2

        # Calculate new velocities for object 1
        object1_velocity[0] = ((v1x * (m1 - m2)) + (2 * m2 * v2x)) / (m1 + m2)
        object1_velocity[1] = ((v1y * (m1 - m2)) + (2 * m2 * v2y)) / (m1 + m2)

        # Calculate new velocities for object 2
        object2_velocity[0] = ((v2x * (m2 - m1)) + (2 * m1 * v1x)) / (m1 + m2)
        object2_velocity[1] = ((v2y * (m2 - m1)) + (2 * m1 * v1y)) / (m1 + m2)

        # Move objects slightly apart to avoid sticking
        dx = object1_rect.centerx - object2_rect.centerx
        dy = object1_rect.centery - object2_rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        overlap = (object1_rect.width + object2_rect.width) / 2 - distance
        if overlap > 0:
            object1_rect.x += overlap * dx / distance
            object1_rect.y += overlap * dy / distance
            object2_rect.x -= overlap * dx / distance
            object2_rect.y -= overlap * dy / distance

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, object1_color, object1_rect)
    pygame.draw.rect(screen, object2_color, object2_rect)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
