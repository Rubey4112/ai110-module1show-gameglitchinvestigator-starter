# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

The first problem I noticed was that the hint is reversed. The hint would tell me to go higher even though I was above the secret number or it tells me to go lower when I was below the secret number. A second problem with the game is that clicking new game after reaching game over / win state doesn't properly restart the game.
Other problems that I noticed:
- Clicking submit guess sometime doesn't properly update the value of my current attempt
- Easy mode secret value should be between 1-20 but the current value can be outside the range. Same thing with hard mode.
- The range of value for Hard difficulty is smaller then Normal difficulty. It likely should be larger
- Sometime guessing the wrong value gives points rather than subtract points

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

I utilized Claude to help me debug. The AI succefully fixed the incorrect hint problem. I visually verified the fix and checked it in game.
One incorrect suggest that the AI made (this time it was CoPilot using inline chat) was when I asked it to rewrite the logic_utils import statement in the `test_game_logic.py` file. I visually checked the code and all CoPilot did was rewrote the import statement to be two lines without actually changing anything logically. I eventually asked Claude to fix the import statement while providing it the pytest error code `E   ModuleNotFoundError: No module named 'logic_utils'`. 
I also tried messing around with the agent mode feature of Claude but I just found it to be more cumbersome then helpful for a simple program like this.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

My method for testing my fix for the hint bug was to test a value that is 1 above and 1 below the secret value. Since if the hint function properly for the such a small incremement from the secret value then it reasonable that the hint will also works for other value. Certainly, it is not an exhautives test but I considered it to be good enough and added it to my pytest file using Claude.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
