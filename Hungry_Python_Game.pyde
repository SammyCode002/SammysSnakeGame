#Sammy's Snake Game
import random

# Constants
GRID_SIZE = 20
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
BORDER_SIZE = 50  # Size of the border around the canvas

# Variables
snake = [(0, 0)]  # Starting position of the snake
snake_direction = (1, 0)  # Initial direction (right)
food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))  # Random initial food position

# Player's snake color (default: yellow)
snake_color = (0, 255, 0)  # Bright green color (R, G, B)

# Game over flag
gameOver = False
showPlayAgainButton = False

# Score
score = 0

def setup():
    size(CANVAS_WIDTH + 2 * BORDER_SIZE, CANVAS_HEIGHT + 2 * BORDER_SIZE)  # Set the canvas size with border

def draw():
    frameRate(10)  # Set the frame rate to control game speed

    if gameOver:
        draw_game_over_screen()
        if showPlayAgainButton:
            draw_play_again_button()
    else:
        handle_input()
        update_game()
        render_game()

def handle_input():
    global snake_direction
    if keyPressed:
        if keyCode == UP:
            snake_direction = (0, -1)
        elif keyCode == DOWN:
            snake_direction = (0, 1)
        elif keyCode == LEFT:
            snake_direction = (-1, 0)
        elif keyCode == RIGHT:
            snake_direction = (1, 0)

def update_game():
    global snake, food, score, gameOver

    # Move the snake
    head_x, head_y = snake[-1]
    dx, dy = snake_direction
    new_head_x = (head_x + dx) % GRID_SIZE
    new_head_y = (head_y + dy) % GRID_SIZE
    new_head = (new_head_x, new_head_y)

    # Check for collisions
    if len(snake) > 1 and new_head in snake[:-1]:
        gameOver = True

    if new_head_x < 0 or new_head_x >= GRID_SIZE or new_head_y < 0 or new_head_y >= GRID_SIZE:
        gameOver = True

    snake.append(new_head)

    # Check if the snake eats the food
    if new_head == food:
        snake_random = random.Random()
        food = (snake_random.randint(0, GRID_SIZE-1), snake_random.randint(0, GRID_SIZE-1))
        score += 1  # Increase the score when the snake eats food
    else:
        snake.pop(0)

def render_game():
    # Draw the grassy background
    background(150, 255, 150)  # Light green color (R, G, B)

    # Draw the border
    fill(200)
    rect(0, 0, CANVAS_WIDTH + 2 * BORDER_SIZE, BORDER_SIZE)  # Top border
    rect(0, BORDER_SIZE, BORDER_SIZE, CANVAS_HEIGHT)  # Left border
    rect(0, CANVAS_HEIGHT + BORDER_SIZE, CANVAS_WIDTH + 2 * BORDER_SIZE, BORDER_SIZE)  # Bottom border
    rect(CANVAS_WIDTH + BORDER_SIZE, BORDER_SIZE, BORDER_SIZE, CANVAS_HEIGHT)  # Right border

    # Draw the snake
    fill(snake_color[0], snake_color[1], snake_color[2])  # Bright green color (R, G, B)
    for segment in snake:
        x, y = segment
        ellipse((x * (CANVAS_WIDTH / GRID_SIZE)) + BORDER_SIZE + CANVAS_WIDTH / GRID_SIZE / 2,
                (y * (CANVAS_HEIGHT / GRID_SIZE)) + BORDER_SIZE + CANVAS_HEIGHT / GRID_SIZE / 2,
                CANVAS_WIDTH / GRID_SIZE, CANVAS_HEIGHT / GRID_SIZE)

    # Draw the apple as the food
    x, y = food
    cell_size = CANVAS_WIDTH / GRID_SIZE
    apple_x = (x * cell_size) + BORDER_SIZE + cell_size / 2
    apple_y = (y * cell_size) + BORDER_SIZE + cell_size / 2

    # Draw the apple body (red circle)
    fill(255, 0, 0)  # Red color (R, G, B)
    ellipse(apple_x, apple_y, cell_size, cell_size)

    # Draw the apple leaf (green triangle)
    fill(0, 128, 0)  # Green color (R, G, B)
    triangle(
        apple_x - cell_size * 0.2, apple_y - cell_size * 0.6,
        apple_x + cell_size * 0.2, apple_y - cell_size * 0.6,
        apple_x, apple_y - cell_size * 0.9
    )

    # Draw the score
    textSize(24)
    fill(0)
    textAlign(CENTER)
    text("Score: " + str(score), CANVAS_WIDTH / 2 + BORDER_SIZE, BORDER_SIZE - 10)  # Display the score above the border

def draw_game_over_screen():
    textSize(32)
    fill(0)
    textAlign(CENTER, CENTER)
    text("Game Over", CANVAS_WIDTH / 2 + BORDER_SIZE, CANVAS_HEIGHT / 2 + BORDER_SIZE)

    # Draw the final score
    textSize(24)
    fill(0)
    textAlign(CENTER)
    text("Score: " + str(score), CANVAS_WIDTH / 2 + BORDER_SIZE, CANVAS_HEIGHT / 2 + BORDER_SIZE + 40)

    # Set the flag to show the Play Again button
    global showPlayAgainButton
    showPlayAgainButton = True

# Draw the "Play Again" button
def draw_play_again_button():
    button_width = 120
    button_height = 40
    button_x = CANVAS_WIDTH / 2 + BORDER_SIZE - button_width / 2
    button_y = CANVAS_HEIGHT / 2 + BORDER_SIZE + 80

    # Draw the button rectangle
    fill(255)
    rect(button_x, button_y, button_width, button_height)

    # Draw the button text
    textSize(20)
    fill(0)
    textAlign(CENTER, CENTER)
    text("Play Again", CANVAS_WIDTH / 2 + BORDER_SIZE, button_y + button_height / 2)

def mouseClicked():
    global snake_color, gameOver, showPlayAgainButton

    if gameOver and showPlayAgainButton:
        # Check if the click is within the bounds of the "Play Again" button
        button_width = 120
        button_height = 40
        button_x = CANVAS_WIDTH / 2 + BORDER_SIZE - button_width / 2
        button_y = CANVAS_HEIGHT / 2 + BORDER_SIZE + 80

        if button_x < mouseX < button_x + button_width and button_y < mouseY < button_y + button_height:
            # Reset the game state and start a new game
            global snake, snake_direction, food, score
            snake = [(0, 0)]
            snake_direction = (1, 0)
            food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            gameOver = False
            score = 0
            showPlayAgainButton = False

    # Allow the player to click on the canvas to change the snake color
    snake_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

# Call the setup() function to initialize the game
setup()
