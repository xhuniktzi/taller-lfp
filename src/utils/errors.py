class Errors:
    def __init__(self, char: str, row: int, col: int) -> None:
        self.char = char
        self.row = row
        self.col = col