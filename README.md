
# Asteroids: Python Edition

A modern reconstruction of the classic arcade hit, built with **Pygame** and managed by **uv**. This version features physics-based movement, procedural asteroid spawning, and a robust event-logging system for gameplay analysis.

## Project Structure

```text
asteroid/
├── main.py              # Entry point for the game
├── player.py            # Player class and controls
├── asteroid.py          # Asteroid class and splitting logic
├── asteroidfield.py     # Asteroid spawning system
├── shot.py              # Projectile class
├── circleshape.py       # Base class for game objects
├── constants.py         # Game configuration
├── logger.py            # Event and state logging
├── pyproject.toml       # Project dependencies
└── README.md            # This file

```

## Features

* **Player Controls**: High-precision rotation and thrust mechanics.
* **Asteroid Physics**: Edge-spawning system with randomized trajectory and velocity.
* **Collision Detection**: Circle-to-circle collision logic for pixel-perfect interaction.
* **Asteroid Splitting**: Dynamic destruction logic where larger asteroids fragment into smaller pieces.
* **Game Logging**: Real-time serialization of game state to JSONL for data analysis.

## Installation

This project requires **Python 3.13+**.

### Using uv (Recommended)

```bash
# Sync dependencies and create virtual environment
uv sync

# Run the game
uv run main.py

```

### Using pip

```bash
# Install dependencies
pip install pygame==2.6.1

# Run the game
python main.py

```

## Game Mechanics

### Controls

| Key | Action |
| --- | --- |
| **W / S** | Move Forward / Backward |
| **A / D** | Rotate Left / Right |
| **SPACE** | Shoot |

### Splitting Logic

When an asteroid is hit by a projectile, it follows a hierarchical destruction path:

* **Large (Radius 60)** → Splits into two Medium asteroids.
* **Medium (Radius 40)** → Splits into two Small asteroids.
* **Small (Radius 20)** → Completely destroyed.

## Data Analysis & Logging

The game tracks performance and state through two primary log files:

* `game_state.jsonl`: Records sprite positions, velocities, and frame data every tick.
* `game_events.jsonl`: Captures specific triggers like `player_hit`, `shot_fired`, and `asteroid_split`.

---

*Developed as a modular Python game exercise using Pygame 2.6.*

```

