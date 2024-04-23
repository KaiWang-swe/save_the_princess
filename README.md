# Save The Princess

## Overview
"Save The Princess" is a text-based adventure game that invites players to embark on a thrilling quest filled with choices that dictate the storyline and lead to multiple endings. Written in Python and utilizing object-oriented programming (OOP) principles, the game is designed to be replayable, with each playthrough offering new paths and outcomes.

## Game Features
- **Text-based Adventure**: Explore a richly described world through text and make choices that influence the narrative.
- **Multiple Endings**: Your decisions lead to different outcomes, providing a unique experience on each playthrough.
- **Replayable**: With various choices leading to different endings, the game encourages multiple playthroughs to explore all possible scenarios.

## File Structure
- `play.py`: The main entry point of the game. Run this file to start your adventure.
- `characters.py`: Defines the classes for the player and other characters you will interact with during your quest.
- `tools.py`: Contains tools and utilities for game mechanics, such as managing game states, inventory, and interactions.

## Technical Requirements
- **Python Version**: The game is compatible with Python 3.6 and newer versions. Developed using Python 3.12.2, it ensures compatibility with most recent Python installations.

## Modules and OOP Usage
### `characters.py`
This module employs object-oriented programming to define the game's characters. Each character, including the protagonist and the princess, is modeled as an object, encapsulating unique attributes and methods. Polymorphism is featured in method overrides, particularly in character interaction mechanisms that vary by character type.

### `tools.py`
`tools.py` serves as a utility module supporting the game's operational mechanics. It includes classes and methods for handling game events, inventory management, and player decisions, illustrating the use of inheritance to build upon basic functionality for advanced game tools.

## Design Philosophy
The game's architecture emphasizes modular design and OOP to enhance maintainability and scalability. By separating character definitions and game mechanics into distinct modules, the game code remains organized and easy to manage. This modular approach not only simplifies debugging and expansion but also helps in encapsulating functionality, reducing dependency conflicts among components.

Enjoy "Save The Princess" and uncover all the narratives woven into the heart of this enchanting quest. Each choice could be the key to a new ending, so choose wisely!

## Running the Game
To play the game, simply execute the `play.py` script in a Python environment that meets the version requirements. Enjoy the adventure as you apply your wits and bravery to save the princess!

## Note
This README is focused on the game's design and architecture, omitting setup and execution instructions to concentrate on explaining its technical and narrative structure.

