#  Dice Rolling Game (Python)

A simple yet fun **dice rolling game** written in Python.  
This project is beginner-friendly and demonstrates **loops, functions, and ASCII art rendering**.

---

##  How to Run

1. Install Python (3.6 or higher).  
2. Clone this repository or download the files.  
3. Run the game:
   - **In IDLE** → Open `dice_game.py` and press `F5`  
   - **In Terminal/Command Prompt**:
     ```bash
     python dice_game.py
     ```

---

##  Features
-  Roll **one or many dice**
-  Choose number of sides
-  **ASCII art dice** for 6-sided rolls
-  Displays **total of all rolls**
-  Play until you quit

---

##  Code Explanation

### Importing Required Libraries
We import the `random` module to simulate dice rolls:

   import random



### Function to Roll Dice

This function simulates rolling multiple dice:

def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls



## Main Game Loop

We keep asking the player if they want to roll again:

while True:
    num_dice = int(input("How many dice do you want to roll? "))
    num_sides = int(input("How many sides should each die have? "))

    rolls = roll_dice(num_dice, num_sides)
    print("\n You rolled:", rolls)

    if num_sides == 6:
        for line in zip(*(dice_art[roll] for roll in rolls)):
            print("  ".join(line))

    print(" Total:", sum(rolls))

    play_again = input("\nRoll again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break

## Future Enhancements

  Colored dice output

  Two-player or multiplayer mode

  GUI version using Tkinter or Pygame
