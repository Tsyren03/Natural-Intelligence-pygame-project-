import pygame
import sys
import time
from CounterManager import CounterManager
from rooms import rooms

pygame.init()

# Constants
WIDTH, HEIGHT = 1600, 800
GREEN = (68, 214, 44)
font_path = "Orbitron-VariableFont_wght.ttf"
font_size = 28
opening_font_size = 72
font = pygame.font.Font(font_path, font_size)
opening_font = pygame.font.Font(font_path, opening_font_size)
pygame.mixer.init()
pygame.display.set_caption("Natural Intelligence")

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game state
current_room = "start"
game_over = False
opening_screen = True

# Typing effect variables
text = ""
text_index = 0
typing_speed = 0.01  # Adjust the speed of typing (in seconds)
last_character_time = time.time()

counter_manager = CounterManager()  # Create an instance of the CounterManager class

# Load and play the background music
background_music = "sound1.mp3"  # Adjust the file name accordingly
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)  # Play the music in a loop
def format_text_in_box(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)

    formatted_text = "+" + '-' * (max_length + 2) + "+\n"

    for line in lines:
        formatted_text += "| " + line.ljust(max_length) + " \n"

    formatted_text += "+" + '-' * (max_length + 2) + "+"

    return formatted_text


def display_text_in_box(text):
    formatted_text = format_text_in_box(text)
    display_text(formatted_text)


def display_text(text):
    screen.fill((0, 0, 0))
    lines = text.split("\n")
    y = 50
    cursor_x = 50
    cursor_y = y

    for line in lines:
        text_surface = font.render(line, True, GREEN)
        text_rect = text_surface.get_rect()
        text_rect.left = cursor_x
        text_rect.top = cursor_y
        screen.blit(text_surface, text_rect)

        cursor_x = 50
        cursor_y = text_rect.bottom

    pygame.display.flip()


# Function to display opening screen
def process_event(event):
    global game_over, current_room, text, text_index, last_character_time

    if event.type == pygame.QUIT:
        game_over = True
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            game_over = True
        key = pygame.key.name(event.key)
        if key in rooms[current_room]["responses"]:
            response_key = key
            current_response = rooms[current_room]["responses"][response_key]
            current_room = current_response["next_room"]

            # Correct the counter key usage
            counter_key = current_response.get("counter_key", None)
            if counter_key:
                counter_manager.increment_counter(counter_key)

            text = ""
            text_index = 0
            last_character_time = time.time()




def display_opening_screen():
    opening_text = "Natural Intelligence"
    opening_text_surface = opening_font.render(opening_text, True, GREEN)
    opening_text_rect = opening_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(opening_text_surface, opening_text_rect)
    pygame.display.flip()


# Main loop
while opening_screen:
    display_opening_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            opening_screen = False

# Reset game state for the main loop
text = ""
text_index = 0
last_character_time = time.time()

# Reset game state for the main loop

def display_ending_text():
    global game_over, ending_text
    human_count = counter_manager.get_counter("human")
    deviator_count = counter_manager.get_counter("deviator")
    non_human_count = counter_manager.get_counter("non_human")

    # Select the ending text based on the counters
    if human_count >= 2:
        ending_text = rooms["end_game"]["dynamic_text"]["human_ending"]
    elif deviator_count >= 2:
        ending_text = rooms["end_game"]["dynamic_text"]["deviator_ending"]
    elif non_human_count >= 2:
        ending_text = rooms["end_game"]["dynamic_text"]["non_human_ending"]
    else:
        # Default ending text if none of the conditions are met
        ending_text = ""

    # Clear the screen
    screen.fill((0, 0, 0))

    # Display the ending text
    display_text(rooms["end_game"]["text"].format(
        human_count=human_count,
        deviator_count=deviator_count,
        non_human_count=non_human_count,
        ending_text=ending_text
    ))

    pygame.display.flip()  # Update the display

    # Wait for any key press to exit
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                waiting_for_key = False
                game_over = True



counter_manager = CounterManager()
while not game_over:
    for event in pygame.event.get():
        process_event(event)

    current_time = time.time()
    if current_time - last_character_time >= typing_speed:
        if text_index < len(rooms[current_room]["text"]):
            text += rooms[current_room]["text"][text_index]
            text_index += 1
            last_character_time = current_time

    # Clear the screen
    screen.fill((0, 0, 0))

    # Display the current room's description
    if text_index >= len(rooms[current_room]["text"]):
        room_description = text
    else:
        room_description = text

    # Display the text within a box
    display_text_in_box(room_description)

    pygame.display.flip()

    # Check for ending text display
    if current_room == "end_game" and not game_over:
        # Calculate the ending text based on counters
        display_ending_text()

# Quit Pygame
pygame.quit()
sys.exit()