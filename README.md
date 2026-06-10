# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Choose a difficulty — Select Easy (1–20, 6 attempts), Normal (1–100, 8 attempts), or Hard (1–200, 5 attempts) from the sidebar. A secret number is randomly picked within that range.
2. Read the hint — The info bar tells you how many attempts you have left before the game locks.
3. Type a guess — Enter a number in the text field and click "Submit Guess." Decimals are accepted and rounded automatically; non-numbers show an error.
4. Receive feedback — If "Show hint" is checked, the game tells you whether your guess was too high or too low. Your guess is added to the history log.
5. Score changes with each guess — A correct guess awards 100 minus 10× (attempt number + 1) points (minimum 10). Every wrong guess deducts 5 points.
6. Win or lose — Guess the exact number before running out of attempts to win (confetti included). If you exhaust all attempts, the secret number is revealed and the game ends.
7. Start over — Click "New Game" at any time to reset the secret number, attempts, score, and history, then play again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
