
from typing import Iterable

def grouped (iterable : Iterable, n : int):
    return zip(*[iter(iterable)]*n)
