import pygame
from audsrc import *
from audengin import *
nepali_letters = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः', 'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज',
                  'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह']

# Initialize pygame
pygame.init()

# Load the combined audio
pygame.mixer.init()
pygame.mixer.music.load(
    r"C:\Users\aryal\OneDrive\Desktop\voice model\v1\temp\combined_temp.wav")

# Play the combined audio
pygame.mixer.music.play()

# Wait for the sound to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Clean up pygame
pygame.quit()
