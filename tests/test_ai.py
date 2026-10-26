import random
import pytest

from ai import AIPlayer

def rng(seed=7):
    return random.Random(seed)

def test_abstract_ai_cannot_be_created():
    with pytest.raises(TypeError):
        AIPlayer(rng())