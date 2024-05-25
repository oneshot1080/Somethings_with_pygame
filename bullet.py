import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Motion Simulation")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

# Define parameters
initial_speed = 8  # Initial speed of the bullet
initial_angle = 45  # Initial angle of the bullet (in degrees)
initial_height = 100  # Initial height of the bullet above the ground
gravity = 9.81  # Acceleration due to gravity (m/s^2)

# Convert angle to radians
angle_rad = math.radians(initial_angle)

# Calculate initial velocities
initial_velocity_x = initial_speed * math.cos(angle_rad)
initial_velocity_y = -initial_speed * math.sin(angle_rad)  # Negative because y-coordinates increase downwards

# Define bullet properties
bullet_radius = 5
bullet_color = WHITE

# Define coordinate system parameters
axis_thickness = 2
axis_margin = 20
tick_length = 5
tick_frequency = 50

# Define bullet position
bullet_x = axis_margin
bullet_y = HEIGHT - bullet_radius - initial_height  # Start at the specified height above the ground

# Define bullet velocity
bullet_velocity_x = initial_velocity_x
bullet_velocity_y = initial_velocity_y

maxx = 0
# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update bullet position
    bullet_x += bullet_velocity_x
    bullet_y += bullet_velocity_y
    bullet_velocity_y += gravity / 100  # Apply gravity (scaled down for visualization)

    # Check if bullet hits the ground
    if bullet_y >= HEIGHT - bullet_radius - axis_margin:
        # Stop the simulation
        running = False

    # Draw everything
    screen.fill((0, 0, 0))

    # Draw xOy coordinate system (Earth's surface as x-axis)
    pygame.draw.line(screen, GRAY, (axis_margin, HEIGHT - axis_margin), (WIDTH - axis_margin, HEIGHT - axis_margin), axis_thickness)
    pygame.draw.line(screen, GRAY, (axis_margin, HEIGHT - axis_margin), (axis_margin, axis_margin), axis_thickness)

    # Draw ticks on y-axis
    for y in range(HEIGHT - axis_margin - tick_frequency, axis_margin, -tick_frequency):
        pygame.draw.line(screen, GRAY, (axis_margin - tick_length // 2, y), (axis_margin + tick_length // 2, y), axis_thickness)

    # Draw bullet
    pygame.draw.circle(screen, bullet_color, (int(bullet_x), int(bullet_y)), bullet_radius)

    # Draw text showing current position of the bullet
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"({bullet_x - axis_margin:.1f}, {HEIGHT - bullet_y:.1f})", True, WHITE)
    screen.blit(text, (bullet_x + 10, bullet_y + 10))

    pygame.display.update()
    maxx = max(maxx, HEIGHT - bullet_y)
    # Cap the frame rate
    
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
