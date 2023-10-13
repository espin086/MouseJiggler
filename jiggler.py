import pyautogui
import numpy as np
import time
import keyboard
import logging
import random
import threading

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Get screen size
screen_width, screen_height = pyautogui.size()
logging.info(f"Screen size: {screen_width} x {screen_height}")

# Set the center of the screen as the center of the 2D normal distribution
mean = (screen_width / 2, screen_height / 2)

# Set the standard deviation for x and y coordinates
std_dev_x = screen_width / 6
std_dev_y = screen_height / 6

# Set the parameters for the delay distribution
delay_mean = 12
delay_std_dev = 6

# Set the time lapse for the mouse movement
move_duration = 0.5

# Flag to control the execution of the loop
continue_execution = True


def check_key_press():
    global continue_execution
    keyboard.wait()  # Wait for any key press
    continue_execution = False


# Start a separate thread to monitor key presses
key_thread = threading.Thread(target=check_key_press)
key_thread.start()


# Define a list of commands using lambda expressions
# Define a list of commands using lambda expressions and their descriptions
commands = [
    {
        "command": lambda: pyautogui.hotkey("command", "shift", "]"),
        "description": "Switched to the next tab",
    },
    {
        "command": lambda: pyautogui.moveTo(x, y, duration=move_duration),
        "description": "Moved mouse to position",
    },
    {
        "command": lambda: pyautogui.hotkey("command", "shift", "["),
        "description": "Switched to the previous tab",
    },
]


while continue_execution:
    # Sample x and y coordinates from the 2D normal distribution
    x, y = np.random.multivariate_normal(
        mean, [[std_dev_x**2, 0], [0, std_dev_y**2]]
    )

    # Clamp the values to be within the screen boundaries
    x, y = max(0, min(x, screen_width - 1)), max(0, min(y, screen_height - 1))

    # Choose a random command from the commands list
    random_command = random.choice(commands)

    # Execute the random command
    random_command["command"]()

    # Log the executed command
    logging.info(random_command["description"])

    # Sample a delay from the normal distribution
    delay = np.random.normal(delay_mean, delay_std_dev)

    # Clamp the delay to be non-negative
    delay = max(0, delay)

    # Log the delay
    logging.info(f"Delaying next movement for {delay:.2f} seconds")

    # Delay the next iteration
    time.sleep(delay)

logging.info("Key pressed. Exiting program.")
