# Layered Matrix Rain Simulator

This Python script creates an enhanced "Matrix-style" digital rain effect in your terminal. It simulates falling streams of characters with multiple layers, each having different speeds and colors. This creates a more dynamic and visually interesting effect reminiscent of the iconic visuals from the Matrix movies.

## Features

- Multiple layers of rain with different properties:
  - A fast, bright green layer for prominent foreground streams
  - A medium-speed green layer for additional depth
  - A slow, white layer for subtle background effects
- Customizable stream length
- Adjustable density and speed for each layer
- Automatic adaptation to your terminal width

## Requirements

This script requires Python 3 and the following external library:
- colorama

To install the required library, run:

```
pip install -r requirements.txt
```

## Usage

To run the Layered Matrix Rain Simulator, execute the script:

```
python matrix_rain.py
```

The simulation will start after a 2-second delay. To stop the simulation, press Ctrl-C.

## Customization

You can adjust the following variables at the beginning of the script to customize the rain effect:

- `MIN_STREAM_LENGTH` and `MAX_STREAM_LENGTH`: Control the length of the character streams
- `STREAM_CHARS`: Characters used in the rain (default is '0' and '1')
- `LAYERS`: A list of dictionaries, each defining a layer with its color, density, and speed


## How it works

1. The script initializes multiple layers, each with its own properties (color, density, speed).
2. In each frame:
   - It updates each layer based on its speed.
   - For each column in a layer, it randomly initiates new streams or continues existing ones.
   - It combines all layers into a single output, with faster layers overwriting slower ones.
3. The result is a deep, dynamic rain effect with varying speeds and colors.

## Extending the Script

You can further enhance the script by:
- Adding more layers with different properties
- Implementing character variations for each layer
- Adding command-line arguments for easy customization

## Troubleshooting

If you encounter any issues with colors, ensure that your terminal supports ANSI color codes. The `colorama` library should handle most compatibility issues automatically.

Enjoy your enhanced Matrix Rain Simulator!