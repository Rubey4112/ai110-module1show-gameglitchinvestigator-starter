from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_hint_says_go_lower_when_guess_too_high():
    # If guess is above the secret, the hint message should tell the player to go lower
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()

def test_hint_says_go_higher_when_guess_too_low():
    # If guess is below the secret, the hint message should tell the player to go higher
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()

# Edge case 1: negative guess is accepted by parse_guess but falls outside the
# valid game range (1–100). The parser should reject it or the caller must validate.
def test_negative_guess_is_out_of_range():
    ok, value, error = parse_guess("-5")
    # A negative number should be flagged as invalid for this game.
    assert not ok, "parse_guess should reject negative numbers outside the game range"

# Edge case 2: a decimal string like "3.9" should be rejected — the game only
# accepts whole numbers, so decimals are invalid input.
def test_decimal_input_is_rejected():
    ok, value, error = parse_guess("3.9")
    assert not ok, "parse_guess should reject decimal numbers"
    assert value is None
    assert error is not None

# Edge case 3: passing None as a guess triggers the TypeError fallback branch in
# check_guess, which then tries to compare str(None) > secret (an int) — raising
# another unhandled TypeError in Python 3.
def test_none_guess_does_not_crash():
    try:
        result = check_guess(None, 50)
        # If it doesn't raise, we at least expect a well-defined outcome string.
        assert result[0] in ("Win", "Too High", "Too Low")
    except TypeError:
        assert False, "check_guess raised an unhandled TypeError when guess is None"
