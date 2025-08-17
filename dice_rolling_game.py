"""
Dice Rolling Game
Run this in VS Code's terminal:
    python dice_game.py
"""

import random
import sys

DICE_ART = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘",
    ),
}

def render_dice(values):
    """Return a multi-line string that displays ASCII dice side by side."""
    rows = [""] * len(next(iter(DICE_ART.values())))
    for val in values:
        art = DICE_ART.get(val)
        if art is None:
            raise ValueError(f"Unsupported die face: {val}")
        for i, line in enumerate(art):
            rows[i] += line + "  "
    return "\n".join(rows)

def roll_dice(n=1, sides=6):
    """Roll n dice each with 'sides' sides and return a list of integers."""
    if n <= 0 or sides <= 1:
        raise ValueError("Number of dice must be > 0 and sides must be > 1")
    return [random.randint(1, sides) for _ in range(n)]

def ask_int(prompt, default=None, min_val=None, max_val=None):
    while True:
        raw = input(prompt).strip()
        if not raw and default is not None:
            return default
        try:
            val = int(raw)
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Please enter a number between {min_val} and {max_val}.")
                continue
            return val
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("🎲 Dice Rolling Game")
    print("-" * 22)
    n = ask_int("How many dice? (default 2): ", default=2, min_val=1, max_val=20)
    sides = ask_int("How many sides per die? (default 6): ", default=6, min_val=2, max_val=100)
    show_art = input("Show ASCII dice art? (Y/n): ").strip().lower() not in {"n", "no"}

    while True:
        values = roll_dice(n, sides)
        total = sum(values)
        if sides == 6 and show_art and n <= 8 and all(1 <= v <= 6 for v in values):
            print(render_dice(values))
        else:
            print(f"Rolls: {values}")
        print(f"Total: {total}\n")

        again = input("Roll again? (Y/n): ").strip().lower()
        if again in {"n", "no"}:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting. Bye!")
        sys.exit(0)
