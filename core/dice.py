import random

class Dice:
    def __init__(self, seed: int | None = None):
        self.seed = seed
        if seed is not None:
            random.seed(seed)

    def roll(self) -> tuple[int, int]:
        return random.randint(1, 6), random.randint(1, 6)

    def is_double(self, a: int, b: int) -> bool:
        return a == b
