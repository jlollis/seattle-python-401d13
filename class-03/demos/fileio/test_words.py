from words import get_words, get_non_exists, get_binary
import pytest


# def test_get_words():
#     with open('./assets/words.txt', 'r') as fd:
#         for line in fd:
#             assert len(line) > 3



def test_get_non_exists():
    with pytest.raises(FileNotFoundError) as exc:
        get_non_exists()
    assert dir(exc.value) == 'Not cool'
