import pytest
from rock_paper_scissors_lizard_spock import rpsls

@pytest.mark.parametrize("pl1, pl2, expected", [
    ('rock', 'lizard', 'Player 1 Won!'),
    ('paper', 'rock', 'Player 1 Won!'),
    ('scissors', 'lizard', 'Player 1 Won!'),
    ('lizard', 'paper', 'Player 1 Won!'),
    ('spock', 'rock', 'Player 1 Won!'),
    ('lizard','scissors', 'Player 2 Won!'),
    ('spock','lizard', 'Player 2 Won!'),
    ('paper','lizard', 'Player 2 Won!'),
    ('scissors','spock', 'Player 2 Won!'),
    ('rock','spock', 'Player 2 Won!'),
    ('rock', 'rock', 'Draw!'),
    ('spock', 'spock', 'Draw!'),
])
def test_fixed(pl1, pl2, expected):
    assert rpsls(pl1, pl2) == expected
