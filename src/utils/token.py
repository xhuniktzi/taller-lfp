class Token:
    def __init__(self, name: str, value: str, row: int, col: int):
        self.name = name
        self.value = value
        self.row = row
        self.col = col