def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for a given difficulty level.

    Args:
        difficulty (str): The difficulty setting. Expected values are
            "Easy", "Normal", or "Hard".

    Returns:
        tuple[int, int]: A ``(low, high)`` pair representing the inclusive
        guess range.
    """
    # FIXME: Logic breaks here
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse user input string into an integer guess.

    Args:
        raw (str | None): The raw string entered by the user.

    Returns:
        tuple[bool, int | None, str | None]: A ``(ok, guess_int,
        error_message)`` tuple. ``ok`` is ``True`` on success; on failure
        ``guess_int`` is ``None`` and ``error_message`` contains a
        human-readable description of the problem.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare a guess to the secret number and return the outcome.

    Args:
        guess (int): The player's guessed value.
        secret (int): The secret target value.

    Returns:
        tuple[str, str]: A ``(outcome, message)`` pair. ``outcome`` is one
        of ``"Win"``, ``"Too High"``, or ``"Too Low"``; ``message`` is a
        display string for the player.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

#FIX: Guessing too high will no longer gives points on even numbered attempts.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Calculate and return the updated score based on the round outcome.

    Scoring rules:

    - ``"Win"``: Awards ``100 - 10 * (attempt_number + 1)`` points,
      minimum 10.
    - ``"Too High"`` or ``"Too Low"``: Applies a 5-point penalty.
    - Any other outcome: Score is unchanged.

    Args:
        current_score (int): The player's score before this round's result.
        outcome (str): The result of the guess (``"Win"``, ``"Too High"``,
            or ``"Too Low"``).
        attempt_number (int): Zero-based attempt index used to scale win
            points.

    Returns:
        int: The updated score after applying the outcome rules.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
