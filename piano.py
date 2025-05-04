import pygame
import numpy as np
import simpleaudio as sa

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define piano notes and their corresponding frequencies
notes = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}

# Function to generate a note
def generate_note(frequency, duration):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note_wave = np.sin(frequency * t * 2 * np.pi)
    audio = note_wave * (32767 / np.max(np.abs(note_wave)))
    audio = audio.astype(np.int16)
    return audio

# Function to play a note
def play_note(note):
    frequency = notes[note]
    duration = 1  # seconds
    audio = generate_note(frequency, duration)
    play_obj = sa.play_buffer(audio, 1, 2, 44100)
    play_obj.wait_done()

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                play_note('C')
            elif event.key == pygame.K_s:
                play_note('D')
            elif event.key == pygame.K_d:
                play_note('E')
            elif event.key == pygame.K_f:
                play_note('F')
            elif event.key == pygame.K_g:
                play_note('G')
            elif event.key == pygame.K_h:
                play_note('A')
            elif event.key == pygame.K_j:
                play_note('B')

    # Fill the background
    screen.fill(WHITE)

    # Draw piano keys
    for i, note in enumerate(notes.keys()):
        pygame.draw.rect(screen, BLACK if i % 2 == 0 else WHITE, (i * 100, 0, 100, HEIGHT))
    
    pygame.display.flip()

pygame.quit()