import pygame
import os
from audengin import *
from audsrc import *
# Database file path
current_dir = os.path.dirname(os.path.abspath(__file__))
temp_file_path = os.path.join(current_dir, "temp", "temp.wav")

# Initialize pygame
pygame.init()

# Initialize mixer
pygame.mixer.init()

# Load the combined audio
pygame.mixer.music.load(temp_file_path)

# Play the combined audio
pygame.mixer.music.play()

# Wait for the sound to finish playing
clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    clock.tick(100000)

# Clean up pygame
pygame.quit()
