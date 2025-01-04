import pygame
import random
import time
import sys

# Initialize pygame
pygame.init()

# Initialize pygame mixer for music
pygame.mixer.init()

# Load the song
pygame.mixer.music.load('Blip Stream.mp3')

# Start playing the song once
pygame.mixer.music.play(0)

# Set up display for fullscreen
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('GAME OVER')

# Colors
bg_color = (2, 48, 40)
note_color = (0, 255, 12)
crack_color = (10, 55, 38)
close_button_color = (200, 0, 0)
close_button_hover_color = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Load custom fonts
cyber_alert_font = pygame.font.Font('Cyber Alert.otf', 120)  # Game Over font
medodica_regular_font = pygame.font.Font('MedodicaRegular.otf', 30)  # Main font
cool_font = pygame.font.Font('Cyber Alert.otf', 60)  # Smaller font for score

# Close button
close_button_rect = pygame.Rect(screen_width - 100, 10, 80, 50)

# Music duration
song_length = pygame.mixer.Sound('Blip Stream.mp3').get_length()
start_time = time.time()

# Score
score = 0

# Class for falling notes
class Note:
    def __init__(self, x, y, speed, text, player_side=False):
        self.x = x
        self.y = y
        self.speed = speed
        self.text = medodica_regular_font.render(text, True, note_color)
        self.rect = self.text.get_rect(center=(self.x, self.y))
        self.text_content = text
        self.cracked = False
        self.pieces = []
        self.player_side = player_side

    def update(self):
        if not self.cracked:
            self.y += self.speed
            self.rect.y = self.y
        else:
            # Update pieces if cracked
            for piece in self.pieces:
                piece['y'] += self.speed
                piece['rect'].y = piece['y']

    def draw(self, screen):
        if not self.cracked:
            screen.blit(self.text, self.rect)
        else:
            # Draw the cracked pieces (halves)
            for piece in self.pieces:
                screen.blit(piece['text'], piece['rect'])

    def crack(self):
        if not self.cracked:
            self.cracked = True

            # Split the note into two halves
            top_text = medodica_regular_font.render(self.text_content[:len(self.text_content)//2], True, crack_color)
            bottom_text = medodica_regular_font.render(self.text_content[len(self.text_content)//2:], True, crack_color)

            # Set top and bottom pieces
            self.pieces = [
                {'text': top_text, 'x': self.x, 'y': self.y + 20, 'rect': top_text.get_rect(center=(self.x, self.y + 20))},
                {'text': bottom_text, 'x': self.x, 'y': self.y - 10, 'rect': bottom_text.get_rect(center=(self.y, self.x + 10))}
            ]

# Generate notes for the player side
def generate_notes():
    global next_note_time
    text = random.choice(list(key_map.values()))
    x_pos = random.randint(screen_width // 4, screen_width - screen_width // 4)
    notes.append(Note(x_pos, -50, note_speed, text, player_side=True))

    # Set next note time to be random (between 1-3 seconds)
    next_note_time = time.time() + random.uniform(1, 3)

# Key mapping for notes
key_map = {
    pygame.K_p: 'POST',
    pygame.K_g: 'GET',
    pygame.K_i: 'input()',
    pygame.K_t: 'print()'
}

# Game loop variables
running = True
game_over = False
note_speed = 5
next_note_time = time.time() + random.uniform(1, 3)
notes = []

# Main game loop
while running:
    screen.fill(bg_color)

    # Display FPS
    fps = int(pygame.time.get_ticks() / 1000)
    fps_text = medodica_regular_font.render(f"FPS: {fps}", True, white)
    screen.blit(fps_text, (10, 10))

    # Display song timer
    elapsed_time = time.time() - start_time
    timer_text = medodica_regular_font.render(f"Time: {int(elapsed_time)} / {int(song_length)}s", True, white)
    screen.blit(timer_text, (10, 40))

    # Close button
    mouse_pos = pygame.mouse.get_pos()
    if close_button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, close_button_hover_color, close_button_rect)
    else:
        pygame.draw.rect(screen, close_button_color, close_button_rect)
    close_text = medodica_regular_font.render("X Close", True, white)
    screen.blit(close_text, (close_button_rect.x + 10, close_button_rect.y + 5))

    # Check for player input (for cracking notes)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and close_button_rect.collidepoint(event.pos):
            running = False  # Exit on close button click
        elif event.type == pygame.KEYDOWN:
            if event.key in key_map:
                key_text = key_map[event.key]
                for note in notes:
                    # Only crack notes on the player's side when the key is pressed
                    if note.text_content == key_text and not note.cracked and note.player_side:
                        note.crack()

    # Game over logic
    if game_over:
        game_over_text = cyber_alert_font.render(f"GAME OVER!", True, red)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 3))

        score_text = cool_font.render(f"Score: {score}", True, white)
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2))

        pygame.display.update()
        pygame.time.delay(3000)
        running = False  # Auto exit after showing game over

    if not game_over:
        # Generate new notes every few seconds
        if time.time() > next_note_time:
            generate_notes()

        # Update and draw notes
        for note in notes[:]:
            note.update()
            note.draw(screen)

            if note.y > screen_height:
                game_over = True  # Game over if a note falls

        # Update score
        score = int(elapsed_time)

    # Update display
    pygame.display.update()

    # Cap the frame rate to 180 FPS
    pygame.time.Clock().tick(180)

pygame.quit()
sys.exit()
