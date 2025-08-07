````markdown
# U.S. States Guessing Game 🗺️

Welcome to the **U.S. States Guessing Game**!  
This is a fun and educational game that challenges you to name all 50 states of the United States. It's built with **Python** and the **turtle** module to create an interactive map-based experience.

---

## 🚀 Features

- **Interactive Map**: A map of the U.S. is displayed, and correctly guessed states appear on it.
- **Guess the States**: Enter the name of a state in the pop-up dialog box.
- **Score Tracking**: The game keeps track of how many states you've correctly identified out of 50.
- **Learn From Your Misses**: When you finish the game or type `exit`, a `states_to_learn.csv` file is automatically generated with all the states you missed — a great way to study for next time!

---

## 🎮 How to Get Started

Follow these simple steps to get the game running on your local machine.

### ✅ Prerequisites

- Python installed on your system. [Download Python](https://www.python.org/)
- The `pandas` library (for handling data)

---

### 🔧 Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/fsydurden/US_state_guessing_game.git
````

2. **Navigate to the project directory**

```bash
cd US_state_guessing_game
```

3. **Install required library**

```bash
pip install pandas
```

---

### ▶️ Running the Game

Run the game with the following command:

```bash
python main.py
```

A window will pop up with the map of the U.S.
Start typing your guesses into the input dialog!
To exit the game at any time, simply type `exit`.

---

## 📝 About the `remaining_states.csv` File

Don't worry if you can't name all 50 states on your first try!
When you're done playing (either by guessing all the states or by typing `exit`), the game creates a file called:

```
remaining_states.csv
```

This file contains the names of all the states you missed — making it the perfect study guide for your next attempt.

---