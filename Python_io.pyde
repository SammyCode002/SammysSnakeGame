import random

# Game settings
GRID_SIZE = 20
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SCORE_AREA_HEIGHT = 30  # Additional area for displaying the score

# Initialize snake settings
snake = [(0, 0)]  # Snake starts at the top-left corner
snake_direction = (1, 0)  # Snake moves right initially
food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))  # Random position for the first food

# Color settings
snake_color = (0, 255, 0)  # Green color for the snake

# Game state variables
gameOver = False
showPlayAgainButton = False
score = 0

def setup():
    # Set up the canvas with an additional area for the score
    size(CANVAS_WIDTH, CANVAS_HEIGHT + SCORE_AREA_HEIGHT)

def draw():
    # Main game loop
    frameRate(10)  # Control the game speed

    if gameOver:
        # Show game over screen if the game is over
        draw_game_over_screen()
        if showPlayAgainButton:
            draw_play_again_button()
    else:
        # Handle game updates and rendering
        handle_input()
        update_game()
        render_game()

def handle_input():
    # Update the snake's direction based on key presses
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
    # Update the game state: move the snake, check for collisions
    global snake, food, score, gameOver

    # Calculate new head position
    head_x, head_y = snake[-1]
    dx, dy = snake_direction
    new_head_x = (head_x + dx) % GRID_SIZE
    new_head_y = (head_y + dy) % GRID_SIZE
    new_head = (new_head_x, new_head_y)

    # Check for collisions with the snake itself
    if len(snake) > 1 and new_head in snake[:-1]:
        gameOver = True

    # Check for collisions with the boundaries
    if new_head_x < 0 or new_head_x >= GRID_SIZE or new_head_y < 0 or new_head_y >= GRID_SIZE:
        gameOver = True

    # Add new head to the snake
    snake.append(new_head)

    # Check if the snake eats the food
    if new_head == food:
        # Generate new food and increase score
        food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        score += 1
    else:
        # Remove the last segment of the snake if no food is eaten
        snake.pop(0)

def render_game():
    # Render the game elements: snake, food, score
    # Draw the black background
    background(0, 0, 0)

    # Draw the snake
    fill(snake_color[0], snake_color[1], snake_color[2])
    cell_size = CANVAS_WIDTH / GRID_SIZE
    for segment in snake:
        x, y = segment
        rect(x * cell_size, y * cell_size, cell_size, cell_size)

    # Draw the food
    x, y = food
    fill(255, 0, 0)  # Red color for food
    rect(x * cell_size, y * cell_size, cell_size, cell_size)

    # Draw the score outside the game area
    textSize(24)
    fill(255)  # White color for text
    textAlign(LEFT, TOP)
    text("Score: " + str(score), 10, CANVAS_HEIGHT + 5)

def draw_game_over_screen():
    # Display the game over message
    textSize(32)
    fill(255)
    textAlign(CENTER, CENTER)
    text("Game Over", CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)

    # Display the final score
    textSize(24)
    fill(255)
    textAlign(CENTER)
    text("Score: " + str(score), CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + 40)

    # Show the Play Again button
    global showPlayAgainButton
    showPlayAgainButton = True

def draw_play_again_button():
    # Draw the Play Again button
    button_width = 120
    button_height = 40
    button_x = CANVAS_WIDTH / 2 - button_width / 2
    button_y = CANVAS_HEIGHT / 2 + 80

    fill(255, 0, 0)  # Red color for the button
    rect(button_x, button_y, button_width, button_height)

    textSize(20)
    fill(255)  # White color for text
    textAlign(CENTER, CENTER)
    text("Play Again", CANVAS_WIDTH / 2, button_y + button_height / 2)

def mouseClicked():
    # Handle mouse click events
    global snake_color, gameOver, showPlayAgainButton

    if gameOver and showPlayAgainButton:
        # Check if the click is within the Play Again button
        button_width = 120
        button_height = 40
        button_x = CANVAS_WIDTH / 2 - button_width / 2
        button_y = CANVAS_HEIGHT / 2 + 80

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

# Initialize the game
setup()
