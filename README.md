
<h1 align="center">
  <br>
  <pre>
╔══════════════════════════════════════════════╗
║                                              ║
║  ██████╗ ██████╗ ██████╗ ██╗███████╗████████╗║
║  ██╔══██╗██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝║
║  ██████╔╝██████╔╝██║  ██║██║█████╗     ██║   ║
║  ██╔═══╝ ██╔══██╗██║  ██║██║██╔══╝     ██║   ║
║  ██║     ██║  ██║██████╔╝██║███████╗   ██║   ║
║  ╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝   ╚═╝   ║
║                                              ║
║                 HANGMAN GAME                 ║
║                                              ║
╚══════════════════════════════════════════════╝
  </pre>
  <br>
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Task-1%20of%204-FF6B35?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/CodeAlpha-Internship-6C63FF?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-28C840?style=for-the-badge"/>
</p>

<p align="center">
  A classic terminal-based Hangman game built with pure Python.<br>
  Guess the word, one letter at a time — before the man is hanged.
</p>

---

## Preview

```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

  Word: p _ t h _ n
  Wrong guesses left: 1
  Wrong letters: a, e, i, o, z

  Guess a letter: _
```

---

## Features

- 5 predefined mystery words chosen at random each round
- 7-stage ASCII art gallows that updates live
- Tracks correct and incorrect guesses separately
- Displays remaining attempts and wrong letters after every turn
- Input validation — rejects non-letters and already-guessed letters
- Play again loop after each round

---

## How to Run

**Requirements:** Python 3.x — no external libraries needed.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/CodeAlpha_HangmanGame.git

# Navigate into the folder
cd CodeAlpha_HangmanGame

# Run the game
python hangman.py
```

---

## How to Play

| Step | Action |
|------|--------|
| 1 | A random word is selected and shown as blanks |
| 2 | Type a single letter and press Enter |
| 3 | Correct guess fills in the blank(s) |
| 4 | Wrong guess adds a body part to the gallows |
| 5 | Win by guessing all letters before 6 wrong guesses |
| 6 | Lose when the hangman is fully drawn |

---

## Game Rules

- You get **6 incorrect guesses** before game over
- Each guess must be a **single alphabetical letter**
- You **cannot repeat** a letter you already guessed
- The word is revealed if you lose

---

## Project Structure

```
CodeAlpha_HangmanGame/
│
├── hangman.py       # Main game file
└── README.md        # Project documentation
```

---

## Concepts Used

| Concept | Usage |
|---------|-------|
| `random` | Picks a random word each round |
| `while` loop | Keeps the game running until win or loss |
| `if-else` | Checks guesses and game conditions |
| `strings` | Processes and displays the word |
| `lists / sets` | Tracks guessed and remaining letters |
| `functions` | Organises game logic into clean blocks |

---

## Internship

This project was built as **Task 1** of the **CodeAlpha Python Programming Internship**.

> CodeAlpha is a leading software development company focused on building scalable and efficient software solutions. This internship empowers students to master Python fundamentals through real-world projects.

**Intern:** `SAMIRAN HAZRA`  
**Domain:** Python Programming  
**Task:** 1 — Hangman Game  

---

## Connect

<p>

  </a>
  <a href="https://github.com/cypherbytes01">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

---

<p align="center">
  Made with Python — CodeAlpha Internship 2026
</p>

