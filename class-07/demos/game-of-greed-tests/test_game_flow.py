import pytest
from game import Game

def test_flow_yes():

    prints = ['Welcome to Game of Greed','Check back tomorrow :D']
    prompts = ['Wanna play?']
    responses = ['y']

    def mock_print(*args):
        if len(prints):
            current_print = prints.pop(0)
            assert args[0] == current_print

    def mock_input(*args):
        if len(prompts):
            current_prompt = prompts.pop(0)
            assert args[0] == current_prompt

        if len(responses):
            current_response = responses.pop(0)
            return current_response

    game = Game(mock_print, mock_input)

    game.play()

def test_flow_no():

    prints = ['Welcome to Game of Greed','OK. Maybe later']
    prompts = ['Wanna play?']
    responses = ['no']

    def mock_print(*args):
        if len(prints):
            current_print = prints.pop(0)
            assert args[0] == current_print

    def mock_input(*args):
        if len(prompts):
            current_prompt = prompts.pop(0)
            assert args[0] == current_prompt

        if len(responses):
            current_response = responses.pop(0)
            return current_response

    game = Game(mock_print, mock_input)

    game.play()
