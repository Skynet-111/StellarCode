import subprocess

def connect(username, password):
    print("Connected successfully")
    

def execute_command(command):
    try:
        # Execute the given command using subprocess.run()
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Print the output and errors, if any
        print("Output:\n", result.stdout)
        print("Errors:\n", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")


def execute_code(code_string):
    try:
        exec(code_string)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    execute_command("python hello.py")


code = """with open('hello.py', 'w') as file:
    file.write('''import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pygame Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define player properties
player_size = 50
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Keep player on screen
    player_x = max(0, min(player_x, screen_width - player_size))
    player_y = max(0, min(player_y, screen_height - player_size))

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

''')
"""

execute_code(code)



