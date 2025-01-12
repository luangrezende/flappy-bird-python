# Flappy Bird Game

This is a simple Flappy Bird clone built using Python and Pygame. The game features classic mechanics, where the player controls a bird and tries to navigate through gaps in pipes without crashing.

## Features

- Side-scrolling gameplay with randomly generated pipes.
- Gravity and lift mechanics for realistic bird movement.
- Score tracking for competitive fun.
- A "Game Over" screen displayed for a brief moment before restarting.

## Prerequisites

- Python 3.7+
- Pygame library

## Installation

1. Clone this repository or download the source files.
2. Ensure you have Python and Pygame installed:
   ```bash
   pip install pygame
   ```
3. Place the following image assets in the `assets/` folder:
   - `background-day.png`
   - `bluebird-downflap.png`
   - `pipe-green.png`
   - `gameover.png`

## How to Play

1. Run the game:
   ```bash
   python flappy_bird_game.py
   ```
2. Press the **spacebar** to make the bird flap its wings and ascend.
3. Avoid the pipes to keep the game going.
4. The game restarts automatically upon "Game Over".

## Folder Structure

```
flappy_bird_game/
|
|-- assets/
|   |-- background-day.png
|   |-- bluebird-downflap.png
|   |-- pipe-green.png
|   |-- gameover.png
|
|-- flappy_bird_game.py
|-- README.md
```

## Future Improvements

- Add sound effects for a more immersive experience.
- Include a leaderboard for high scores.
- Implement multiple difficulty levels.

## License

This project is licensed under the MIT License.

---

Enjoy the game and happy flapping! 🐦