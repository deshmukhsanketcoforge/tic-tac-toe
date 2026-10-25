import pytest

from main import parse_move

@pytest.mark.parametrize("text, expected", [
    ("1 1", (0, 0)),
    ("3 3", (2, 2)),
    ("2 3", (1, 2)),
    ("  2  3  ", (1, 2)),
])
def test_valid_move_is_converted_to_zero_based(text, expected):
    assert parse_move(text, 3) == expected

@pytest.mark.parametrize("text", ["a b", "one 2", "1", "1 2 3", "0.5 1", "", " ",])
def test_non_numeric_or_wrong_count_input_shows_a_clear_message(text):
    with pytest.raises(ValueError, match="two numbers"):
        parse_move(text, 3)

@pytest.mark.parametrize("text", ["0 1", "1 0", "-1 1", "1 -1", "4 1", "1 4"])
def test_out_of_range_input_shows_a_clear_message(text):
    with pytest.raises(ValueError, match="between 1 and 3"):
        parse_move(text, 3)