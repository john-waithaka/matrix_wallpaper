
import random
import shutil
import sys
import time
from colorama import Fore, Style, init

# Initialize colorama
init()

# Constants
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
STREAM_CHARS = ['1', '0']
WIDTH = shutil.get_terminal_size()[0] - 1

# Layer configurations
LAYERS = [
    {"color": Fore.LIGHTGREEN_EX, "density": 0.02, "speed": 0.1},
    {"color": Fore.GREEN, "density": 0.01, "speed": 0.15},
    {"color": Fore.GREEN, "density": 0.005, "speed": 0.05}
]

def create_layer(color, density, speed):
    return {
        "columns": [0] * WIDTH,
        "color": color,
        "density": density,
        "speed": speed,
        "last_update": 0
    }

def update_layer(layer, current_time):
    if current_time - layer["last_update"] >= layer["speed"]:
        layer["last_update"] = current_time
        for i in range(WIDTH):
            if layer["columns"][i] == 0:
                if random.random() <= layer["density"]:
                    layer["columns"][i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
            if layer["columns"][i] > 0:
                layer["columns"][i] -= 1
        return True
    return False

def main():
    print('Press Ctrl-C to quit.')
    time.sleep(2)

    layers = [create_layer(**config) for config in LAYERS]
    
    try:
        while True:
            current_time = time.time()
            output = [' '] * WIDTH
            
            for layer in layers:
                if update_layer(layer, current_time):
                    for i in range(WIDTH):
                        if layer["columns"][i] > 0:
                            output[i] = layer["color"] + random.choice(STREAM_CHARS) + Style.RESET_ALL

            print(''.join(output))
            sys.stdout.flush()
            time.sleep(0.05)  # Small delay for smoother animation

    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()    