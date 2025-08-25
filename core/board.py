class Board:

    def __init__(self):
        self.points = [[] for _ in range(24)]
        self.bar = {'white': [], 'black': []}
        self.bear_off = {'white': [], 'black': []}

    def is_empty(self, point_index: int) -> bool:
        
        return len(self.points[point_index]) == 0 
    