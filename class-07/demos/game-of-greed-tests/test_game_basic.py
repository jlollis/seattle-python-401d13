import pytest
from game import Game
import game as game_module

def test_module_doc():
    assert game_module.__doc__ != None

def test_create(game):
    assert isinstance(game, Game)

@pytest.mark.parametrize("num_dice",[1,2,3,4,5,6])
def test_roll(game, num_dice):
    roll = game.do_roll(num_dice)
    for val in roll:
        assert 1 <= val <= 6


@pytest.fixture()
def game():
    return Game()

