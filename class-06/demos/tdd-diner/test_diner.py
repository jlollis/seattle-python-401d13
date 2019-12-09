import pytest
from diner import Diner

def test_diner_instance():
    diner = Diner()
    assert diner


def test_greeting():

    prints = ['Welcome to TDD Diner','Home of the hottest cup of joe']
    prompts = ['Enter main dish: ','Enter side dish: ','Enter beverage: ']
    responses = []

    def print_for_testing(message):
        if len(prints):
            assert message == prints.pop(0)

    def input_for_testing(prompt):
        if len(prompts):
            assert prompt == prompts.pop(0)

    diner = Diner(print_for_testing, input_for_testing)

    diner.dine()

def test_final_order():

    prints = [
        'Welcome to TDD Diner',
        'Home of the hottest cup of joe',
        'One order of lasagna with ceasar salad and whisky coming up!'
    ]
    prompts = ['Enter main dish: ','Enter side dish: ','Enter beverage: ']
    responses = ['lasagna','ceasar salad','whisky']

    def print_for_testing(message):
        assert message == prints.pop(0)

    def input_for_testing(prompt):
        assert prompt == prompts.pop(0)
        return responses.pop(0)

    diner = Diner(print_for_testing, input_for_testing)

    diner.dine()



