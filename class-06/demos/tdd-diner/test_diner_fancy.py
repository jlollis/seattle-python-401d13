import pytest
from diner_fancy import Diner

def test_greeting(sample_diner):
    set_scripts(['Welcome to TDD Diner'])

    sample_diner.dine()


def test_bacon_eggs_ham(sample_diner):

    set_scripts(
        ['Welcome to TDD Diner', 'One order of bacon with a side of eggs and ham coming right up!'],
        ['Enter main dish: ','Enter first side: ','Enter second side: '],
        ['bacon','eggs','ham']
    )

    sample_diner.dine()


def test_olives_pickles_hummus(sample_diner):

    set_scripts(
        ['Welcome to TDD Diner', 'One order of olives with a side of pickles and hummus coming right up!'],
        ['Enter main dish: ','Enter first side: ','Enter second side: '],
        ['olives','pickles','hummus']
    )

    sample_diner.dine()


#################################################
## Below code is for helping out tests above ####
#################################################

scripts = {
    'prints' : [],
    'prompts' : [],
    'inputs' : [],
}

@pytest.fixture()
def sample_diner():
    diner = Diner(mock_print, mock_input)
    return diner

def set_scripts(prints=[], prompts=[],inputs=[]):
    scripts['prints'] = prints
    scripts['prompts'] = prompts
    scripts['inputs'] = inputs

def mock_print(msg, *args):
    if len(scripts['prints']):
        assert scripts['prints'].pop(0) == msg


def mock_input(prompt, *args):

    if len(scripts['prompts']):
        assert prompt == scripts['prompts'].pop(0)

    if len(scripts['inputs']):
        return scripts['inputs'].pop(0)

