# ForestGate
This is a simple text-based adventure game implemented using the Tkinter library in Python. In the game, you find yourself in a mysterious abandoned cottage in the forest and your goal is to find your way home. The game provides various options and choices for you to make as you explore the environment.

## Dependencies
- Python 3.x
- tkinter
- PIL (Python Imaging Library)
- pygame

Make sure you have these dependencies installed before running the game.

## How to Run
To run the game, execute the Python script containing the code. The game will launch in a new window.

```bash
python adventure_game.py
```

## Gameplay
- Upon launching the game, you will see a text window displaying the game's storyline and prompts.
- The available options and actions will be shown as numbered choices.
- To make a choice, enter the corresponding number in the entry field and click the "Submit" button.
- You can also use the number keys on your keyboard to make a choice directly.
- As you progress through the game, different events will occur based on your choices.
- The game also includes sound effects and background music to enhance the experience.
- Your score will be displayed in the score label, which increases or decreases based on your actions.
- The game provides a menu bar with additional options such as multiplayer mode and credits.

## Functions and Features
- `intro()`: Displays the game's introduction and plays the introductory sound and background music.
- `check_window()`: Displays a message indicating that the windows are boarded up.
- `open_door()`: Displays a message indicating that the door is locked and you need to find the key.
- `search_room()`: Displays a message indicating that you have found the key under the pillow and have unlocked the door, leading to a successful escape.
- `explore_forest()`: Displays a message indicating that you decide to explore the forest and prompts you to investigate the well or return to the cottage.
- `investigate_well()`: Displays a message indicating that you approach the well, see a glimmering object (amulet), and then fall into darkness.
- `make_decision(decision)`: Handles the user's decision by calling the corresponding function based on the choice made.
- `handle_button_click()`: Gets the decision from the entry field, clears the field, and calls `make_decision()` function.
- `toggle_fullscreen(event=None)`: Toggles the game window between fullscreen and windowed mode.
- `handle_key_press(event)`: Handles the number key presses by calling `make_decision()` function.
- `update_score(points)`: Updates the score by adding or subtracting the given points.
- `play_sound(sound_file)`: Plays a sound effect using the pygame library.
- `play_music(music_file)`: Plays background music using the pygame library.
- `open_github(event)`: Opens the GitHub repository of the game in the default web browser.
- `show_credits()`: Displays a separate window showing the credits for the game.
- `center_window(window)`: Centers a given window on the screen.
- `show_multiplayer()`: Displays information about the multiplayer mode and provides options to host or join a game.
- `host_multiplayer_game()`: Displays an error message indicating the need for an internet connection to host a multiplayer game.
- `join_multiplayer_game()`: Displays an error message indicating the need for an internet connection to join a multiplayer game.
- `back_to_main_menu()`: Resets the game state and returns to the main menu.


## Screenshots 
![111111111111](https://github.com/CryptGodSon/ForestGate/assets/106864633/7616f2e3-44b5-458b-8ec0-707ede339e1f)

## Credits
This game was created by CryptGodSon. To learn more about the creator, you can visit their [GitHub profile](https://github.com/CryptGodSon

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute to the project by creating pull requests or submitting issues for any improvements or bug fixes.
