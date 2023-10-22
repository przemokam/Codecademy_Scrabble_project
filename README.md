# Codecademy_Scrabble_project
Welcome in my wersion of "Scrabble" Codecademy project in Python
This Python-based project is designed to compute Scrabble scores for given words, based on the standard Scrabble letter-point assignment. It also includes a function to calculate the total score of words played by different players.

## Features

**Scrabble Dictionary:** A dictionary (letter_to_points) of all Scrabble letters mapped to their respective point values.

**Score Calculation:** A function (score_word) to compute the Scrabble score of any word, considering both letters and any non-letter characters (e.g., '!' will contribute 0 points).

**Player Word Tracking:** A dictionary (player_to_words) that represents words played by different players.

**Player Score Computation:** Computes total scores of all words played by each player and stores them in a dictionary (player_to_points).

## How to Use

1. Copy the file: [Codecademy_scrabble.py](../main/Codecademy_scrabble.py) 

2. Navigate to your download directory

3. Run the Script:

```bash

python3 Codecademy_scrabble.py
```
Get Score for a Word: After running the script, input a word when prompted to get its Scrabble score.

Player Scores: At the end of the script, see the printed dictionary of players with their total scores.

## Requirements

    Python 3.x

## Credits

> This project was inspired by the Scrabble exercise from Codecademy's Learn Python 3 Course.
